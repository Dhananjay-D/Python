import csv 
def addBooks(books):
    n=int(input("Enter no of books :"))
    for i in range(n):
        bno=int(input("Enter book no :"))
        title=input("Enter Title :")
        author=input("ENter author : ")
        price=float(input("Enter price : "))
        books.append([bno,title,author,price])
    with open("books.csv","a",newline='') as file:
        writeObj=csv.writer(file)
        writeObj.writerows(books)
 
def Search_by_author():
    flag=0
    au = input("Enter Author to search : ")
    with open("books.csv",newline='') as file:
        readerObj=csv.reader(file)
        for line in readerObj:
            if au==line[2]:
                flag=1
                print("Book found with details :\n",line)
            if flag==0:
                print("No book by the author ",au)

def Search_by_price():
    flag=0
    try:
        pr = float(input("Enter Price to search : "))
        if pr <= 0:
            raise ValueError("price should be greter than zero .")
    except ValueError as e:
        print(e)
        return 
    
# price > 0
    with open("books.csv",newline='') as file:
        readerObj=csv.reader(file)
        for line in readerObj:
            if pr > float(line[3]):
                flag=1
                print("Book found with details :\n",line)
            if flag==0:
                print("No book below the price ",pr)

def Search_by_word():
    flag=0
    word = input("Enter word to search in title : ")
    with open("books.csv",newline='') as file:
        readerObj=csv.reader(file)
    for line in readerObj:
        if word in line[1]:
            flag=1
            print("Book found with details :\n",line)
        if flag==0:
            print("No book with title containing word ",word)
 
def main():
    books=[]
    addBooks(books)
    print("Books are :")
    with open("books.csv",newline='') as file:
        readerObj=csv.reader(file)
        for line in readerObj:
            print(line)
    while(1):
        print("\n1.Search By Author\n2.Search By price\n3.Search By word\n4.Exit\n\n")
        opt=int(input("Enter your option : "))
        if opt ==1:
            Search_by_author()
        elif opt ==2:
            Search_by_price()
        elif opt==3:
            Search_by_word()
        elif opt==4:
            break
        else:
            print("Enter valid Choice !")
 
 
# if __name__=='__main__':
main()
