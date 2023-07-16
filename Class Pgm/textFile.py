# python program to read n names from user amd write to file named names.txt 
# the program should also read from file and display the names.


def main():
    listOfNames=[]
    n=int(input("enter the number of names: "))
    for i in range(0,n):
        name=input("Enter name: ")
        listOfNames.append(name)
    
    with open("names.txt","w") as file:
        for i in listOfNames:
            file.write(i+"\n")

    print("Names are: ",end="\n")
    with open("names.txt","r") as file:

        # for line in file:
        #     print(line)


        print(file.read())        #reads entire data present in the file

        # print(file.readline())        #reads single line from the file

        # print(file.readlines())  #reads entire data of file as list in which each line acts an element of an list

if __name__=="__main__":
    main()