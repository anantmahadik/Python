print("application to demonstrate industrial programming")

import marvellousmodule
def main():
    print("__name__",__name__)
    print("enter first number: ")
    no1=int(input())
    
    print("enter second number:")
    no2=int(input())
    
    ret=marvellousmodule.Addition(no1,no2)

    print("Addition is:",ret)

if __name__=="__main__":
    main()