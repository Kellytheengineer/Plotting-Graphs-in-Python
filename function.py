#Functions in Python

#Like in mathematics where a function takes an arguement and produces a result
#does so in Python as well !

#The general form of a Python function is:
#def function name(arguments):
# {Lines telling the function what to do to produce the result}
#  return result

#Let's consider producing a function that return x^2 + y^2
def squared(x,y):
    result = x**2 + y**2
    return result


print(squared(10,2))

#A new function
def born(country):
    return print("I am from " + country)


born("England")