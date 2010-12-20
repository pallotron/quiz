#!/usr/bin/python

import unittest

rom2nums = { 'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1 }
rom_order = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
 
def roman2dec(rom_num=''):
    dec_num = 0
    prev_value = 0

    for rom_char in rom_num:

        rom_value = rom2nums[rom_char.upper()]

        # this is the case of IX, IV and so on 
        if prev_value and rom_value > prev_value:
            # remove the previous value and add the correct one
            dec_num -= prev_value
            dec_num += rom_value - prev_value
        else: # just add it
            dec_num += rom_value

        prev_value = rom_value


    # self test before returning
    rom_compare = rom_num.upper()
    rom_res = dec2roman(dec_num)
#    print "ROM %s NUM %d RES %s" % (rom_compare, dec_num, rom_res)
    if dec2roman(dec_num) != rom_compare:
        raise ValueError

    return dec_num
 
def dec2roman(num=0):
    if num <= 0:
        raise ValueError

    rom_num = ''

    # step 1: convert to roman chars
    for rom_char in rom_order:
        rom_value = rom2nums[rom_char]
        # std sub
        while num >= rom_value:
            rom_num = rom_num + rom_char
            num -= rom_value

        if rom_char == 'I':
            continue

        if rom_char == 'V':
            next_step = 1
        else:
            next_step = 2

        next_char = rom_order[rom_order.index(rom_char)+next_step]
        next_value = rom2nums[next_char]
        next_cmp = rom_value - next_value
        while num >= next_cmp:
            rom_num = rom_num + next_char + rom_char
            num -= next_cmp
        
    return rom_num
 
class RomanTests(unittest.TestCase):
 
    def testSimple(self):
        self.assertEqual(roman2dec('XXIV'), 24)
        self.assertEqual(roman2dec('mcmxcix'), 1999)
        self.assertEqual(dec2roman(13), 'XIII')
        self.assertEqual(dec2roman(78), 'LXXVIII')
 
    def testInvalid(self):
        self.assertRaises(ValueError, roman2dec, 'IIII')
        self.assertRaises(ValueError, roman2dec, 'VX')
        self.assertRaises(ValueError, roman2dec, 'VV')
        self.assertRaises(ValueError, roman2dec, 'IC')
        self.assertRaises(ValueError, dec2roman, -1)
 
    def testExhaustive(self):
        for i in range(1, 4000):
            self.assertEqual(roman2dec(dec2roman(i)), i)
 
if __name__ == '__main__':
    unittest.main()
