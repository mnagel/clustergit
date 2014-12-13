from nose.tools import *

def same(message, expected, actual):
    eq_(actual, expected, '%s. We expected [%s] but got [%s]' % (message, expected, actual))

def confirm(message, actual):
	eq_(message, True, actual)
