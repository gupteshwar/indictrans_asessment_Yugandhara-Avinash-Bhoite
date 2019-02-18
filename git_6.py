#question : 1.06 (*) Find out whether a list is a palindrome.

class find:
	def enter_list(self):
		input_element=raw_input('Enter comma seperated elements -')
		mylist=[ x for x in input_element.split(',')]
		return mylist

	def find_reverse(self,x):
		reverse=x[::-1]
		return "List is palindrome" if x==reverse else "List is not palindrome"
a=find()
create_list=a.enter_list()
print "Entered list : ",create_list
print a.find_reverse(create_list)