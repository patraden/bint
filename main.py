"""
Experimental custom int class·to·simulate·CPU arithmetics on fixed point numbers (+-*/).
Main·purpose·is·to·learn·and·practice·OOP·in·Python.

Test cases for module.

>>> a = -2321531871332173218312021309138193213031225
>>> b = -222732132132131231231211231332131
>>> ab = bint(a)
>>> bb = bint(b)
>>> print(b.bit_length() - bb.bit_length())
0
>>> print(ab+bb-a-b)
0
>>> print(ab-bb-a+b)
0
>>> b = -12167319231
>>> bb = bint(b)
>>> print(abs(bb)-abs(b))
0
>>> a = 13219316732197361931293612831283912389138172987391836
>>> b = 3102312322817382781378217310273292379103701293729017
>>> ab = bint(a)
>>> bb = bint(b)
>>> print(a*b-ab*bb)
0
>>> print(ab==bb)
False
>>> ab = bint(89)
>>> bb = bint(89)
>>> print(ab==bb)
True
>>> ab = bint(809)
>>> bb = bint(89)
>>> print(ab!=bb)
True
>>> a = 136321763217321721219316732197361931293612831283912389138172987391836
>>> b = 3102312322817382781378217310273292379103701293729017
>>> print(a*b - bint(0)._mul_karatsuba(a,b))
0
"""

LONG_INT_MIN_BIT_LENGTH = 2000

class bint(int):
    """Custom class, a child of int"""

    def __new__(value, *args, **kwargs):
        return int.__new__(value,*args, **kwargs)

    def __init__(self, *args, **kwargs):
        super().__init__()
        self.msg = None

    def __eq__(self, other):
        return not(self ^ other)

    def __neq__(self, other):
        return self ^ other

    def __neg__(self):
        return ~self + 1

    def __abs__(self):
        if self >> self.bit_length():
            return ~self + 1
        return self

    def __sub__(self, other):
        assert type(other) in (int, bint)
        return bint(self._sub(self, other))

    def _sub(self, _self, _other):
        """
        Auxilary substraction method.
        """
        return self._add(_self, -_other)

    def __add__(self, other):
        assert type(other) in (int, bint)
        return bint(self._add(self, other))

    def _add(self, a, b):
        """
        Auxilary addition method.
        Algorythm mimics half-adder circuit of CPU.
        Algorythm relies on assumption that python always interprets integers as 2’s compliment with binarywise operations.
        "s" var represents sum output.
        "c" var represents carry output.
        "bitmask" var is required to handle "travellingi 1-bit" situations.
        "travelling bit" situation happens in main algorythm when "c" has single 1-bit remaining in certain position.
        While "s" left remainder (to the same position) has only 1-bits ("s" is negative).
        In this case remaining 1-bit in "c" keeps travelling left through alrorythm and loop does not exit.
        """

        max_bit_pos = max(a.bit_length(), b.bit_length()) + 1
        bitmask = -1 << max_bit_pos
        _bitmask = ~bitmask

        # Main algorythm for half-adder circuit
        c,s = (a & b) << 1, a ^ b
        while c and c & _bitmask:
            c,s = (s & c) << 1, s ^ c

        # Exception check for "travelling 1-bit"
        if c & bitmask:

            c = c >> max_bit_pos
            shifts = 0
            # Finding remaining 1-bit position and capture count of shifts
            while c != 1:
                c = c >> 1
                shifts += 1

            # Adjusting bitmask to zero left 1-bits only remainder of sum
            bitmask = bitmask << shifts
            # Esnure left bits remainder in sum has expected structure
            if s >> (max_bit_pos + shifts) == -1:
                s = s ^ bitmask
            else:
            # In theory any different sum remainder structure is not possible
                raise Exception ('Impossible case!')
        return s

    def __mul__(self, other):
        """
        Main multiplication method.
        """
        assert type(other) in (int, bint)
        s_bits = self.bit_length()
        o_bits = other.bit_length()
        s_sign = self >> s_bits
        o_sign = other >> o_bits
        sign = s_sign ^ o_sign

        if sign:

#            return bint(-self._mul(abs(self), abs(other)))
#        return bint(self._mul(abs(self), abs(other)))

            return bint(-self._mul_karatsuba(abs(self), abs(other)))
        return bint(self._mul_karatsuba(abs(self), abs(other)))

    def _mul(self, a, b):
        """
        Auxilary multiplication method.
        Algorythm mimics multiplier circuit of CPU.
        Inputs limitations: a, b >= 0.
        """

        n = a.bit_length()
        m = b.bit_length()

        # get multiplier with shortest length to minimze additions
        if m > n:
            a,b = b,a

        prod = 0
        b_bit = 0
        while b >> b_bit != 0:
            b_bit_val = b & (1 << b_bit)
            if b_bit_val:
#                prod = self._add(prod, a << b_bit)
                prod += a << b_bit
            b_bit += 1
        return prod

    def _mul_karatsuba(self, a, b):
        """
        Auxilary method for multiplication of long integers.
        Uses reccursive Karatsuba algorythm.
        Inputs limitations: a, b >= 0.
        LONG_INT_MIN_BIT_LENGTH triggers Karatsuba algo versus simple multiplication.
        """

        n = a.bit_length()
        m = b.bit_length()

        # reccursion condition
        if n <= LONG_INT_MIN_BIT_LENGTH or m <= LONG_INT_MIN_BIT_LENGTH:
            return self._mul(a, b)

        shifts = 0

        if m <= n:
            # check if m is add, if true, make it even
            if m & 1 == 1:
                shifts = 1
                b = b << shifts
                m += 1
            k = m >> 1
        else:
            # check if n is add, if true, make it even
            if n & 1 == 1:
                shifts = 1
                a = a << shifts
                n += 1
            k = n >> 1

        terms_mask = ~(-1 << k) # 0..01..1

        # input numbers split polynomail terms
        a0 = a & terms_mask
        a1 = a >> k
        b0 =b & terms_mask
        b1 =b >> k
#        sum_a0a1 = self._add(a0, a1)
#        sum_b0b1 = self._add(b0, b1)
        sum_a0a1 = a0 + a1
        sum_b0b1 = b0 + b1
        prd_a0b0 = self._mul_karatsuba(a0, b0)
        prd_a1b1 = self._mul_karatsuba(a1, b1)

        # resulted number polynomial terms
        lo = prd_a0b0
        hi = prd_a1b1
        mi = self._mul_karatsuba(sum_a0a1, sum_b0b1)
#        mi = self._add(mi, -prd_a0b0)
#        mi = self._add(mi, -prd_a1b1)
        mi = mi - prd_a0b0
        mi = mi - prd_a1b1

        # shifting resulted terms
#        lo, mi = lo & terms_mask, self._add(mi, lo >> k)
#        mi, hi = mi & terms_mask, self._add(hi, mi >> k)
        lo, mi = lo & terms_mask, mi + (lo >> k)
        mi, hi = mi & terms_mask, hi + (mi >> k)

        return  (lo | mi << k | hi << k << k) >> shifts


# test functions

def nsqr (n):
    result = n
    for i in range(abs(n)-1):
        result = n + result
    return result

def fact(n):
    if type(n) == bint:
        result = bint(1)
    else:
        result = 1
    for i in range(1,n+1,1):
        result = result * i
    return result

if __name__ == "__main__":
#    import doctest
#    doctest.testmod(verbose=False)

    import random
    a = random.getrandbits(499000)
    b = random.getrandbits(599000)

# performance comparison
    import time
    t0= time.perf_counter()
    c = a*b
    t1 = time.perf_counter()
    print("Time elapsed: ", t1 - t0)

    t0= time.perf_counter()
    cb = bint(a)*bint(b)
    t1 = time.perf_counter()
    print("Time elapsed: ", t1 - t0)
    print("Difference", c - cb)
