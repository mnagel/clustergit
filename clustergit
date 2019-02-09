#!/usr/bin/env python3

""" run git commands on multiple git clones
inspired by https://github.com/mnagel/clustergit """

import argparse
import asyncio
import glob
import os
import re
import subprocess
import sys
from functools import wraps

LOOP = asyncio.get_event_loop()


async def main(args, argv):
    def clean(filename):
        if args.absolute:
            return filename
        if uniq_repo:
            return os.path.basename(filename)
        return filename[len(args.dir) :].strip("/")

    def max_padding(repos):
        if args.absolute:
            return max(map(len, repos)) + 1
        return max(map(len, repos)) - len(args.dir) + 1

    def _print(repo, status):
        if args.hide_clean and "Clean" in status:
            return
        print(f"{clean(repo):<{padding}}: {status}", flush=True)

    async def loop(method, *args):
        """ helper method to keep all actions under one interface """
        async for repo, status in method(repos, *args):
            _print(repo, status)

    repos = find_repos(args.dir)
    uniq_repo = 1 == len(repos)
    padding = max_padding(repos)
    parser = Parser(args)
    status = GitAction("status", parser.status)

    if args.status:
        await loop(repos_statuses, status)
    elif args.branch:
        branch = GitAction("status", parser.branch)
        await loop(repos_statuses, branch)
    elif args.fetch:
        fetch_all = GitAction(["fetch", "--all"], parser.fetch)
        await loop(repos_action, fetch_all, status)
    elif args.pull:
        pull = GitAction("pull", parser.pull)
        await loop(repos_action, pull, status)
    elif args.push:
        push = GitAction("push", parser.push)
        await loop(repos_action, push, status)
    elif args.exec:
        await loop(execute, args.exec.split(), parser.exec)
    else:
        print(*[clean(repo) for repo in repos], sep="\n")


class GitAction:
    def __init__(self, action, parser):
        self.action = git_async_action(action)
        self.parser = parser


async def repos_statuses(repos, git_status: GitAction):
    status = iter_as_completed(git_status.action)
    for task in status(repos):
        errcode, repo, out = await task
        yield repo, git_status.parser(errcode, out)


async def repos_action(repos, principal: GitAction, secondary: GitAction):
    @iter_as_completed
    async def git_chain(task):
        """
        expects the result from another git_async_action
        allows them chaining together and keep yielding in completion order
        """
        errcode1, repo, out1 = await task
        errcode2, _, out2 = await secondary.action(repo)
        return errcode1, errcode2, repo, out1, out2

    action = iter_as_completed(principal.action)
    for task in git_chain(action(repos)):
        e1, e2, repo, o1, o2 = await task
        yield repo, ", ".join([principal.parser(e1, o1), secondary.parser(e2, o2)])


async def execute(repos, command, parser):
    @iter_as_completed
    @async_io
    def _run(repo, command):
        errcode, out = run(command, repo)
        return errcode, repo, out.strip()

    for task in _run(repos, command):
        errcode, repo, out = await task
        yield repo, parser(errcode, out)


def iter_as_completed(method):
    """
    transforms an async function taking one item into a list processing function
    yielding its result in completion order (first finished first yielded)
    """

    @wraps(method)
    def inner(iterable, *a, **kw):
        return asyncio.as_completed([method(i, *a, **kw) for i in iterable])

    return inner


def find_repos(base_dir):
    search_glob = os.path.join(base_dir, "**/.git")
    return [f[:-5] for f in glob.glob(search_glob, recursive=True)]


def async_io(func):
    """
    Transforms any io function in the standard libraries to be used in async mode
    by wrapping them in thread, but using async/await syntax.
    """

    @wraps(func)
    def threaded_executor(*args):
        return LOOP.run_in_executor(None, func, *args)

    return threaded_executor


def git_async_action(action):
    """ Run a git command in async """

    @async_io
    def inner(repo):
        """ on the given repository """
        status, out = run_git_repo(repo, action)
        return status, repo, out

    return inner


def run_git_repo(repo, action):
    """ Run a git command on the given repository """
    command = ["git"]
    if type(action) == list:
        command += action
    elif type(action) == str:
        command.append(action)
    return run(command, repo)


class Parser:
    """ Parse a user readable message from the stdout/stderr of git """

    def __init__(self, args):
        # if I wanted to customize the output based on user's options
        self.args = args

    def fetch(self, errcode, out):
        fetch = []
        if "error: " in out:
            fetch.append(self.colorize(Colors.FAIL, "Fetch fatal"))
        else:
            fetch.append(self.colorize(Colors.OKPURPLE, "Fetched"))
        if errcode != 0:
            fetch.append(self.colorize(Colors.FAIL, "Fetch unsuccessful"))
        return ", ".join(fetch)

    def status(self, errcode, out):
        messages = []
        clean = True

        if "On branch master" not in out and "On branch develop" not in out:
            branch = out.splitlines()[0].replace("On branch ", "")
            messages.append(self.colorize(Colors.OKBLUE, f"On branch {branch}"))

        if "nothing added to commit but untracked files present" in out:
            messages.append(self.colorize(Colors.WARNING, "Untracked files"))
            clean = False

        if "Changes not staged for commit" in out:
            messages.append(self.colorize(Colors.FAIL, "Changes"))
            clean = False

        if "Your branch is ahead of" in out:
            messages.append(self.colorize(Colors.FAIL, "Unpushed commits"))

        if clean:
            messages = [self.colorize(Colors.OKGREEN, "Clean")] + messages

        return ", ".join(messages)

    def branch(self, errcode, out):
        branch = out.splitlines()[0].replace("On branch ", "")
        return self.colorize(Colors.OKGREEN, branch)

    def pull(self, errcode, out):
        messages = []
        if re.search(r"Already up.to.date", out):
            messages.append(self.colorize(Colors.OKGREEN, "Pulled nothing"))
        elif "CONFLICT" in out:
            messages.append(self.colorize(Colors.FAIL, "Pull conflict"))
        elif "fatal: No remote repository specified." in out:
            messages.append(self.colorize(Colors.WARNING, "Pull remote not configured"))
        elif "fatal: " in out:
            messages.append(self.colorize(Colors.FAIL, "Pull fatal"))
        elif "error: " in out:
            messages.append(self.colorize(Colors.FAIL, "Pull error"))
        else:
            messages.append(self.colorize(Colors.OKBLUE, "Pulled"))

        return ", ".join(messages)

    def push(self, errcode, out):
        messages = []
        error = False
        if "read-only" in out:
            messages.append(self.colorize(Colors.WARNING, "Read-only remote"))
            error = True
        if re.search(r"\[(remote )?rejected\]", out):
            messages.append(self.colorize(Colors.FAIL, "Push rejected"))
            error = True
        if "denied" in out:
            messages.append(self.colorize(Colors.FAIL, "Permission denied"))
            error = True

        if "Everything up-to-date" in out:
            messages.append(self.colorize(Colors.OKGREEN, "Already up-to-date"))
            error = True

        if not error:
            messages.append(self.colorize(Colors.OKBLUE, "Push accepted"))

        return ", ".join(messages)

    def exec(self, errcode, out):
        messages = []
        if errcode != 0:
            messages.append(self.colorize(Colors.FAIL, f"Return code {errcode}"))
        else:
            messages.append(self.colorize(Colors.OKGREEN, f"Return code {errcode}"))
        messages.append(out)

        return "\n".join(messages)

    def colorize(self, color, message):
        if os.name == "nt" or self.args.no_color:
            return message
        return f"{color}{message}{Colors.ENDC}"


class Colors:
    OKBLUE = "\033[94m"  # write operation succeeded
    OKGREEN = "\033[92m"  # readonly operation succeeded
    OKPURPLE = "\033[95m"  # readonly (fetch) operation succeeded
    WARNING = "\033[93m"  # operation succeeded with non-default result
    FAIL = "\033[91m"  # operation did not succeed
    ENDC = "\033[0m"  # reset color


def run(command, cwd=None):
    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, cwd=cwd)
        return 0, output.decode("utf-8")
    except subprocess.CalledProcessError as e:
        return e.returncode, e.output.decode("utf-8")


def parse_args(argv):
    parser = argparse.ArgumentParser(
        description="""
        {0} will scan through all subdirectories looking for a .git directory.
        When it finds one it'll look to see if there are any changes and let you know.
        If there are no changes it can also push and pull to/from a remote location.
        """.format(
            os.path.basename(__file__)
        ).strip()
    )
    parser.add_argument(
        "dir", help="directory to parse sub dirs from", type=os.path.abspath
    )
    actions = parser.add_mutually_exclusive_group()
    actions.add_argument("-s", "--status", help="show status", action="store_true")
    actions.add_argument("-b", "--branch", help="show branch", action="store_true")
    actions.add_argument("-f", "--fetch", help="fetch from remote", action="store_true")
    actions.add_argument("-p", "--pull", help="pull from remote", action="store_true")
    actions.add_argument("-P", "--push", help="push to remote", action="store_true")
    actions.add_argument("--exec", help="execute custom command on each repo")
    parser.add_argument(
        "-A", "--absolute", help="display absolute paths", action="store_true"
    )
    parser.add_argument(
        "-H", "--hide-clean", help="hide clean repos", action="store_true"
    )
    parser.add_argument(
        "-n", "--no-color", help="don't colorize output", action="store_true"
    )
    return parser.parse_known_args(argv)


if __name__ == "__main__":
    try:
        LOOP.run_until_complete(main(*parse_args(sys.argv[1:])))
    except KeyboardInterrupt:
        print()
