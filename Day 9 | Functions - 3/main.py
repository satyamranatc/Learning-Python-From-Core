# Return As Stoper
def Fun(a):
    for i in range(a):
        print(i)
        if i == 4:
            return

    print("Bye By Fun")

# Fun(10)

# Function Calling To ItSelf:
    # Recursion

def Fun(a):
    if a < 100:
        print(a)
        Fun(a+1)
    else:
        print("Bye By Fun")

# Fun(5)
        

def Gun():
    print("Gun")
    Gun()

# Gun()
    

def Fact(n):
    if n == 1:
        return 1
    else:
        return n * Fact(n-1)
    
print(Fact(5))