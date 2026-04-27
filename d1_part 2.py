def odd_even(x):
    if x %2 == 0:
        return "even"
    else:
        return "odd"
    
x=int(input("Enter a number: "))

print(odd_even(x))