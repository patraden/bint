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
		self.message='Seems user provided base='+str(self.i_base)+'and alphabet='+''.join(self.i_alphabet)

	def __init__(self,n=10):
		if type(n)==int:
			if n not in range(2,37):
				self.i_alphabet=[]
				self.i_base=0
				self.message='base value is out of [2,36] range for pre-defined alphabets'
			else:
				if	n<=10:
					self.i_alphabet=list(map(chr,[*range(ord('0'),ord('0')+n)]))
				else:
					self.i_alphabet=list(map(chr,[*range(ord('0'),ord('0')+10),*range(ord('a'),ord('a')+n-10)]))
					self.i_base=n
					self.message='base='+str(self.i_base)+'alphabet='+''.join(self.i_alphabet)
				else:
					try:
						self.__user_input_handle__(n)
					except TypeError:
						self.__user_input_handle__(str(n))
