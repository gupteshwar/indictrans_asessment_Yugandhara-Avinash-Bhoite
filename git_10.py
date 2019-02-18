#question : 1.10 (*) Run-length encoding of a list.
#Use the result of problem 1.09 to implement the so-called run-length encoding data compression method. Consecutive duplicates of elements are encoded as terms [N,E] where N is the number of duplicates of the element E.

class find:
	def enter_list(self):
		input_element=raw_input('Enter comma seperated repeated elements -')
		mylist=[ x for x in input_element.split(',')]
		return mylist
	def get_sublist(self,x):
		prev=""
		return_list=[]
		flag=0
		for i in range(len(x)):
			if x[i]!=prev:
				if flag==0:
		 			sorted_list=[]
					sorted_list.append(x[i])
					prev=x[i]
				else:
					return_list.append(sorted_list)
					sorted_list=[]
					sorted_list.append(x[i])
					prev=x[i]
			elif x[i]==prev:
				sorted_list.append(x[i])
				prev=x[i]
				flag=1
			if i==len(x)-1:
				return_list.append(sorted_list)
		return return_list
	def subcount(self,nested):
		new_list=[]
		for i in nested:
			sub_list=[]
			sub_list.append(len(i))
			sub_list.append(i[0])
			new_list.append(sub_list)
		return new_list

a=find()
create_list=a.enter_list()
print "Entered list : ",create_list
slist= a.get_sublist(create_list)
print a.subcount(slist)