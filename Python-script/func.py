#function.py

#def hello(greet, name ='You'):
#    return '{},{}'.format(greet, name)

#print(hello('Hi', name = 'Tarak'))

def student(*args, **kwargs):
    print(args)
    print(kwargs)
student('Math','tra')
