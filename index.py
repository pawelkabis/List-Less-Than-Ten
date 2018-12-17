a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
c = []
d = []

for number in a:
    if number < 5:
        print (number, end = " ")

#Extras 1:
for number in a:
    if number < 5:
        b.append(number)
print(b)

#Extras 2:
c = [element for element in a if int(element) < 5 ]
print(c)

#Extras 3:
numberByUser = int(input('Enter number: '))
for number in a:
    if  number < numberByUser:
        d.append(number)
print(d)
