class Person:
    def _init_(self,f,l,e):
        self.__fname=f
        self.__lname=l
        self.__email=e
        
    def get(self):
        return self.__fname+' '+self.__lname+' '+self.__email
    
class Customer(Person):
    def _init_(self,f,l,e,id):
        Person._init_(self,f,l,e)
        self.__ID=id
    
    def get(self):
        return Person.get(self)+' '+str(self.__ID)
    
class Employee(Person):
    def _init_(self,f,l,e,pan):
        Person._init_(self,f,l,e)
        self.__PAN=pan
    def get(self):
        return Person.get(self)+' '+self.__PAN
    
    
def show(obj):
   if isinstance(obj,Customer):
      print("Customer Name,email and ID:",obj.get())
   elif isinstance(obj,Employee):
      print("Employee Name,email and PAN:",obj.get())
   elif isinstance(obj,Person):
      print("Person Name and email :",obj.get())
            
def main():
    while(True):
        n=int(input("\n1.Customer\n2.Employee \n3.Person \n4.Exit\n\nEnter your Option:"))
        if n==1:
            f,l,e,i=input("Enter customer fname,lname,email and ID:\n").split()
            c=Customer(f,l,e,i)
            show(c)
        elif n==2:
            f,l,e,p=input("Enter Employee fname,lname,email and PAN:\n").split()
            e=Employee(f,l,e,p)
            show(e)
        elif n==3:
            f,l,e,i=input("Enter Person fname,lname,email and ID:\n").split()
            p=Person(f,l,e)
            show(p)
        else:
            break
        
        

main()