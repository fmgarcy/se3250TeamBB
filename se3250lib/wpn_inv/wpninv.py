"""
se3250lib Version 0.1.0

Copyright (c) 2024 FEONA MAE L. JOHNSON

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
class Missiles:
    ''' The specification of the missile systems carried by a group of ships.

    Attributes:
        * launch_reliability (fraction): fraction of cruise missiles that launch successfully.
        * ascm_to_hit (fraction): fraction of cruise missiles that hit, in the absence of defences.
        * sam_to_hit (fraction): fraction of SAM that successfully intercept incoming missiles.
    '''
    def __init__(self, launch_reliability = 1, ascm_to_hit = 1, sam_to_hit = 1):
        self.launch_reliability = launch_reliability
        self.ascm_to_hit = ascm_to_hit
        self.sam_to_hit = sam_to_hit

    def offensive_modifier(self):
        ''' Returns the fraction of missiles that launch AND hit.'''
        return self.launch_reliability * self.ascm_to_hit

wpn_inv = {
    #Friendly
    "AGM-114L": Missiles(
        launch_reliability = 0.8,
        ascm_to_hit = 0.55,
        sam_to_hit = 0.68,
        ),
    "AGM-84E": Missiles(
        launch_reliability = 0.8,
        ascm_to_hit = 0.55,
        sam_to_hit = 0.68,
        ),
    "BGM-109": Missiles(
        launch_reliability = 0.8,
        ascm_to_hit = 0.55,
        sam_to_hit = 0.68,
        ),
    "RIM-116": Missiles(
        launch_reliability = 0.5,
        ascm_to_hit = 0.88,
        sam_to_hit = 0.80,
        ),
    "RGM-84": Missiles(
        launch_reliability = 0.9,
        ascm_to_hit = 0.20,
        sam_to_hit = 0.68,
        ),
    "RGM-184A": Missiles(
        launch_reliability = 0.8,
        ascm_to_hit = 0.55,
        sam_to_hit = 0.68,
        ),
    "SM-3": Missiles(
        launch_reliability = 1.0,
        ascm_to_hit = 0.75,
        sam_to_hit = 0.68,
        ),
    #Hostile
    "FL-300N": Missiles(
        launch_reliability = 0.8,
        ascm_to_hit = 0.55,
        sam_to_hit = 0.68,
        ),
    "HQ-10": Missiles(
        launch_reliability = 0.8,
        ascm_to_hit = 0.55,
        sam_to_hit = 0.68,
        ),
    "HQ-16": Missiles(
        launch_reliability = 0.8,
        ascm_to_hit = 0.55,
        sam_to_hit = 0.68,
        ),
    "YJ-18": Missiles(
        launch_reliability = 0.8,
        ascm_to_hit = 0.55,
        sam_to_hit = 0.68,
        ),
    "YJ-12": Missiles(
        launch_reliability = 0.8,
        ascm_to_hit = 0.55,
        sam_to_hit = 0.68,
        ),
    "YJ-83": Missiles(
        launch_reliability = 0.8,
        ascm_to_hit = 0.55,
        sam_to_hit = 0.68,
        )
}

def get_wpn_data(wpn_type):
    return wpn_inv.get(wpn_type)

def list_all_weapons():
    return list(wpn_inv.keys())

def get_offensive_mod(wpn_type)
    weapon = wpn_inv.get(wpn_type)
    lr = weapon.launch_reliability
    ath = weapon.ascm_to_hit
    launch_hit_frac = lr*ath
    return launch_hit_frac