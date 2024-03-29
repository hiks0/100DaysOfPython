
from replit import clear
def add(n1, n2):
    return n1+n2

def sub(n1, n2):
    return n1-n2

def mul(n1, n2):
    return n1*n2

def div(n1, n2):
    return n1/n2

dict={"+":add,
     "-":sub,
     "*":mul,
     "/":div}

def calculator():
    n1=float(input("Enter first number: "))
    bool=True
    while bool:
        for i in dict:
            print(f"Type {i} to perform  the operation")
    
        opr=input("Enter the operation: ")
    
   
        

   
        n2=float(input("Enter second number: "))

    

    
        funct=dict[opr]

        answer=funct(n1, n2)
        print(f"the solution for {n1}{opr}{n2} = {answer}")
        
        status=input("Enter 'y' if you want to continue with the answer or 'n' to start a new calculation or 'e' to exit the calculator\n")
        if status=="y":
            n1=answer
            continue
        elif status=="n":
            bool=False
            clear()
            calculator()
        elif status=="e":
            break
        else:
            print("invalid input!")
calculator()
            
print("The pogram has ended!")


