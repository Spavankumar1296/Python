def remove(set1,set2):
	return set1.symmetric_difference(set2)
set1={1,2,3,4}
set2={3,4,5,6}
newset=remove(set1,set2)
print(newset)