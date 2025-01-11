start = int(input("Select a starting number: "))
end = int(input("Select an ending number: "))
increment = int(input("Select amount to increment: "))

for i in range(start, end, increment):
    print(i)