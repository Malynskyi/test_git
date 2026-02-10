#1

# takes a string and returns its length
def string_length(text):
    return len(text)


# takes two strings and returns a combined string
def combine_strings(str1, str2):
    return str1 + " " + str2



word1 = "Programming"
word2 = "Python"

length = string_length(word1)
combined = combine_strings(word1, word2)


print("First string:", word1)
print("Length of the first string:", length)
print("Combined string:", combined)




#2

#takes a number and returns its square
def square_number(number):
    return number ** 2


#takes two numbers and returns their sum
def sum_numbers(num1, num2):
    return num1 + num2


#takes two integers, performs division
def divide_numbers(a, b):
    quotient = a // b     
    remainder = a % b      
    return quotient, remainder



number = 7
first_number = 12
second_number = 5

square_result = square_number(number)
sum_result = sum_numbers(first_number, second_number)
division_result = divide_numbers(first_number, second_number)


print("Number:", number)
print("Square of the number:", square_result)

print("First number:", first_number)
print("Second number:", second_number)
print("Sum of numbers:", sum_result)

print("Division result:")
print("Quotient:", division_result[0])
print("Remainder:", division_result[1])



#3

def average(numbers):
    total = 0
    for n in numbers:
        total += n
    return total / len(numbers)



def common_elements(list1, list2):
    result = []
    for item in list1:
        if item in list2:
            result.append(item)
    return result



list_a = [2, 4, 6, 8, 10]
list_b = [5, 6, 7, 8, 9]

avg = average(list_a)
common = common_elements(list_a, list_b)

print("List A:", list_a)
print("Average value:", avg)

print("List B:", list_b)
print("Common elements:", common)




#4

def print_keys(data):
    for key in data:
        print(key)



def merge_dicts(dict1, dict2):
    result = {}
    for key in dict1:
        result[key] = dict1[key]
    for key in dict2:
        result[key] = dict2[key]
    return result



student_scores = {
    "Math": 85,
    "English": 90,
    "Physics": 78
}

extra_scores = {
    "History": 88,
    "English": 92
}

print("Keys in student_scores:")
print_keys(student_scores)

merged = merge_dicts(student_scores, extra_scores)

print("Merged dictionary:")
print(merged)




# 5

def union_sets(set1, set2):
    result = set()
    for item in set1:
        result.add(item)
    for item in set2:
        result.add(item)
    return result



def is_subset(set1, set2):
    for item in set1:
        if item not in set2:
            return False
    return True



set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
set_c = {1, 2}

union_result = union_sets(set_a, set_b)
subset_result = is_subset(set_c, set_a)

print("Set A:", set_a)
print("Set B:", set_b)
print("Union of sets:", union_result)

print("Set C:", set_c)
print("Is Set C a subset of Set A?", subset_result)




# 6


def check_even(number):
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")



def get_even_numbers(numbers):
    result = []
    for n in numbers:
        if n % 2 == 0:
            result.append(n)
    return result



num = 7
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8]

check_even(num)

even_numbers = get_even_numbers(numbers_list)

print("Original list:", numbers_list)
print("Even numbers:", even_numbers)



# 7

check_even = lambda x: 1 if x % 2 == 0 else 0



number = 11

result = check_even(number)

print("Number:", number)
print("Result:", result)