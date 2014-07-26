from tools import same

from cStringIO import StringIO
import sys

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
        import tempfile
        dirpath = tempfile.mkdtemp()
        print "working in %s" % (dirpath)
        clustergit.run('cd "%s"; mkdir mygit; cd mygit; git init' % (dirpath), clustergit.read_arguments(['-v']))

        old_stdout = sys.stdout
        old_stderr = sys.stderr
        sys.stdout = mystdout = StringIO()
        sys.stderr = mystderr = StringIO()

        clustergit.main(['-d', dirpath, '--no-color'])

        actual_out = mystdout.getvalue()
        expected_out = """Starting git status...
Scanning sub directories of %s
%s/mygit                    : Changes
Done
""" % (dirpath, dirpath)
        actual_err = mystderr.getvalue()
        expected_err = """"""
        same("stdout should be alright", expected_out, actual_out)
        same("stderr should be alright", expected_err, actual_err)

        sys.stdout = old_stdout
        sys.stderr = old_stderr
