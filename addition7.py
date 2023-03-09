print("application to demonstrate industrial programming")

def Addition(value1,value2):
     ans=value1+value2  
     return ans

def main():
    print("enter first number: ")
    no1=int(input())
    
    print("enter second number:")
    no2=int(input())
    
    ret=Addition(no1,no2)

    print("Addition is:",ret)

if __name__=="__main__":
    main()