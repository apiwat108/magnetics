# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 16:30:09 2024

@author: Admin
"""

import freegs

from freegs.machine import Coil, Machine
from freegs.equilibrium import Equilibrium

coils = [("P1L", Coil(1.0, -1.1)),
         ("P1U", Coil(1.0, 1.1)),
         ("P2L", Coil(1.75, -0.6)),
         ("P2U", Coil(1.75, 0.6))]

