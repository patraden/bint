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
       assert type(other) in (int, bint)
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
        Auxilary addition method.
        Algorythm mimics half-adder circuit.
        Algorythm relies on assumption that python always interprets integers as 2’s compliment with binarywise operations.
        s var represents sum output.
        c var represents carry output.
        bitmask var requires to treat situations with "travelling" bit in carry variable.
        """

        max_bit_pos = max(self.bit_length(), other.bit_length()) + 1

        bitmask = -1 << max_bit_pos
        _bitmask = ~bitmask

        # main algorythm for half-adder circuit
        c,s = (self & other) << 1, self ^ other
        while c and c & _bitmask:
            c,s = (s & c) << 1, s ^ c

        # exception check for remaining bit in carry variable
        if c & bitmask:

            c = c >> max_bit_pos
            shifts = 0
            # finding remaining bit position and capture count of shifts
            while c != 1:
                c = c >> 1
                shifts += 1

            # changing bitmask to apply to left bits remainder of sum output
            bitmask = bitmask << shifts
            # esnuring left bits remainder in sum output
            if s >> (max_bit_pos + shifts) == -1:
                s = s ^ bitmask
            else:
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
    n = 45455
    nb = bint(n)
    t0= time.perf_counter()
    print(nsqr(n))
    t1 = time.perf_counter()
    print("Time elapsed: ", t1 - t0) # CPU seconds elapsed (floating point)
    t0= time.perf_counter()
    print(nsqr(nb))
    t1 = time.perf_counter()
    print("Time elapsed: ", t1 - t0) # CPU seconds elapsed (floating point)

    a = 3721687328139138019310370127321037120371203710720371203710739021792103710923710293792173901730913709209319371377472645653652364562546546532764527542754754265454272387627816372637136821763187361287361278361873617836872163827163781236817263821736217361783612876816312132786318631863123131231231313123131313213131312313131313123178
    b = -321691372813321803721072303710730192739273913921730137207310973283183232131312321213213211232131313231321321313123123123132313123131213132331313232213312784273478923748927489374982846296437964289463289648296493264274629846239469264926394629463984628964983264982694862398462986498326489264982364926498236439826983624926946239649286984628946928649826489326498264928364928643928649264982649264928648264982649862946928468246826492431231287897870870
    ab=bint(a)
    bb=bint(b)

    t0= time.perf_counter()
    print(a+b)
    t1 = time.perf_counter()
    print("Time elapsed: ", t1 - t0) # CPU seconds elapsed (floating point)

    t0= time.perf_counter()
    print(ab+bb)
    t1 = time.perf_counter()
    print("Time elapsed: ", t1 - t0) # CPU seconds elapsed (floating point)
