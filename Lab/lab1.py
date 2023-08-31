# queue implementation programm :

def enque(Q):
    x=input("Enter the element to be stored: ")
    Q.append(x)

def deque(Q):
    if(Q == []):
        print("Queue underflow!")
    else:
        return (Q.pop(0))

def display(Q):
    for item in Q:
        print(item,end=" ")

def queueFront(Q):
    return Q[0]

def queueRear(Q):
    return Q[len(Q)-1]


#main programm  :
def main():
    Q=[]
    while(1):
        print("\n1-Enque\n2-Deque\n3-Display\n4-QFront\n5-QRear\n6-Exit\n")
        ch=int(input("\nEnter Your Choice: \n"))
        if(ch==1):
            enque(Q)
        elif(ch==2):
            print("Deleted element is: ",deque(Q))
        elif(ch==3):
            display(Q)
        elif(ch==4):
            print("First element in List is: ",queueFront(Q))
        elif(ch==5):
            print("Last element in List is: ",queueRear(Q))
        elif(ch==6):
            break
        else:
            print("invalid choice!")



if __name__=="__main__":
        main()