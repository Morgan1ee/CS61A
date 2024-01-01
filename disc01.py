#Q1
def special_case():
    x = 10
    if x > 0:
        x += 2
    elif x < 13:
        x += 3
    elif x % 2 == 1:
        x += 4
    return x

special_case()   #12


def just_in_case():
    x = 10
    if x > 0:
        x += 2
    if x < 13:
        x += 3
    if x % 2 == 1:
        x += 4
    return x
just_in_case() #19

def case_in_point():
    x = 10
    if x > 0:
        return x + 2
    if x < 13:
        return x + 3
    if x % 2 == 1:
        return x + 4
    return x
case_in_point() #12

'''Which of these code snippets result in the same output, and why? Based on your findings, when do you think using
a series of if statements has the same effect as using both if and elif cases?
1 and 3.
only one of the if statements is true or the value is not changed and returned after the truthy statement, then ...'''

#Q2
def wears_jacket_with_if(temp, raining):
    """
    >>> wears_jacket_with_if(90, False)
    False
    >>> wears_jacket_with_if(40, False)
    True
    >>> wears_jacket_with_if(100, True)
    True
    """
    "*** YOUR CODE HERE ***"
    return (temp <60 or raining == True)
    #return temperature < 60 or raining

#Q3
def nearest_ten(n):
    """
    >>> nearest_ten(0)
    0
    >>> nearest_ten(4)
    0
    >>> nearest_ten(5)
    10
    >>> nearest_ten(61)
    60
    >>> nearest_ten(2023)
    2020
    """
    "*** YOUR CODE HERE ***"
    if n%10 >= 5:
        return (n//10)*10+10
    else:
        return (n//10)*10
'''def round_to_nearest_ten(n):
    return n + (10 - n % 10) if n % 10 >= 5 else n - n % 10
'''

#Q4
def square(x):
    print("here!")
    return x * x

def so_slow(num):
    x = num
    while x > 0:
        x = x + 1
    return x / 0

square(so_slow(5))
#square function is an infinite loop never ends, teh outside function will not execute because of that, the 'here' will n0ot be printed.

#Q5
def fizzbuzz(n):
    """
    >>> result = fizzbuzz(16)
    1
    2
    fizz
    4
    buzz
    fizz
    7
    8
    fizz
    buzz
    11
    fizz
    13
    14
    fizzbuzz
    16
    >>> print(result)
    None
    """
    "*** YOUR CODE HERE ***"
    for i in range(n):
        if i%15==0:
            print('fizbuzz')  
        elif i%3==0:
            print('fizz') 
        elif i%5==0: 
            print('buzz') 
        else:
            print(i)

#Q6
def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    >>> is_prime(1) # one is not a prime number!!
    False
    """
    "*** YOUR CODE HERE ***"
    if n>2:
        for i in range(2,n):  #(2,int(n**0.5)+1)
            if n%i ==0:
                return False
    elif n==1:
        return False
    return True

#Q7
def unique_digits(n):
    """Return the number of unique digits in positive integer n.

    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(101) # 0 and 1
    2
    """
    "*** YOUR CODE HERE ***"
    a=0
    for i in range(10):
        if has_digit(n, i):
            a+=1
    return a
def has_digit(n, k):
    """Returns whether k is a digit in n.

    >>> has_digit(10, 1)
    True
    >>> has_digit(12, 7)
    False
    """
    assert k >= 0 and k < 10
    "*** YOUR CODE HERE ***"
    while n>0:
        if n%10==k:
            return True
        else:
            n=n//10
    return False

#Q8
x = 11 % 4
y = x
x **= 2
'''
Global frame:
x 3
y 3
x 9'''

#Q9
def double(x):
    return x * 2

def triple(x):
    return x * 3

hat = double
double = triple
'''Global frame:               
double - func double(x) [parent = Global] -> o1
triple - func triple(x) [parent = Global] -> o2
hat - func double(x) [parent = Global] -> o1
double - func tripel(x) [parent = Global] -> o2

Objects:      
def double(x):
    return x * 2
def triple(x):
    return x * 3  
'''













