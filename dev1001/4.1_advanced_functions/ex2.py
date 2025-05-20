# Callbacks Exercise
#
# 1. Write a function: perform_operation(a, b, math_callback).
# 2. This function should take two numbers and a callback.
# 3. The callback function itself should accept two numbers and return their result
#       (e.g., sum, product).
# 4. perform_operation() should then print this result.
# 5. Create two simple callbacks (e.g., add_them, multiply_them) and
#       test perform_operation with both.

def perform_operation (a,b, math_callback):
    result = math_callback (a,b)
    print(f'Result: {result}')
    
    def add_them (x,y):
        return x + y
    
    def multiply_them(x,y):
        return x * y

if 
    perform_operation (5, 10, multiply_them)
    perform_operation (5, 10, add_them)



def perform_operation(a,b,math_callback):
  return(math_callback(a,b))
# 2. This function should take two numbers and a callback.
# 3. The callback function itself should accept two numbers and return their result
#       (e.g., sum, product).
def add_them(a,b):
  return a+b
def multiply_them(a,b):
  return a*b

print(f'summarise numbers 1 and 2 = {perform_operation(1,2,add_them)}')
print(f'multiply numbers 2 and 3 = {perform_operation(2,3,multiply_them)}')

    
