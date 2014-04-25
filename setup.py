from distutils.core import setup

from pluplusch import __version__

setup(name='pluplusch',
      author='Thomas Levine',
      author_email='_@thomaslevine.com',
      description='Download data from OpenDataSoft open data platforms.',
      url='https://github.com/tlevine/pluplusch',
      packages=['pluplusch'],
      install_requires = ['picklecache'],
      tests_require = ['nose'],
      version=__version__,
      license='AGPL',
)
