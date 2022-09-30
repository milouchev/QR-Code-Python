#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 10:43:30 2022

@author: milouchev
"""

# pip install pyqrcode
import pyqrcode
import png 

redirect = ('https://github.com/milouchev')

qr = pyqrcode.create(redirect, error='L', version=10, mode='binary')
qr.png("My Github.png", scale=8,)
qr.show()