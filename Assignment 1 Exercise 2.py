NUM_DAY = int(input("Number of daytime minutes?: "))
NUM_EVE = int(input("Number of evening minutes?: "))
NUM_WEEK = int(input("Number of weekend minutes?: "))


A_FREE = 100 
A_DAY = (NUM_DAY - A_FREE) * 0.15
if A_DAY < 0:#this is so that we will not have a negative number or else it may reduce the total cost
    A_DAY = 0
A_EVE = NUM_EVE * 0.20
A_WEEK = NUM_WEEK * 0.25
A_TOTAL = A_DAY + A_EVE + A_WEEK + 10

B_FREE = 200
B_DAY = (NUM_DAY - B_FREE) * 0.20
if B_DAY < 0: #this is so that we will not have a negative number or else it may reduce the total cost
    B_DAY = 0
B_EVE = NUM_EVE * 0.25
B_WEEK = NUM_WEEK * 0.30
B_TOTAL = B_DAY + B_EVE + B_WEEK + 10

C_FREE = 250
C_DAY = (NUM_DAY - C_FREE) * 0.30
if C_DAY < 0: #this is so that we will not have a negative number or else it may reduce the total cost
    C_DAY = 0
C_EVE = NUM_EVE * 0.35
C_WEEK = NUM_WEEK * 0.40
C_TOTAL = C_DAY + C_EVE + C_WEEK + 10

print("Plan A costs", A_TOTAL)
print("Plan B costs", B_TOTAL)
print("Plan C costs", C_TOTAL)

if A_TOTAL < B_TOTAL and A_TOTAL < C_TOTAL:
    print("Choose Plan A")

elif B_TOTAL < A_TOTAL and B_TOTAL < C_TOTAL:
    print("Choose Plan B")

elif C_TOTAL < A_TOTAL and C_TOTAL < B_TOTAL:
    print("Choose Plan C")
