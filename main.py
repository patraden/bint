"""
Experimental custom int class·to·simulate·CPU arithmetics on fixed point numbers (+-*/).
Main·purpose·is·to·learn·and·practice·OOP·in·Python.

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
>>> a = bint(-5450)
>>> b= bint(5)
>>> print(a+b)
-5445
"""

class bint(int):
    """Custom int class.A child of build-in int class"""

    def __new__(value, *args, **kwargs):
        return int.__new__(value,*args, **kwargs)

    def __init__(self, *args, **kwargs):
        super().__init__()
        self.name = None

    def __add__(self, other):
       assert type(other) in (int, bint)
       return self._add(other)

    def _is_negative(self):
        """Aux method returning sign bit value"""
        return self >> self.bit_length()

    def __abs__(self):
        if self._is_negative():
            return bint(~self) + 1
        return self

    def _add(self, other):
        """
        Auxilary addition method.
        Algorythm mimics half-adder circuit of CPU.
        Algorythm relies on assumption that python always interprets integers as 2’s compliment with binarywise operations.
        "s" var represents sum output.
        "c" var represents carry output.
        "bitmask" var is required to handle "travellingi bit" situations.
        "travelling bit" situation happens in main algorythm when "c" has single bit remaining in certain position.
        While "s" left remainder (to the same position) has only bits ("s" is negative).
        In this case remaining bit in "c" keeps travelling left through alrorythm and loop does not exit.
        """

        max_bit_pos = max(self.bit_length(), other.bit_length()) + 1
        bitmask = -1 << max_bit_pos
        _bitmask = ~bitmask

        # Main algorythm for half-adder circuit
        c,s = (self & other) << 1, self ^ other
        while c and c & _bitmask:
            c,s = (s & c) << 1, s ^ c

        # Exception check for "travelling bit"
        if c & bitmask:

            c = c >> max_bit_pos
            shifts = 0
            # Finding remaining bit position and capture count of shifts
            while c != 1:
                c = c >> 1
                shifts += 1

            # Adjusting bitmask to zero left bits remainder of sum
            bitmask = bitmask << shifts
            # Esnure left bits remainder in sum has expected structure
            if s >> (max_bit_pos + shifts) == -1:
                s = s ^ bitmask
            else:
            # In theory any different sum remainder structure is not possible
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

    a = 3721687328139138019310370199318290839184738738921782983171312393890281901289381098309128301983092183910283902132197301237190283918129832190382190381209310293219032190321903712097310273107321097310973091730917309173901730917093270917309217321903721093721907301293721093710973021973109732109731092371209371209371027310730912371093710937120937210937120937210937102973190371209371029732107310273102371023710273017397029370173012932811023893812903820913891028301923821903821093812932109371023721073012370123710923710937129037012937012937210973109273712037210937137103710371209371937210937102371209371037012937109273019273091273091730912739012739017309173091730912730917310927317037102372130927321037120371203710720371203710739021792103710923710293792173901730913709209319371377472645653652364562546546532764527542754754265454272387627816372637136821763187361287361278361873617836872163827163781236817263821736217361783612876816312132786318631863123131231231313123131313213131312313131313123178
    b = -32169137281332180372107230371073019273927391392173013720731097328318323213131232121321321123213131323132132131312312312313231312313121313233131323221331278427347892374892748937498284629643796428946328964829649326427462984623946926492639462946398462896498326498269486239846298649832648926498236492649823891830918372817389173829739821832193926966666666666666666666666666666666666666666666666666666666666666666666666666666666378217307309132197389173910731207312093719372903701973092173109731023721097310730921730197302197309217029137019730917230937210937210937109372103710937109370123721390730917309127302173017321097310973019731073102973091273017309127310927301937109732190730192730112309170137310316666666666666666666666666666666666666888888888888888888888888888888888888888888888888888888888888888838983128963921631236439826983624926946239649286984628946928649826489326498264928364928643928649264982649264928648264982649862946928468246826492431231287897870870
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
