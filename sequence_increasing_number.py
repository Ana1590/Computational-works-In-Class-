#Check for the increasing sequence
def increase_number_sequence_check(list):
	length_of_input = len(list)
	for i in range(0,length_of_input-1):
		if list[i] < list[i+1]:
			print ("The list until position ", i ," is in increasing sequence")
			continue
		else:
			print ("The list from the position ", i ," is not in increasing sequence")
			break	
#input the number sequence
list = [1,2,3,4,7,9,10,11,77,100,9]
#Call the function to perform the check of increasing sequence
increase_number_sequence_check(list)
