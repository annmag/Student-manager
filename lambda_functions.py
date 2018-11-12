# Lambda functions - are anonymous function defined not by using def keyword but lambda keyword
# They can have any number of arguments but just one expression, which is evaluated and returned
# They're useful in higher-order functions (taking another function as an argument)


double = lambda x: x*2
print(double(6))

# Lambda with filter function
# filter(function, iterator) - function - a function that test if elements of an iterable returns true or false
# iterable - something which is filtered - sets, lists, tuples or containers of any iterator

list_of_numbers = [12, 16, 18, 23, 29, 31, 37, 39, 40]

filtered_list_of_numbers = list(filter(lambda x: (x % 3 == 0), list_of_numbers))
print(filtered_list_of_numbers)

