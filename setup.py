#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import setuptools

# https://towardsdatascience.com/create-your-custom-python-package-that-you-can-pip-install-from-your-git-repository-f90465867893

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='micrOSDevToolKit',
    version='0.1.0',
    author='Marcell Ban',
    author_email='miros.framework@gmail.com',
    description='Development environment for micrOS (micropython based IoT solution)',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/BxNxM/micrOS',
    project_urls={
        "Bug Tracker": "https://github.com/BxNxM/micrOS/issues"
    },
    license='MIT',
    packages=setuptools.find_packages(),
    install_requires=['adafruit-ampy', 'esptool', 'ipaddress', 'mpy-cross', 'netaddr',
                      'netifaces', 'pylint', 'PyQt5', 'pyserial', 'resources'],
    scripts=['devToolKit.py'],
    include_package_data=True,
    use_scm_version=True,
    setup_requires=['setuptools_scm']
)