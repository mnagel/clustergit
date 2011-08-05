h1. clustergit

clustergit is a renamed and slightly improved version of Mike Pearce's
show_status.

h2. Installation

Either copy the script as indicated below or have a look at the Debian
packaging at: https://github.com/mnagel/clustergit-packaging

h2. Credits

show_status by Mike Pearce: https://github.com/MikePearce/Git-Status
patches to show_status by ilor: https://github.com/ilor/Git-Status

h1. show_status by Mike Pearce

Ever wanted to get the status of repos in multiple sub directories?
Yeah, me too. So I knocked this up.

h2. Installation

Copy the file to /usr/bin
<pre><code> cp show_status /usr/bin
</code></pre>

Give it execute permissions
<pre><code> chmod +x /usr/bin/show_status
</code></pre>

h2. Usage

Usage: show_status [options]

Show Status is awesome. If you tell it a directory to look in, it'll scan
through all the sub dirs looking for a .git directory. When it finds one it'll
look to see if there are any changes and let you know. It can also push and
pull to/from a remote location (like github.com) (but only if there are no
changes.)
Contact mike@mikepearce.net for any support.

h2. Options

<pre><code>
  -h, --help            Show this help message and exit
  -d DIR, --dir=DIRN    The directory to parse sub dirs from
  -v, --verbose         Show the full detail of git status
  -r REM, --remote=REM  Pull/Push will work with this remote
  -p, --pull            Pull from the master (remotename:branchname)
  --push                Push to the master (remotename:branchname)
  ...                   There are more (not yet documented) options
</code></pre>

h2. Warranties/Guarantees

None, you're on your own.
If you'd like some help, mail me on mike@mikepearce.net
