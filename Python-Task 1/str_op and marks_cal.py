# strings operations

first_name = "Arup"
second_name = "Maji"

print(first_name + " " + second_name)			# concatenation using + operator

college_name = "Asansol Engineering College"
coll_address = "Asansol"

print('{}, {}'.format(college_name,coll_address))	# concatenation using place holder operator


# working with arithmetics (calculating total and percentage)

# first let us declare the variables

sub_1 = 90
sub_2 = 95
sub_3 = 82
sub_4 = 88
sub_5 = 80

# now let us calculate percentage and total

total = (sub_1 + sub_2 + sub_3 + sub_4 + sub_5)
percent = total / 500 * 100

print(f'Total is {total} and percentage is {percent}')	# now let us print the output
