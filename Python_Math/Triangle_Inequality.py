def triangle_inequality(side1, side2, side3):
    lst = [side1, side2, side3]
    largest = max(lst)
    total = sum(lst)
    other2 = (total - largest)
    if largest - other2 < 0:
        return True

    return False


side1 = input("Enter the length of side 1: ")
side2 = input("Enter the length of side 2: ")
side3 = input("Enter the length of side 3: ")

print(triangle_inequality(float(side1),float(side2),float(side3)))
