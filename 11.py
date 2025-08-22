#11.	Write a program to demonstrate Tuple function.

tuple1 = (1, 2, 3, 4, 5)

tuple1 = tuple1 + (6, 7, 8)
tuple1 = tuple1 + (9, 10)
tuple1 = tuple1 + (11, 12, 13)

tuple1 = tuple1[1:4]

print("tuple1 => ",tuple1)
print("tuple1.count", tuple1.count(2))
print("tuple1.index", tuple1.index(3))
print("tuple1[0]", tuple1[0])
print("tuple1[1]",tuple1[1])
print("tuple1.count(1)",tuple1.count(1))
print("tuple1.__add__((14, 15, 16))",tuple1.__add__((14, 15, 16)))