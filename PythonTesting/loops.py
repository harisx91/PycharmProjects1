

greeting = "Good Morning"
a = 4
if a>2:
    print("Condition matches")
else:
    print("Not Met")

print("Testing Done!")


##For loops

obj = [2,3,5,7,9]
for i in obj:
    print(i*2)

##Sum of First Natural Number 1+2+3+4+5 = 15
sums = 0
for j in range(1,6):
    sums = sums + j
    print(sums)

print("*****")
for k in range(1,10,5):
    print(k)

print("Skip First Index")

for m in range(10):
    print(m)