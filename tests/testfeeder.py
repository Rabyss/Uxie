#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This file is part of Uxie.

Uxie - Pokemon Showdown's usage stats database builder
Copyright (C) 2016 Kewin Dousse (Protectator)

Licensed under the MIT License. See file LICENSE in the project root for license information.
"""
import os
import unittest
from src.feeder import Feeder

class FeederTest(unittest.TestCase):
    def test_feed(self):
        feeder = Feeder('tests' + os.sep + 'textfiles')
        feeder.feedAll('mysql', 'localhost', 'uxie', 'uxie', 'uxie')
