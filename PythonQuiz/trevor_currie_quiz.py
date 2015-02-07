def problem_1():
    print "Hello World"
    return None

def problem_2():
    fruit_list = ['Apples', 'Oranges', 'Bananas']
    return fruit_list

def problem_3():
    fruit_list = ['Apples', 'Oranges', 'Bananas']
    print fruit_list
    return None

def problem_4():
    fruit_list = ['Apples', 'Oranges', 'Bananas']
    fruit_list[1] = 'Grapes'
    return fruit_list

def problem_5():
    fruit_list = ['Apples', 'Oranges', 'Bananas']
    for fruit in fruit_list:
        print fruit
    return None

def problem_6():
    dict = {'Bob':22, 'Carol':47, 'Justin':14}
    return dict

def problem_7(number_a,number_b):
    return number_a + number_b

def problem_8():
    function_calls = [[5,5],[10,15],[3,6]]
    for function_call in function_calls:
        print problem_7(function_call[0],function_call[1])
    return None

def problem_9(input_integer):
    while input_integer < 1000:
        input_integer += 5
        print input_integer
    return None

def problem_10():
    ''' Fizz Buzz'''
    for integer in range(101):
        string = str(integer)
        if integer%3 == 0:
            string = " Fizz"
        if integer%5 == 0:
            string += "Buzz"
        print string
    return None

class Customer(object):
    '''Problem 11'''
    def __init__(self, name, age, location='Washington', credit_score=718):
        self.name = name
        self.age = age
        self.location = location
        self.credit_score = credit_score

def problem_12():
    Jessie = Customer('Jessie',18)
    return Jessie

def problem_13():
    Jessie = Customer('Jessie',18)
    print Jessie.name
    return None

def problem_14():
    Jessie = Customer('Jessie',18)
    print Jessie.location
    return None

def problem_15():
    Jessie = Customer('Jessie',18)
    print Jessie.credit_score
    return None

def problem_16():
    Jessie = Customer('Jessie',18)
    Jessie.credit_score = 650
    return None

def problem_17():
    Jessie = Customer('Jessie',18)
    Jessie.credit_score = 650
    print Jessie.credit_score
    return None
