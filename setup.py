# -*- coding: utf-8 -*-

import os
import re

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup (
    name = 'pixaven',
    version = '1.0.0',
    description = 'Official Python integration for the Pixaven Image API',
    long_description = 'Pixaven is an enterprise-grade image processing SaaS running entirely on Apple® platform. Resize, scale, crop, mask, filter and enhance your images with blazing speed.',
    url = 'https://github.com/pixaven/pixaven-python',
    download_url = 'https://github.com/pixaven/pixaven-python/archive/1.0.0.tar.gz',
    author = 'Pixaven UG',
    author_email = 'support@pixaven.com',
    license = 'MIT',
    keywords = 'pixaven image processing resizing resizer cropping scaling masking watermarking filtering thumbnails pic picture photo face face detection visual watermark filter crop mask resize resizer thumbs thumbnail thumbnails jpg jpeg png gif svg bmp psd tiff',

    packages = [
        'pixaven'
    ],

    install_requires = [
        'requests'
    ],

    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities'
    ]
)