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

        if self > 0 and other >0:
            return self._add(other)
        else:
            return

    def _is_negative(self):

        return self >> self.bit_length()

    def __abs__(self):

        if self._is_negative():
            return bint(~self) + 1
        return self

    def _add(self, other):
        """Auxilary addition"""

        assert type(other) in (int, bint)
        # r - register
        # s - bitwise temporary sum
        r,s = (self & other) << 1, self ^ other
        while r:
            r,s = (s & r) << 1, s ^ r
        return bint(s)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
