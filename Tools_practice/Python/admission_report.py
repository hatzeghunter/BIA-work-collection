# file for report1
def report1():
    report1=open("Students&Schools.txt","w")
    for i in range(len(student_names)):
        if i>0:
            report1=open("Students&Schools.txt","a")
            if i==(len(student_names)-1):
                report1.write(student_names[i]+"- "+school_names[i])
            else:
                report1.write(student_names[i]+"- "+school_names[i]+"\n")
        else:
            report1.write(student_names[i]+"- "+school_names[i]+"\n")
    report1.close()
    return None

# file for report2
def report2(total,eng,bus,law):
    report2=open("Acceptants&Course.txt","w")
    report2.write("Total number of students who got accepted are: "+str(total)+"\n")
    report2=open("Acceptants&Course.txt","a")
    report2.write("Total number of students who got assigned to the School of Engineering: "+str(eng)+"\n") 
    report2.write("Total number of students who got assigned to the School of Business: "+str(bus)+"\n") 
    report2.write("Total number of students who got assigned to the Law School: "+str(law))   
    report2.close()
    return None

# file for report3
def report3(r):
    report3=open("Rejectants.txt","w")
    report3.write("Total number of students who got Not Accepted are: "+str(r))
    report3.close()
    return None

# file for report4
def report4():
    report4=open("Students&Scholarships.txt","w")
    for i in range(len(scholarships)):
        report4=open("Students&Scholarships.txt","a")
        if scholarships[i]!=0:
            report4.write(student_names[i]+", will receive a scholarship covering a total of "+str(scholarships[i])+" percent of their tuition amount")
            if scholarships[len(scholarships)-1]==0:
                if i==len(scholarships)-2:
                    break
                else:
                    report4.write("\n")
            elif i==len(scholarships)-1:
                break
            else:
                report4.write("\n")
    report4.close()
    return None

# function to check if the login password is correct or not
def check_password(password):
    if len(password) >= 10:
        up=0
        digit=0
        special=0
        for char in password:
            if char.isupper():
                up=up+1
            elif char.isdigit():
                digit=digit+1
            elif not char.isalnum():
                if char==" ":
                    continue
                else:
                    special=special+1
        if (up>0) and (1<digit<4) and (special==1):
            return True
        else:
            return False
    else:
        return False

# function to get total number of students   
def get_number_of_students():
    attempts = 3
    while attempts > 0:
        num_students = int(input("Please enter the number of students (between 1 and 50): "))
        if 1 <= num_students <= 50:
            print("Number of students: ",num_students)
            return num_students
        else:
            print("Invalid Input")
            attempts -= 1
        if attempts==0:
            print("You have exceeded maximum attempts. Please try again")
            return 0

# function to form a list containing student names
def insert_students(num_students):
    print("Enter the names of the students:")
    for i in range(num_students):
        name = input(f"Enter name of student {i + 1}: ")
        student_names.append(name)
    return None

# function to assign scores and gpas for each student
def scores_and_gpas(num_students):
    for row in range(0,num_students):
        grades.append([])
        x=0
        print("\nEnter the Grades as of Student "+str(row+1)+" for 100")
        for column in range(0,len(subjects)):
            g=int(input("Enter grade of "+subjects[column]+": "))
            while int(g)>100 or int(g)<0:
                print("Invalid input, enter new input") 
                g=int(input("Enter grade of "+subjects[column]+":  "))
            grades[row].append(g)
            x=g*sch[column]+x
            if column==(len(subjects)-1):
                x=x/sum(sch)
                gpas.append(x)
    return None

# function to assign schools based on gpas and to get the number of students accepted or rejected
def assign_schools():
    eng=0
    bus=0
    law=0
    r=0
    for gpa in gpas:
        if 90 <= gpa <= 100:
            school_names.append("School of Engineering")
            eng=eng+1
            scholarships.append(15)
        elif 80 <= gpa < 90:
            school_names.append("School of Business")
            bus=bus+1
            scholarships.append(10)
        elif 70 <= gpa < 80:
            school_names.append("Law School")
            law=law+1
            scholarships.append(5)
        else:
            school_names.append("Not Accepted")
            r=r+1
            scholarships.append(0)
    total=eng+bus+law
    report2(total,eng,bus,law)
    report3(r)
    return None

# function to display scores along with gpa for all students
def print_data(num_students):
    print("\n=============================*> Students Report <*==============================")        
    # Display entered grades 
    for i in range(num_students):
        print("\n")
        print("-"*30)
        print("Student Name\t: "+student_names[i])
        print("-"*30)
        for j in range(len(subjects)):
            print(subjects[j].ljust(15)+" : "+ str(grades[i][j]).rjust(5))
            if j==(len(subjects)-1):
                print("GPA".ljust(15)+" : "+ str(round(gpas[i],2)).rjust(7))
                print("SCHOOL".ljust(15)+" : "+ school_names[i])
                if(scholarships[i]!=0):
                        print("SCHOLARSHIP".ljust(15)+" : "+ str(scholarships[i]).rjust(5)+"%")
    return None

print("Welcome to Humber College")
# print list of subjects of students
subjects=["Math","Science","Language","Drama","Music","Biology"]
# list for subject credit hours for each subject in order
sch=[4,5,4,3,2,4]
# Intialize an empty list for grades, gpas, school names, student names and scholarships
grades=[]
gpas=[]
school_names=[]
student_names=[]
scholarships=[]

attempts=1
while attempts<=3:
    password = input("Please enter your password: ")
    if check_password(password):
        num_students= get_number_of_students()
        if num_students==0:
            break
        else:
            insert_students(num_students)
            scores_and_gpas(num_students)
            assign_schools()
            report1()
            report4()
            print_data(num_students)
            break
    else:
        print("Your password is incorrect, please enter your password again")
        attempts=attempts+1
    if attempts==4:
        print("You have exceeded maximum attempts. Please Try again")