def greet_user():
    print("Hi are you There")
    print("welcome")


print("start")
greet_user()
print("stop")
###############
def greet_user(first_name,last_name):
    print(f'hello {first_name}  {last_name}')


print("start")
greet_user(first_name='john', last_name='smith')
print("stop")

###############
def square(number):
    return number * number


print(square(6))
# ##########
def calc_sum(a: object, b: object) -> object:
    return a + b


sum = calc_sum(5 ,6)
print(sum)
# write a function to print the length of the list
def cal_length(list):
    return len(list)


result = cal_length([1, 8, 9, 7, 10])
print(result)
# write a function to print elements in single line


def print_list(lst):
    for item in lst:
        print(item, end=' ')


cities = ['delhi', 'mumbai', 'chennai', 'kolkata']
numbers = [78, 96, 56, 23, 69]

print_list(cities)
print()
