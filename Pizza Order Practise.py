print("Thank you for choosing Python Pizza Deliveries!")
size= input() #what size pizza do you want? "S","M", "L"
add_pepporoni = input() # Do you want pepporoni? "Y" or "N"
extra_cheese = input()# Do you want extra cheese? "Y" or "N"
bill=0
if size=="S":
  bill+15
elif size=="M":
  bill+=20
else:
  bill+=25
if add_pepporoni == "Y":
    if size=="S":
        bill+=2
    else:
        bill+=3
if extra_cheese == "Y":
    bill+=1

print(f"your final bill is: ${bill}.")             
    