import student_1 


class StudentDB:


    students = []
    def importStudentData():
        with open("studentDatabase.dat", "r") as file:
            for line in file:
                student_details  = line.strip().split(":")

                # STORING EACH STUDENT DATA AS A Dictionary
                singleStd = student_1.Student(student_details[1], student_details[0],  student_details[2],student_details[3], student_details[4].split("[")[0], student_details[4].split("[")[1].rstrip("]"))
                StudentDB.students.append(singleStd)

    def checkId(id):
        # status = False
        with open("studentDatabase.dat", "r") as f:
            for line in f:
                StudentDetails  = line.strip().split(":")
                if int(id) == int(StudentDetails[0]):
                    return False;
            return  True

    def addStudent():
    # Using this for validating all input 
            validStatus= False;
            while validStatus == False:
                id = input("Enter Id:")
                # VALIDATING ID WITH LENGHT AND NUMERIC VALUE
                if (len(id) > 0  and  id.strip().isdigit()):

                    # CHECKING IF THE ID ALREADY EXIST OR NOT?
                    validStatus = StudentDB.checkId(id)

                    #If Id already Exist then asking user if he wants to add again or go back to main Funtion: 
                    if(validStatus == False):
                        print("Uer ID Already Exist!!!")
                        print("Press Any Digit Between 1 Or 2:")
                        print("Press 1 If you want to Add a new ID ")
                        print("Press 2 If You want to go back to the main Function.")
                        n = input("Enter Number in between 1 and 2:")
                        if(int(n) == 1 ):
                            continue
                        # else: 
                        #     main()
                else:
                    print("Enter A Valid ID!!")

            validStatus= False;
            while validStatus == False:
                name = input("Enter Your Name:")
                if name.isalpha():
                    break
                else:
                    print("Enter a Valid Name!")

            validStatus= False;
            while validStatus == False:
                mail = input("Enter Your Mail:")
                if name.isalpha():
                    break
                else:
                    print("Enter a Valid Name!")


            validStatus= False;
            while validStatus == False:
                semeter = input("Enter Semester:")
                if len(semeter) > 0  and  semeter.strip().isdigit():
                    break
                else:
                    print("Enter A Valid Numeric Semester!!")

            validStatus= False;
            while validStatus == False:
                nocourses = input("Enter Number Of Courses:")
                if (len(nocourses) > 0  and  nocourses.strip().isnumeric()):
                    validStatus = True
                else:
                    print("Enter A Valid Numeric Course Number!!")
            
            courselist = [];
            # USING A NEW VARIABLE FOR TRACING THE COURSE NUMBER ACCORDING TO INPUT
            j = 1;
            print("Enter Course Codes .Course codes should be 6 characters long with three alphabets followed by 3 digits:")
            while j <= int(nocourses):
                
                coursecode = input("Enter Course Codes %d : "%j)
                # print(coursecode)
                if len(coursecode) == 6 and  coursecode[:3].isalpha() and coursecode[3:].isnumeric():
                    courselist.append(coursecode)
                else:
                    print("Enter a Valid course Name")
                    j = j-1
                j = j+1;

            # JOINING THE LIST TO MAKE PROPER COURSECODE FORMAT AS A STRING SEPARATED BY COMMA
            coursecode =  ",".join(courselist) 
            singleStd = student_1.Student(name, id,  mail, semeter, nocourses, coursecode)
            print(singleStd.name)
            StudentDB.students.append(singleStd);

            for std in StudentDB.students:
                print(std)
            print(StudentDB.students)


            with open("studentDatabase.dat", "a") as f:
                stdInfo = id + ":" + name + ":" +mail+ ":" + str(semeter)+":" +str(nocourses) +"[" +coursecode +"]"
                f.write("\n")
                f.write(stdInfo)
                print("\n")
                print("Record added successfully!")
    
    def removeStudent():
        id = input("Enter The ID You want to Remove: ")
        if id.isnumeric():
            for std in StudentDB.students:
                if int(std.id) == int(id):
                    std.removeStudent(id)

    def getStudentInfoFunc():
        id = input("Enter The ID You want to Get Information: ")
        status = 1
        if id.isnumeric():
            for std in StudentDB.students:
                if int(std.id) == int(id):
                    std.getStudentInfoFunc()
                    status  = 0
                

        if status == 1:
            print("You entered a wrong ID!!!")

    def editStudent():
        id = input("Enter The ID You want to Edit Information: ")
        status = 1
        if id.isnumeric():
            for std in StudentDB.students:
                if int(std.id) == int(id):
                    std.editStudent()
                    status  = 0

                    
        if status == 1:
            print("You entered a wrong ID!!!")

    def dropCourseOfStudent():
        id = input("Enter The ID You want to drop a course: ")
        status = 1
        if id.isnumeric():
            for std in StudentDB.students:
                if int(std.id) == int(id):
                    std.dropCourseOfStudent()
                    status  = 0

                    
        if status == 1:
            print("You entered a wrong ID!!!")

