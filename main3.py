#activity3
amount = int(input("Enter the amount that is withdrawn:"))

note_1 = amount//100
note_2 = (amount%100)//50
note_3 = ((amount%100)%50)//10

print("The notes of 100: " , note_1)
print("The notes of 50:" , note_2)
print("The notes of 10:" , note_3)