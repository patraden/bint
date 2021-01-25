"""
Custom·float·class·to·simulate·basic·arithmetic·operations
 (addition,·subtraction,·multiplication,·division).
Main·idea·is·to·learn·and··practice·OOP·in·Python.

Test cases for module.
>>> a = bint(25)
>>> print(a)
25|11001
>>> b=a+46
>>> print(b)
71|1000111
>>> b=bint(-12167319231)
>>> print(abs(b))
12167319231|1011010101001110101000111010111111
>>> a = bint(-50)
>>> b= bint(-50)
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

    def __str__(self):
        return super().__str__() + '|' + format(self, 'b')

    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        return self._add(other)

    def _is_negative(self):
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
        r,s = (self & other) << 1, self ^ other

        while r and r & ~r_mask:
            r,s = (s & r) << 1, s ^ r

        if r & r_mask: # checking  if register left (vs max bit size) remainder has any bits
            r = r >> max_bit
            r_shifts = 0

            while r !=1: #finding remaining bit in register
                r = r >> 1
                r_shift += 1

            r_mask = r_mask << r_shifts
            if s >> (max_bit + r_shifts)== -1: # esnuring left sum remainder contains bits only, no zeroes
                s = s ^ r_mask # changing all left sum remainder bits to zeroes
            else:
                raise Exception ('Impossible case!')
        return bint(s)

if __name__ == "__main__":
    import doctest
    a = bint(-11)
    b= bint(3)
    print(a+b)
#    doctest.testmod(verbose=True)
