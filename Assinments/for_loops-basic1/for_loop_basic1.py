# 1.basic
for a in range(0,151,1):
    print(a)

# 2.Multiples of Five
for b in range(5,1000,5):
    print(b)
# 3
for c in range(1,101,1):

    if c % 10 == 0:  
        print("Coding Dojo")
    elif c % 5 == 0:
        print("Coding")
    else:
        print(c)

# 4
e = 0
for d in range(0,500000,1):
    if d % 2 != 0:
        e += d      # e = e + d
print(e)

# 5
for f in range(2018,0,-4):
    print(f)

# 6 a multiple of mult.
lowNum = 2
highNum = 9
mult = 2

for g in range(lowNum, highNum + 1 , 1):
    if g % mult == 0:
        print(g)