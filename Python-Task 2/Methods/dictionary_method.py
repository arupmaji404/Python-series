# working with dictionary

dict = {'name' : 'Arup' , 'id' : '1357' , 'college' : 'aec' }

print(dict)


print(dict.items())


print(dict.keys())					# this will print all the keys in the dictionary


print(dict.values())				# this will print all the values in the dictionary


dict['name'] = "Arkya"				# this will edit the value of the corresponding key

print(dict)



lenDict = len(dict)				# this will return the length of the dictionary

print(lenDict)



getName = dict.get('name')			# this will return the value of the specified value of the key

print(getName)



popedName = dict.pop('name')		# this will pop the element pair that is mentioned

print(popedName)



popedItem = dict.popitem()			# this will pop the last element pair

print(popedItem)



dict.clear()						# this will clear the whole dictionary



print(dict)