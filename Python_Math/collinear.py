# Inputing data from user
A1 = input("Enter the x coordinates for A: " )
A2 = input("Enter the y coordinates for A: " )

B1 = input("Enter the x coordinates for B: " )
B2 = input("Enter the y coordinates for B: " )

C1 = input("Enter the x coordinates for C: " )
C2 = input("Enter the y coordinates for C: " )
# Puting input into coordinates
A = [float(A1), float(A2)]
B = [float(B1), float(B2)]
C = [float(C1), float(C2)]

print(A, B, C)
# Finding the slope of each segment
AB = (A[1]-B[1])/(A[0]-B[0])
BC = (B[1]-C[1])/(B[0]-C[0])
AC = (A[1]-C[1])/(A[0]-C[0])
# Checking if the same slope/Displaying the results
if AB == BC == AC:
    print("It is collinear")
else:
    print("It is not collinear")