#question : 1.07 (**) Flatten a nested list structure.

from itertools import chain
class find:
	
	def flatten(self,nestedList):
   		def aux(listOrItem):
	       		if isinstance(listOrItem, list):
		           		for elem in listOrItem:
			               		for item in aux(elem):
			                   			yield item
	       		else:
	           		yield listOrItem
   		return list(aux(nestedList))
a=find()
create_list=['a', ['b',['c','d'],'e'],'f']
print "Entered list : ",create_list
print a.flatten(create_list)