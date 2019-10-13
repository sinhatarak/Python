def dev42by(divideby):
    try:
        return 42 / divideby
    except ZeroDivisionError:
        print('Err: you tried to divide by zero')
print(dev42by(2))
print(dev42by(12))
print(dev42by(0))
print(dev42by(1))

# getting ZeroDevison error, so use error handling method using try and except
