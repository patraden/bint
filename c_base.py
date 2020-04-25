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
 def __user_input_handle__(self,m):
  user_alphabet=list(m)
  tmp_alphabet=[]
  for x in user_alphabet:
   if x not in tmp_alphabet:
    tmp_alphabet.append(x)
  tmp_alphabet.sort()
  self.i_base=len(tmp_alphabet)
  self.i_alphabet=tmp_alphabet
 def __init__(self,n=10):
  print('I am here!')
  if type(n)==int:
   if n not in range(2,37):
    self.i_alphabet=[]
    self.i_base=0
   else:
    if n<=10:
     self.i_alphabet=list(map(chr,[*range(ord('0'),ord('0')+n)]))
    else:
     self.i_alphabet=list(map(chr,[*range(ord('0'),ord('0')+10),*range(ord('a'),ord('a')+n-10)]))
     self.i_base=n
  else:
   try:
    self.__user_input_handle__(n)
   except TypeError:
    self.__user_input_handle__(s)
