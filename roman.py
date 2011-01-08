
import unittest

# your global variables can go here, too ;)

def roman2dec(roman):
    assert isinstance(roman, str), 'Expected string argument'

    if roman == "":
        return 0

    result = 0
    # upping the string just in case
    # i still don't know how to to case insensitive regexps :P
    roman = roman.upper()

    import re
    # this char cannot be repeated more than 3 times
    for i in ('X', 'I', 'C', 'M'):
        if re.match(i+"{4}",roman):
            raise ValueError
    # this char cannot be repeated more than 2 times
    for i in ('V', 'L', 'D'):
        if re.match(i+"{2}",roman):
            raise ValueError

    # these combos are not allowed
    #if re.match("[LCDM]VX",roman):
    #    raise ValueError
    #if re.match("(VX|LC|DM|VL|VC|VD|XD|LD|VM|XM|XV|LM|I{2,3}VX)",roman):
    #    raise ValueError
    #if re.match("(IC|IL|ID|IM|I{2,}X|IXV|VI[XLCDM]|IV[XLCDM])",roman):
    #    raise ValueError

    I = roman.count('I')
    V = roman.count('V')
    X = roman.count('X')
    L = roman.count('L')
    C = roman.count('C')
    D = roman.count('D')
    M = roman.count('M')
    result = I+V*5+X*10+L*50+C*100+D*500+M*1000

    if  roman.count('IV') or roman.count('IX'):
        result -= 2
    # jesus, i see the pattern now!!! :D
    # after 3 glasses of good white wines
    # in vino veritas! :P
    if  roman.count('XL') or roman.count('XC'):
        result -= 20
    if  roman.count('CD') or roman.count('CM'):
        result -= 200

    if roman <> dec2roman(result): raise ValueError
    return result

def dec2roman(dec):
    assert isinstance(dec, int), 'Expected integer argument'

    if dec == 0:
        return ""

    if not (0 < dec < 4000): raise ValueError

    num = (1000,  900, 500, 400, 100, 90,  50, 40,  10,  9,  5,  4,   1)
    rom = ( 'M', 'CM', 'D','CD','C', 'XC','L','XL','X','IX','V','IV','I')

    result = ""
    for i in range(len(num)):
        count = int(dec / num[i])
        result += rom[i] * count
        dec  -= num[i] * count

    return result

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
        for i in range(4000):
            self.assertEqual(roman2dec(dec2roman(i)), i)

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
        for i in range(4000):
            self.assertEqual(roman2dec(dec2roman(i)), i)

    def testExhaustive2(self):
        letters = ('I', 'V', 'X', 'L', 'C', 'D', 'M')
        first_example = None
        count = 0
        for i in xrange(8*8*8*8*8):
            rom = ''
            while True:             # do { ... } while i>0
                rom += letters[i % 7]
                i /= 7
                if i<=0: break

            try:
                dec = roman2dec(rom)
                roman = dec2roman(dec)
                if rom <> roman:
                    if first_example is None:
                        first_example = '%s != %s (decimal %d)' % (rom, roman, dec)
                    count += 1
            except ValueError, e:
                pass

        self.assertEqual(count, 0, 'Accepted %d invalid roman numbers (e.g. %s)' % (count, first_example))

if __name__ == '__main__':
    unittest.main()

