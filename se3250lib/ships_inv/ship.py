"""
se3250lib Version 0.1.0

Copyright (c) 2024 FEONA MAE L. JOHNSON

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

class Ship:
    ''' A ship carrying anti-ship cruise missiles.

    Attributes:
        * type (str): the type of ship, for labeling purposes only.
        * op (int): the number of anti-ship cruise missiles the ship can fire in one salvo.
        * dp (int): the number of SAM the ship can fire in one salvo against incoming missiles.
        * sp (float): initial staying power in missile hits.
        * hp (float): hit points remaining.
        * status (fraction): fraction of its staying power remaining. 1 is intact, 0 is OOA.
    '''

    def __init__(self, type, op, dp, sp):
        self.type = type
        self.op = op
        self.dp = dp
        self.sp = sp
        self.hp = sp
        self.status = 1

    def damage(self, damage):
        ''' Lowers the ship's 'hp' attribute by the input amount.

        Args:
            * damage (float): points of damage to subtract. HP cannot go below 0.
        '''
        damage = min(damage, self.hp)
        damage = max(damage, 0)
        self.hp -= damage
        self.status = self.hp / self.sp

    def ascm_fire(self):
        ''' Returns cruise missile salvo size based on status.'''
        return self.op * self.status

    def sam_fire(self):
        ''' Returns SAM salvo size based on status.'''
        return self.dp * self.status

    def __str__(self):
        ''' String override. Returns ship type, status as percentage, OP, and DP.'''
        shipStatus = round(self.status * 100, 2)
        shipOp = round(self.ascm_fire(), 2)
        shipDp = round(self.sam_fire(), 2)
        shipString = "{} ({}%) OP: {} DP: {}\n".format(self.type, shipStatus, shipOp, shipDp)
        return shipString

# BLUFOR friendly
ship_inv = {
    "DDG_52": Ship(
        type="DDG_52",
        op=15,
        dp=10,
        sp=1.5
        ),
    "DDG_84": Ship(
        type="DDG_84",
        op=7,
        dp=13,
        sp=1.2
        ),
    "DDG_105": Ship(
        type="DDG_105",
        op=20,
        dp=4,
        sp=1.8
        ),
    # REDFOR hostile
    "DDG": Ship(
        type="DDG",
        op=9,
        dp=2,
        sp=1.3
        ),
    "FFC": Ship(
        type="FFC",
        op=4,
        dp=14,
        sp=1.6
        ),
    "FFG": Ship(
        type="FFG",
        op=10,
        dp=4,
        sp=1
        )
}

def get_ship_data(ship_type):
    return ship_inv.get(ship_type)

def list_all_ships():
    return list(ship_inv.keys())