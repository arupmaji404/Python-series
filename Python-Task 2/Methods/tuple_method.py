# working with tuple

tuple1 = (1,2,3,4)		# we can define tuple by enclosing it in ()

# since Tuple is immutable, we have less methods compared to other data types



count_1 = tuple1.count(1)				# this method is used to count the occurance of an element

print(count_1)



index_3 = tuple1.index(3)				# this method is used to determine the index of an element in a tuple

print(index_3)



max_tup = max(tuple1)					# this method is used to find the maximum element in the tuple

print(max_tup)



minTup = min(tuple1)					# this method is used to find the minimum element in the tuple

print(minTup)



lenTup = len(tuple1)					# this method is used to find the number of elements in tuple

print(lenTup)



slicedTup = tuple1[1:3]				# thus method is used to take a part of the whole tuple

print(slicedTup)



del slicedTup							# this method is used to delete the whole tuple

