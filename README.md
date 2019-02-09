# clustergit

clustergit allows you to run git commands on multiple repositories *at once*.
It is especially useful to run `git status` recursively on one folder.

clustergit supports `git status`, `git pull`, `git push`, and more.

It is a slightly improved version of Michael Nagel's `clustergit` and Mike Pearce's `show_status`.

[![asciicast](https://asciinema.org/a/NFTmtyQ0dui0DJB36PEhj23mR.svg)](https://asciinema.org/a/NFTmtyQ0dui0DJB36PEhj23mR)

## Installation

Make the script executable and drop it somewhere in your $PATH.

## Dependencies

 * python3.6 or higher

## Usage

Usage: clustergit <directory> [options]

clustergit will scan through all subdirectories looking for a .git
directory. When it finds one it'll look to see if there are any changes and
let you know. It can also push and pull to/from a remote location.

## Options

```
usage: clustergit [-h] [-s | -b | -f | -p | -P | --exec EXEC] [-A] [-H] [-n]
                  dir

clustergit will scan through all subdirectories looking for a .git directory.
When it finds one it'll look to see if there are any changes and let you know.
If there are no changes it can also push and pull to/from a remote location.

positional arguments:
  dir               directory to parse sub dirs from

optional arguments:
  -h, --help        show this help message and exit
  -s, --status      show status
  -b, --branch      show branch
  -f, --fetch       fetch from remote
  -p, --pull        pull from remote
  -P, --push        push to remote
  --exec EXEC       execute custom command on each repo
  -A, --absolute    display absolute paths
  -H, --hide-clean  hide clean repos
  -n, --no-color    don't colorize output
```

## Contact

via https://github.com/jRimbault/clustergit

## Credits

* clustergit by Michael Nagel https://github.com/mnagel/clustergit
* show_status by Mike Pearce: https://github.com/MikePearce/Git-Status
* patches to show_status by ilor: https://github.com/ilor/Git-Status

## License

Files:

* all files

Copyright:

* 2010 Mike Pearce mike@mikepearce.net
* 2010 catchamonkey chris@sedlmayr.co.uk
* 2011-2016 Michael Nagel ubuntu@nailor.devzero.de
* 2015 sedrubal sebastian.endres@online.de
* 2019 Jacques Rimbault jacques.rimbault@gmail.com

License:

* Mike Pearce: "Feel free to use it how you like, no licence required."
* catchamonkey: "I guess whatever the original show_status's license is would apply to my patches. Other than that, I consider my additions to be public domain-ish or 2-clause BSD."
* Michael Nagel: "Donated into the Public Domain."
* sedrubal: "Donated into the Public Domain. Whenever this project gets a 'real' license, I'd prefer a GPL"
