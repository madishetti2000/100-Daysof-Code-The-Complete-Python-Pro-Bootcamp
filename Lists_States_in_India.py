states_in_india = [
    "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", 
    "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", 
    "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", 
    "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", 
    "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", 
    "Uttarakhand", "West Bengal"
]
print(states_in_india[0])

#if you want to change them
states_in_india[0]="Andrapradesh"
print(states_in_india[0])

#append - add an element at the end of the list
states_in_india.append("Hyderabad")

#extend - add all the elements of an iterable (such as another list) to the end of the list
states_in_india.extend(["Warangal", "Gudur"])

print(states_in_india)
