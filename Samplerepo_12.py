# Accept the number inside list and print max number, odd number and even number in different list...
# Solution...

list = [] #Empty list
number = int(input('How many number are you enter:-'))
for i in range(1, number+1):
    elements = int(input('Enter exact number:- '))
    list.append(elements)
print('Original list is :- ', list)
print('Original max number in the list is :- ', max(list))

even_list = []
odd_list = []

for i in list:
    if i%2==0:
        even_list.append(i)
    else:
        odd_list.append(i)

print('even_list is :- ', even_list)
print('odd_list is :- ', odd_list)

