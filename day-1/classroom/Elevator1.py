# # Valid Floors presented to the user are 1,2,3,4,5,6,7,8,9,10,11,12,14,15


# This is how  we get user input
selectedFloor = int(input("Select Floor Number: "))

# Alteration: 13 & 14 are no longer allowed, If someone enters 13 then change the value to 15
# If someone enters 14 then change the value to 15


# Adjust the floor if required
if selectedFloor > 13 :
    actualFloor = selectedFloor - 1
else :
    actualFloor = selectedFloor

# print out the actual floor being visited
print("The elevator will travel to the actual floor", actualFloor)
