#!/usr/bin/env python
# -*- coding: utf-8 -*-

# OpenWasteTrace
# Copyright (C) 2011 Paolo Melchiorre <paolo.melchiorre@madec.it>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
This example shows how to getting an Sede object.
"""

import logging
from example_config import CONFIG_OBJ
from openwastetracelib.services.anagrafiche_service import GettingSedeRequest

# Set this to the INFO level to see the response from Sistri printed in stdout.
logging.basicConfig(level=logging.INFO)

# We're using the FedexConfig object from example_config.py in this dir.
sede = GettingSedeRequest(CONFIG_OBJ)
sede.identity = "test"
sede.idSIS = "00000000000"

# Fires off the request, sets the 'response' attribute on the object.
sede.send_request()

# See the response printed out.
print sede.response
