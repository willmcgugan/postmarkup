"""BBCode to (X)HTML rendering engine

Converts BBCode (http://en.wikipedia.org/wiki/BBCode) in to HTML and
XHTML snippets. Always outputs valid XHTML, even from badly nested BBCode.
"""

VERSION = "1.2.0.a"

classifiers = """\
Development Status :: 5 - Production/Stable
Intended Audience :: Developers
Programming Language :: Python
Programming Language :: Python :: 2.5
Programming Language :: Python :: 2.6
Programming Language :: Python :: 2.7
Programming Language :: Python :: 3.0
Programming Language :: Python :: 3.1
Programming Language :: Python :: 3.2
License :: OSI Approved :: Python Software Foundation License
Operating System :: OS Independent
Topic :: Text Processing :: Markup
"""

from setuptools import setup
import sys

doclines = __doc__.split("\n")

extra = {}
if sys.version_info >= (3,):
    extra["use_2to3"] = True

setup( name='postmarkup',
       version = VERSION,
       author = 'Will McGugan',
       author_email = 'will@willmcgugan.com',
       license = "Python Software Foundation License",
       url = 'http://code.google.com/p/postmarkup/',
       download_url = 'http://code.google.com/p/postmarkup/downloads/list',
       platforms = ['any'],
       description = doclines[0],
       long_description = '\n'.join(doclines[2:]),
       #py_modules = ['postmarkup'],
       package_dir = {"": "src"},
       packages = ["postmarkup"],       
       classifiers = classifiers.splitlines(),       
       **extra
       )
