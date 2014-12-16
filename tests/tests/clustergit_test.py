from tools import same

from cStringIO import StringIO
import sys
import tempfile

import clustergit

class TestClustergit:

    def test_check_no_repo(self):
        old_stdout = sys.stdout
        old_stderr = sys.stderr
        sys.stdout = mystdout = StringIO()
        sys.stderr = mystderr = StringIO()

        clustergit.main([])

        actual_out = mystdout.getvalue()
        expected_out = """Starting git status...
Scanning sub directories of .

"""
        actual_err = mystderr.getvalue()
        expected_err = """Error: None of those sub directories had a .git file.
"""
        same("stdout should be alright", expected_out, actual_out)
        same("stderr should be alright", expected_err, actual_err)

        sys.stdout = old_stdout
        sys.stderr = old_stderr



    def test_check_fresh_repo(self):
        dirpath = tempfile.mkdtemp()
        print "working in %s" % (dirpath)
        clustergit.run('cd "%s"; mkdir mygit; cd mygit; git init' % (dirpath), clustergit.read_arguments(['-v']))

        old_stdout = sys.stdout
        old_stderr = sys.stderr
        sys.stdout = mystdout = StringIO()
        sys.stderr = mystderr = StringIO()

        clustergit.main(['-d', dirpath, '--no-color', '--align=0'])

        actual_out = mystdout.getvalue()
        expected_out = """Starting git status...
Scanning sub directories of %s
%s/mygit: Changes
Done
""" % (dirpath, dirpath)
        actual_err = mystderr.getvalue()
        expected_err = """"""
        same("stdout should be alright", expected_out, actual_out)
        same("stderr should be alright", expected_err, actual_err)

        sys.stdout = old_stdout
        sys.stderr = old_stderr



    def test_excluded(self):
        dirpath = tempfile.mkdtemp()
        print "working in %s" % (dirpath)
        out = clustergit.run(
            'cd "%s";' % (dirpath)
            + 'mkdir notarepo repo1 repo2 target;'
            + 'cd repo1; git init; cd ..;'
            + 'cd repo2; git init; cd ..;'
            + 'tree -A', # show structure in error messages
            clustergit.read_arguments(['-v'])
        )
        print out

        old_stdout = sys.stdout
        old_stderr = sys.stderr
        sys.stdout = mystdout = StringIO()
        sys.stderr = mystderr = StringIO()

        clustergit.main(['-d', dirpath, '--no-color', '--align=0', '--warn-unversioned', '--exclude=target'])

        actual_out = mystdout.getvalue()
        expected_out = """Starting git status...
Scanning sub directories of {0}
{0}/notarepo: Not a GIT repository
{0}/repo1: Changes
{0}/repo2: Changes
Done
""".format(dirpath)
        actual_err = mystderr.getvalue()
        expected_err = ''
        same("stdout should exclude target", expected_out, actual_out)
        same("stderr should be empty", expected_err, actual_err)

        sys.stdout = old_stdout
        sys.stderr = old_stderr
