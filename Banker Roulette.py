names_string = "John,Emma,Michael,Sophia,William"
names = names_string.split(",")
#The split() method is used to split a string into a list of substrings based on a specified delimiter.
import random
#get the total number of items in the list.
num_items=len(names)
#generate random numbers between 0 and 1 in the last index.
random_choice = random.randint(0, num_items - 1)
print(names[random_choice])