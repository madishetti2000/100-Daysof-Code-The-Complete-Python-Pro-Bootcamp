#index - refers to the position of an item within a sequence, such as a string, list, tuple, or any other iterable object.
states_in_india = [
    "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", 
    "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", 
    "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", 
    "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", 
    "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", 
    "Uttarakhand", "West Bengal"
]
num_of_states=len(states_in_india)
print(len(states_in_india))
print(states_in_india[num_of_states -1])

#fruits
fruits = [
    "apple",
    "banana",
    "grape",
    "orange",
    "strawberry"]

vegetables = [
    "carrot",
    "lettuce",
    "tomato",
    "broccoli",
    "kiwi"]
dirty_dozen=[fruits, vegetables]
print(dirty_dozen[1])
print(dirty_dozen[1][1])
#dirty_dozen[1][1] is accessing the second element of the second inner list in the dirty_dozen list.

