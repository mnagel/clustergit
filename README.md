# clustergit

clustergit allows you to run git commands on multiple repositories at once.
It is especially useful to run `git status` recursively on one folder.

clustergit supports `git status`, `git pull`, `git push`, and more.

It is a renamed and slightly improved version of Mike Pearce's `show_status`.

## Screenshot
![clustergit screenshot](/doc/clustergit.png?raw=true "clustergit screenshot")

To reproduce the above locally, run:
```
cd doc
bash demo.sh
cd demo
clustergit
clustergit --warn-unversioned --pull
```

## Installation

Make the script executable and drop it somewhere in your $PATH.

## Usage

Usage: clustergit [options]

clustergit will scan through all subdirectories looking for a .git directory.
When it finds one it'll look to see if there are any changes and let you know.
If there are no changes it can also push and pull to/from a remote location.

## Options

```
  -h, --help            show this help message and exit
  -d DIRNAME, --dir=DIRNAME
                        The directory to parse sub dirs from
  -v, --verbose         Show the full detail of git status
  -a ALIGN, --align=ALIGN
                        Repo name align (space padding)
  -r REMOTE, --remote=REMOTE
                        Set the remote name (remotename:branchname)
  --push                Do a 'git push' if you've set a remote with -r it will
                        push to there
  -p, --pull            Do a 'git pull' if you've set a remote with -r it will
                        pull from there
  -c, --clear           Clear screen on startup
  -C, --count-dirty     Only display a count of not-clean repos
  -q, --quiet           Skip startup info
  -H, --hide-clean      Hide clean repos
  -R, --relative        Print relative paths
  -n, --no-colors       Disable ANSI color output
  -b BRANCH, --branch=BRANCH
                        Warn if not on this branch
  --recursive           Recursively search for git repos
  -e EXCLUDE, --exclude=EXCLUDE
                        Regex to exclude directories
  -B CBRANCH, --checkout-branch=CBRANCH
                        Checkout branch
  --warn-unversioned    Prints a warning if a directory is not under git
                        version control
```

## Contact

via https://github.com/mnagel/clustergit

## Credits

* show_status by Mike Pearce: https://github.com/MikePearce/Git-Status
* patches to show_status by ilor: https://github.com/ilor/Git-Status

## License

Files:

* clustergit, README.*

Copyright:

* 2010 Mike Pearce mike@mikepearce.net
* 2010 catchamonkey chris@sedlmayr.co.uk
* 2011-2014 Michael Nagel ubuntu@nailor.devzero.de

License:

* Mike Pearce: "Feel free to use it how you like, no licence required."
* catchamonkey: "I guess whatever the original show_status's license is would apply to my patches. Other than that, I consider my additions to be public domain-ish or 2-clause BSD."
* Michael Nagel: "Donated into the Public Domain."
