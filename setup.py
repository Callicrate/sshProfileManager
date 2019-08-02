#!/usr/bin/env python
from distutils.core import setup
import setuptools

setup(name='ssh-profile-manager',
      version='1.0.0',
      description='Manage multiple profiles under ~/.ssh/config.d',
      author='Joel Callicrate',
      author_email='joel.callicrate@gmail.com',
      packages=['sshProfileManager.sshProfileManager'],
      entry_points={
            'console_scripts': [
                  'ssh-profile-manager = sshProfileManager.__main__:main',
            ]
      },
      classifiers=[
                          "Programming Language :: Python :: 3",
                          "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
                          "Operating System :: OS Independent",
                    ]
      )