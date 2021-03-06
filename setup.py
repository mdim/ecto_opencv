#!/usr/bin/env python
from distutils.core import setup

setup(name='Ecto OpenCV',
      version='1.0.0',
      description='Ecto bindings for OpenCV',
      packages=['ecto_opencv', 'ecto_opencv.features2d'],
      package_dir={'':'python'}
)
