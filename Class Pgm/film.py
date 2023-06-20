        #  movie python programm
def add(movie):
    i=input("Enter movie name: ")
    movie.append(i)

def search(movie):
    i=input("enter the name of movie to be searched: ")
    if(i in movie):
        print("Movie found")
    else:
        print("Movie not found")    

def delete(movie):
    i=input("Enter the name of movie to be deleted: ")
    movie.remove(i)
    print("Deleted movie is: ",i)

def display(movie):
    print("Movies are:")
    print(movie)


def main():
    movie=["pushpa","kgf","golmaal"]
    while(1):
        print("\n1-Add a Movie\n2-Delete a Movie\n3-Search a Movie\n4-Display Movies\n5-Exit\n")
        ch=int(input("Enter your choice: "))
        if(ch==1):
            add(movie)
        elif(ch==2):
            delete(movie)
        elif(ch==3):
            search(movie)
        elif(ch==4):
            display(movie)
        elif(ch==5):
            break
        else:
            print("invalid choice")

if __name__=="__main__":
            main()