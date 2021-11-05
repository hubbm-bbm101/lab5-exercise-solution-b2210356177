number = int(input("Please enter a number: "))
list1 = list(range(1, number+1))
even_list=[]
odd_list=[]
x = 0
y = 0

for i in list1:
    int(i)
    z = i%2
    if z == 0:
        even_list.append(i)
    else:
        odd_list.append(i)
        
for a in odd_list:
    x = x + a

for b in even_list:
    y = y + b
    c = y/len(even_list)
    int(c)
    
print("Sum of all odd numbers up to {}= ".format(number),x)
print("Avarege of all even numbers up to {}= ".format(number),c)
        
        