print("Welome to the tip calculator!")
bill=float(input("what was the total bill? $"))
tip=int(input("How much tip would you like to give? 10, 20 or 15? "))
people=int(input("How many people to split the bill?"))
tip_as_percent=tip/100
total_tip_amount = bill* tip_as_percent
total_bill=bill+total_tip_amount
bill_per_person = total_bill/people
final_amount= round(bill_per_person)
print(f"Each person should pay {final_amount}")


# bill_with_tip= tip/100*bill+bill
# print(bill_with_tip)