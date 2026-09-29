def example1():
    a=0
    def inner():
        nonlocal a
        a+=1
        
        return a
    return inner
    
A=example1()
print(A())




def example1():
    a=50
    def inner():
        b=25
        
        return a*b
    return inner
    
A=example1()
print(A())