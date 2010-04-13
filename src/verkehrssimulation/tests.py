#! /usr/bin/python

"""
Tests.
"""

import unittest, doctest

def test_suite():
    flags = doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS
    return unittest.TestSuite((
                doctest.DocFileSuite('README.txt', optionflags=flags),
            ))

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
