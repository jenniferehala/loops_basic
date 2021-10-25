# 1. Basic
for x in range(151):
    print(x)

# 2. Multiples of Five
for x in range(5,1000,5):
    print(x)

# 3. Counting, the Dojo Way -  Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".

for i in range(101):
    print(i)
    if i % 5 == 0: 
        print("Coding")
    if i % 10 == 0:
        print("Coding Dojo")

# 4. Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.

sum = 0
for i in range(0,50000):
    if i % 2 != 0:
        sum = sum + i
    
print(sum)

# 5.  Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
def pos_function(x):
    for i in range(0,x+1):
        if i % 2 == 0:
            print(i)
            i-1

pos_function(2018)

# 6. Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)

def flex_Counter(lowNum, highNum, mult):
    for i in range(lowNum,highNum+1):
        if i % mult == 0:
            print(i)

flex_Counter(2,9,3)