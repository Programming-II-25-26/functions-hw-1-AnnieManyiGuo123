# takes a list and returns a new list with distinct elements from the first list
# version: Sept. 9th
# author: Annie

sample_list = [1,2,3,3,3,3,4,5]
# create a blank list to put unique numbers after seperation 
unique_list= []

# idea: 
# check through the sample list, 
# if the number is not in the list, add (append) into the unique list
def unique_numbers (list):
    for number in list:
        if unique_numbers not in unique_list:
            unique_list.append(number)
    

print ("Unique list:" ,unique_numbers(sample_list))
