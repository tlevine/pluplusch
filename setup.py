from distutils.core import setup

from pluplusch import __version__

setup(name='pluplusch',
      author='Thomas Levine',
      author_email='_@thomaslevine.com',
      description='Big dada: Download data from lots of open data platforms.',
      url='https://github.com/tlevine/pluplusch',
      packages=['pluplusch'],
      install_requires = [
          'picklecache>=0.0.3',
          'requests>=2.2.1',
          'pickle_warehouse>=0.0.17'
      ],
      tests_require = ['nose'],
      version=__version__,
      license='AGPL',
)
