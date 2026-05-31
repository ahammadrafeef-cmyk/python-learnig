x = 10      # Global variable

def show():
    global x
    x = 20  # Local variable
    print(x)

show()
print(x)