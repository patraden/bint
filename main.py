"""
Experimental custom int class·to·simulate·CPU arithmetics on fixed point numbers (+-*/).
Main·purpose·is·to·learn·and·practice·OOP·in·Python.

Test cases for module.

>>> a = -2321531871332173218312021309138193213031225
>>> b = 222732132132131231231211231332131
>>> ab = bint(a)
>>> bb = bint(b)
>>> print(ab+bb-a-b)
0
>>> print(ab-bb-a+b)
0
>>> b = -12167319231
>>> bb = bint(b)
>>> print(abs(bb)-abs(b))
0
>>> a = 13219316732197361931293612831283912389138172987391836
>>> b = -183213187382173102312322817382781378217310273292379103701293729017
>>> ab = bint(a)
>>> bb = bint(b)
>>> print(a*b-ab*bb)
0
"""

class bint(int):
    """Custom class, a child of int"""

    def __new__(value, *args, **kwargs):
        return int.__new__(value,*args, **kwargs)

    def __init__(self, *args, **kwargs):
        super().__init__()
        self.name = None

    def __add__(self, other):
       assert type(other) in (int, bint)
       return bint(self._add(other))

    def __mul__(self, other):
       assert type(other) in (int, bint)
       return bint(self._mul(other))

    def __neg__(self):
        return ~self + 1

    def __sub__(self, other):
        return self + (-other)

    def __abs__(self):
        if self >> self.bit_length():
            return ~self + 1
        return self

    def _mul(self, other):
        """
        Auxilary multiplication method.
        Algorythm mimics multiplier circuit of CPU.
        Algorythm relies on assumption that python always interprets integers as 2’s compliment with binarywise operations.
        "muld" var represents multiplicand.
        "mulr" var represents multiplier.
        """

        s_bitsize = self.bit_length()
        o_bitsize = other.bit_length()
        s_sign = self >> s_bitsize
        o_sign = other >> o_bitsize
        p_sign = s_sign ^ o_sign

        # get multiplier with shortest length to minimze additions
        if s_bitsize < o_bitsize:
            muld = -other if o_sign else other
            mulr = -self if s_sign else self
            mulr_bitsize = s_bitsize
        else:
            muld = -self if s_sign else self
            mulr = -other if o_sign else other
            mulr_bitsize = o_bitsize

        # main algorythm
        prod = 0
        mulr_bit = 0
        while mulr_bit < mulr_bitsize:
            mulr_bit_val = mulr & (1 << mulr_bit)
            if mulr_bit_val:
                prod += muld << mulr_bit
            mulr_bit += 1

        if p_sign:
            return -prod
        return prod

    def _add(self, other):
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

        max_bit_pos = max(self.bit_length(), other.bit_length()) + 1
        bitmask = -1 << max_bit_pos
        _bitmask = ~bitmask

        # Main algorythm for half-adder circuit
        c,s = (self & other) << 1, self ^ other
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
    import doctest
    doctest.testmod(verbose=False)

# performance comparison
    import time
    n = 5698
    nb = bint(n)
    t0= time.perf_counter()
    c = fact(n)
#    c = nsqr(n)
    t1 = time.perf_counter()
    print("Time elapsed: ", t1 - t0)
    t0= time.perf_counter()
    d = fact(nb)
#    d = nsqr(nb)
    t1 = time.perf_counter()
    print("Time elapsed: ", t1 - t0)
