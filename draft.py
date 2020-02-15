class c_base:
    """2+ digits base class for longnumber
    which includes predefined 2-36
    characters classic alphabets
    and custom alphabet as provided by user"""
    i_alphabet=[]
    i_base=0
    index=0
    register=False
    sum_table=[]
    message=''
    def __user_input_handle__(self,m):
        user_alphabet=list(m)
        tmp_alphabet=[]
        for x in user_alphabet:
            if x not in tmp_alphabet:
                tmp_alphabet.append(x)
        tmp_alphabet.sort()
        self.i_base=len(tmp_alphabet)
        self.i_alphabet=tmp_alphabet
        self.message='Seems user provided base='+ str(self.i_base)+' and alphabet=' + ''.join(self.i_alphabet)

    def __init__(self,n=10):
        if type(n)==int:
            if n not in range(2,37):
                self.i_alphabet=[]
                self.i_base=0
                self.message='base value is out of [2,36] range for pre-defined alphabets'
            else:
                if n<=10:
                    self.i_alphabet=list(map(chr,[*range(ord('0'),ord('0')+n)]))
                else:
                    self.i_alphabet=list(map(chr,[*range(ord('0'),ord('0')+10),*range(ord('a'),ord('a')+n-10)]))
                self.i_base=n
                self.message='base='+ str(self.i_base)+' alphabet=' + ''.join(self.i_alphabet)
        else:
            try:
                self.__user_input_handle__(n)
            except TypeError:
                self.__user_input_handle__(str(n))

    def __counter__(self, direction:bool=True):
        if direction:
            if self.index==self.i_base-1:
                self.index=0
                self.register=True
            else:
                self.index=self.index+1
        else:
            if self.index==0:
                self.index=self.i_base-1
                self.register=True
            else:
                self.index=self.index-1

    def __sum_table_init__(self):
        self.sum_table.append((self.register,self.index))
        for i in range(1,2*self.i_base-1):
            self.__counter__()
            self.sum_table.append((self.register,self.index))
        self.__index_drop__()

    def __attr_drop__(self):
        import datetime
        self.index=0
        self.register=False
        self.sum_table=[]
        self.message='attributes last dropped @' + str(datetime.datetime.now())

class c_longnumbers():
    float_bytes=5

    def __input_number_handle__(self,input_number):
        import re

        input_type=type(input_number)

        if input_type==int:
            pattern=re.compile('[0-9]+')
            result = pattern.match(str(input_number))
            if result:
                if input_number<0:
                    input_number=abs(input_number)
                    self.value[self.float_bytes+1]=1

                self.value.extend([int(x) for x in reversed(str(input_number))])
                self.i_base=10
            else:
                self.value=[] #надо подумать!

        elif input_type==float:
##            pattern=re.compile(r'[0-9]*[.]?[0-9]*[e]?[+|-]?[0-9]*')
##            result = pattern.match(str(input_number))
##            print(result.group())
            print(input_number)
            print(str(input_number))
            print(re.sub(r'[.]','' , str(input_number)))


        elif input_type==bool:
            input_number=str(input_number)
            print('bool')
        elif input_type==str:
            input_number=str(input_number)
            print('str!')
        else:
            input_number=str(input_number)
            print('unknown input')

    def __init__(self,input_number=0,base=10):
        self.value=[]
        for i in range (self.float_bytes+2):
            self.value.append(0)

        if input_number!=0:
            self.__input_number_handle__(input_number)
        else:
            print('ZEERO!!')
