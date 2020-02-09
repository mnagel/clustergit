# clustergit

clustergit allows you to run git commands on multiple repositories at once.
It is especially useful to run `git status` recursively on one folder.

clustergit supports `git status`, `git pull`, `git push`, and more.

## Screenshot
![clustergit screenshot](/doc/clustergit.png?raw=true "clustergit screenshot")

To reproduce the above locally, run:

```bash
cd doc
bash demo.sh
cd demo
clustergit
clustergit --warn-unversioned --pull
```

## Installation

Make the script executable and drop it somewhere in your $PATH.

## Dependencies

 * python3
 
For latest version with python 2.7 support see:
https://github.com/mnagel/clustergit/releases/tag/python27

## Usage

Usage: clustergit [options]

clustergit will scan through all subdirectories looking for a .git directory.
When it finds one it'll look to see if there are any changes and let you know.
If there are no changes it can also push and pull to/from a remote location.

## Options

```
usage: clustergit [-h] [-d DIRNAME] [-v] [-a ALIGN] [-r REMOTE] [--push] [-p]
                  [-f] [--exec COMMAND] [-c] [-C] [-q] [-H] [-R] [-n]
                  [-b BRANCH] [--recursive] [--skip-symlinks] [-e EXCLUDE]
                  [-B CBRANCH] [--warn-unversioned]
                  [--workers THREAD_POOL_WORKERS] [--print-asap]

clustergit will scan through all subdirectories looking for a .git directory.
When it finds one it'll look to see if there are any changes and let you know.
If there are no changes it can also push and pull to/from a remote location.

optional arguments:
  -h, --help            show this help message and exit
  -d DIRNAME, --dir DIRNAME
                        The directory to parse sub dirs from (default: .)
  -v, --verbose         Show the full detail of git status (default: False)
  -a ALIGN, --align ALIGN
                        Repo name align (space padding) (default: 40)
  -r REMOTE, --remote REMOTE
                        Set the remote name (remotename:branchname) (default:
                        )
  --push                Do a 'git push' if you've set a remote with -r it will
                        push to there (default: False)
  -p, --pull            Do a 'git pull' if you've set a remote with -r it will
                        pull from there (default: False)
  -f, --fetch           Do a 'git fetch' if you've set a remote with -r it
                        will fetch from there (default: False)
  --exec COMMAND, --execute COMMAND
                        Execute a shell command in each repository (default: )
  -c, --clear           Clear screen on startup (default: False)
  -C, --count-dirty     Only display a count of not-clean repos (default:
                        False)
  -q, --quiet           Skip startup info (default: False)
  -H, --hide-clean      Hide clean repos (default: False)
  -R, --relative        Print relative paths (default: False)
  -n, --no-colors       Disable ANSI color output. Disregard the alleged
                        default -- color is on by default. (default: True)
  -b BRANCH, --branch BRANCH
                        Warn if not on this branch. Set to empty string (-b
                        '') to disable this feature. (default: master)
  --recursive           Recursively search for git repos (default: False)
  --skip-symlinks       Skip symbolic links when searching for git repos
                        (default: False)
  -e EXCLUDE, --exclude EXCLUDE
                        Regex to exclude directories (default: [])
  -B CBRANCH, --checkout-branch CBRANCH
                        Checkout branch (default: None)
  --warn-unversioned    Prints a warning if a directory is not under git
                        version control (default: False)
  --workers THREAD_POOL_WORKERS
                        Workers in thread pool for parallel execution
                        (default: 4)
  --print-asap          Print repository status as soon as possible not
                        preserving order (default: False)

```

## Contact

via https://github.com/mnagel/clustergit

## Credits

* show_status by Mike Pearce: https://github.com/MikePearce/Git-Status
* patches to show_status by ilor: https://github.com/ilor/Git-Status

## License

Files:

* all files

Copyright:

* 2010 Mike Pearce mike@mikepearce.net
* 2010 catchamonkey chris@sedlmayr.co.uk
* 2015 sedrubal sebastian.endres@online.de
* 2011-2020 Michael Nagel ubuntu@nailor.devzero.de

License:

* Mike Pearce: "Feel free to use it how you like, no licence required."
* catchamonkey: "I guess whatever the original show_status's license is would apply to my patches. Other than that, I consider my additions to be public domain-ish or 2-clause BSD."
* Michael Nagel: "Donated into the Public Domain."
* sedrubal: "Donated into the Public Domain. Whenever this project gets a 'real' license, I'd prefer a GPL"
