class Array:
  def __init__(self,n):
		self.__data=[]
		for i in range(n):
			self.__data.append(None)
			
	def get_length(self):
		return len(self.__data)
		
	def set_item (self,index,value):
		if index>=0 and index <=len(self.__data):
			self.__data[index]=value
		else:
			print("Fuera de rango")
			
	def get_item(self, index):
		if index >=0 and index<=len(self.__data)[index]
			
	def clearing(self,valor):
		for index in range(len(self.__data)):
			self.__data[index]=valor
				
	def to_string(self):
		print(self.__data) 
		
def main():
main()
