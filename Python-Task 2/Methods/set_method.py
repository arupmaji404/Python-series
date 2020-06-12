# working with set

set1 = {1,2,3,4}	# we can define set by enclosing it in {}

# since set is immutable, we have less methods compared to other data types



maxSet = max(set1)					# this method is used to find the maximum element in the set

print(maxSet)



minSet = min(set1)					# this method is used to find the minimum element in the set

print(minSet)



lenSet = len(set1)					# this method is used to find the number of elements in set

print(lenSet)



set1.add(5)							# this method is used to add an element to the set

print(set1)



set2 = set1.copy()					# this method is used to make a copy of a set

print(set2)



set2 = {3,4,5,6,7}

set3 = {5,6,7,8,9}



intersectionSet1 = set1.intersection(set2 , set3)				# this finds the intersention elements of the sets

print(intersectionSet1)



differenceSet1 = set1.difference(set2)							# this finds the difference elements in the set

print(differenceSet1)



unionSet = set1.union(set2,set3)								# this gives the set which has all the elemnts of the mentioned sets

print(unionSet)
