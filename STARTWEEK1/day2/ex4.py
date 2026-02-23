my_name = "Jack"
hello = "Hello World"
my_age = 27
my_list = [my_name, my_age, hello]

my_other_list = ["Aaron", "Ahoy", 411]

# print(my_other_list[1])

my_nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]

# print(my_nums[1:6:3])

my_nums[1] = "z" # changes 20 to "z"

my_nums.append("100")

another_list = [-9, -8, -7]

# my_nums.append(another_list) # append a list of list

my_nums = my_nums + another_list

print(my_nums)

print(my_nums[-1])

my_nums.remove("100") # remove "100" from the list
my_nums.pop(4) # remove whatever is at index 4
my_nums.pop() # remove the last element of the list

print(my_nums)

print(len(my_nums)) # how many elements are in my_nums?
print(len(str(my_nums))) # how many character are in my_nums?

my_nums.remove('z')

print(sum(my_nums))

print(sorted(my_nums)) # sorts from smallest to largest

my_chars = ['a','f','g','b']

print(sorted(my_chars))

my_names = ['leeroy', 'ruben', 'ben zion', 'Ruben']

print(sorted(my_names)) # 'Ruben' is first. weird.