"""
Custom·float·class·to·simulate·basic·arithmetic·operations
 (addition,·subtraction,·multiplication,·division).
Main·idea·is·to·learn·and··practice·OOP·in·Python.

Test cases for module.
>>> a = FixedPointNum(5)
>>> print(a)
00000000000000000000000000000101
>>> a = FixedPointNum(-5)
>>> print(a)
10000000000000000000000000000101
>>> a = FixedPointNum(0)
>>> print(a)
00000000000000000000000000000000
"""

FIXED_POINT_NUM_BITS = 32

class FixedPointNum(object):
    """
    Fixed point number class storing number as binary in python list.
    """

    def __init__(self, n):
        """
        Initiate class example.
        """
        assert type(n) is int
        if n >= 0:
            self.direct = list(map(int, format(n, '0{}b'.format(FIXED_POINT_NUM_BITS))))
        else:
            self.direct = [1] + list(map(int, format(n, '0{}b'.format(FIXED_POINT_NUM_BITS))[1:]))
        self.reversed = None
        self.extended = None

    def reverse(self):
        """
        Calculates reverse form of fixed point number.
        """
        self.reversed = [not(x) for x in self.direct[1:]] if self.direct[0] else self.direct

    def extend(self):
        """
        Calculates reverse form of fixed point number.
        """
        pass

    def __str__(self):
        return ''.join(str(x) for x in self.direct)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
