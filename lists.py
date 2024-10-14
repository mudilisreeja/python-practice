names = ['ravi', 'rani', 'anshu', 'sarah']
print(names)
print(names[2])
names.append('anil')
print(names)
names.insert(2, 'kavi')
print(names)
print(len(names))
names.sort()
print(names)
names.sort(reverse=True)
print(names)
names.pop(2)
print(names)
#Tuples#
tup = (2, 1, 3, 5)
print(tup[1:3])
print(tup.index(3))
print(tup.count(1))
###ask user to enter names of their 3 fav movies &store them in a list###
movies = []
movies.append(input("Enter 1st movie: "))
movies.append(input("Enter 2nd movie: "))
movies.append(input("Enter 3rd movie: "))
print(movies)
########check given list is palindrome or not########
list1 = [1, 2, 3, 2, 1]
copy_list1 = list1.copy()
copy_list1.reverse()
if copy_list1 == list1:
    print("palindrome")
else:
    print("not palindrome")





