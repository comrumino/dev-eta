import os
import sys

from setuptools import setup, find_packages

package_name = 'deveta'
description = 'A python library for the miscellaneous'
readme = open('man/README.rst').read()
requirements = []
long_description = open('man/README.rst').read()
package = __import__(package_name)

package_version = package.__version__

setup(name=package_name,
      version=package_version,
      author=package.__author__,
      author_email=package.__author_email__,
      url=package.__url__,
      description=description,
      long_description=long_description,
      packages=find_packages(),
      install_requires=requirements,
      license=package.__license__
)
