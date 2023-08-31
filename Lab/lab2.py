#Implemention of dictionary 
def addcourse(courses):
    code=input("Enter Course Code : ")
    if code in courses:
        print("Duplicate Course Not Allowed !! " )
        return
    else:
        name=input("Enter Course Name : ")
        faculty=input("Enter Faculty : ")
        no_of_registrations=input("Enter No. of registrations : ")
        courses[code]=[name,faculty,no_of_registrations]
        print("Courses are :\n",courses)
        
#displaying all courses
def disAll(courses):
    if len(courses)==0:
        print("No Course : " )
        return
    print("Courses are :\n")
    for code,[name,faculty,no_of_registrations] in courses.items():
        print(code,' ',name,' ',faculty,' ',no_of_registrations)
        
#displaying specific course        
def disCourse(courses):
    if len(courses)==0:
        print("No Course : " )
        return
    code=input("Enter course code to search: ")
    if code in courses:
        print("Courses details are :\n")
        print(code,courses[code][0],courses[code][1],courses[code][2])
    else:
        print("Course with code ",code," not present " )
        
#finding course with highest no. of registers
def highestRegs(courses):
    if len(courses)==0:
        print("No Course : " )
        return
    regs=[]
    for details in courses.values():
        regs.append(details[2])
    maxReg=max(regs)
    print("The max no of registrations is :",maxReg)
    print("Course(s) with highest no of registrations is : ")
    for code,[name,faculty,no_of_registrations] in courses.items():
        if maxReg==no_of_registrations:
            print(name)
        
#Driver 
def main():
    courses={}
    while(1):
        print("\n1.Add course \n2.Display All Course \n3.Display Course \n4.highest registration \n5.Exit ")
        opt=int(input("Enter Your Choice : "))
        if opt==1:
            addcourse(courses)
        elif opt ==2:
            disAll(courses)
        elif opt ==3:
            disCourse(courses)
        elif opt ==4:
            highestRegs(courses)
        elif opt ==5:
            break
        else:
            print("Enter invalid Choice !! \n")
            
#if _name=="__main_":
main()