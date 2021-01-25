"""
Custom·float·class·to·simulate·basic·arithmetic·operations
 (addition,·subtraction,·multiplication,·division).
Main·idea·is·to·learn·and··practice·OOP·in·Python.

Test cases for module.
>>> a = bint(25)
>>> print(a)
25
>>> b=a+46
>>> print(b)
71
>>> b=bint(-12167319231)
>>> print(abs(b))
12167319231
>>> a = bint(-50)
>>> b= bint(5)
>>> print(a+b)
-45
"""

class bint(int):
    """Custom int class with redefined basic operations"""

    def __new__(value, *args, **kwargs):
        return int.__new__(value,*args, **kwargs)

    def __init__(self, *args, **kwargs):
        super().__init__()
        self.name = None

    def __add__(self, other):
       return self._add(other)

    def _is_negative(self):
        """Aux method"""
        return self >> self.bit_length()

    def __abs__(self):
        if self._is_negative():
            return bint(~self) + 1
        return self

    def _add(self, other):
        """
        Auxilary addition method
        ***algorythm description***
        """
        assert type(other) in (int, bint)

        max_bit = max(self.bit_length(), other.bit_length()) + 1
        r_mask = -1 << max_bit # register size mask 1..10..0
        _r_mask = ~r_mask # inverted register size mask 0..01..1

        r,s = (self & other) << 1, self ^ other
        while r: # and r & _r_mask:
            r,s = (s & r) << 1, s ^ r

        if r & r_mask: # if register still has a bit remaining

            r = r >> max_bit
            r_shifts = 0
            while r != 1: # finding remaining bit position and capture to r_shifts
                r = r >> 1
                r_shifts += 1

            r_mask = r_mask << r_shifts # changing r_mask to apply to left bits remainder in s
            if s >> (max_bit + r_shifts) == -1: # esnuring left bits remainder in s
                s = s ^ r_mask # changing all left sum remainder bits to zeroes
            else:
                #in theory there should be a case with remaining bit in register and left zero remainder in s
                raise Exception ('Impossible case!')
        return bint(s)

def nsqr (n):
    result = n
    for i in range(abs(n)-1):
        result = n + result
    return result

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=False)
    import time
    n = -45455
    n1 = bint(n)
    t0= time.perf_counter()
    print(nsqr(n))
    t1 = time.perf_counter()
    print("Time elapsed: ", t1 - t0) # CPU seconds elapsed (floating point)
    t0= time.perf_counter()
    print(nsqr(n1))
    t1 = time.perf_counter()
    print("Time elapsed: ", t1 - t0) # CPU seconds elapsed (floating point)
