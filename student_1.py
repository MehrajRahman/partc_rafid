
import studentdb_1 



StudentDB = studentdb_1.StudentDB



class Student:

    def __init__(self,name, id,  mail, semester, nofcourse, coursecodes):
        self.name = name
        self.id = id
        self.mail = mail
        self.semester = semester
        self.nofcourse= nofcourse
        self.coursecodes = coursecodes

    # Defining Id to Check ID Already Exist OR Not?
    def checkId(self,id):
        # status = False
        with open("studentDatabase.dat", "r") as f:
            for line in f:
                StudentDetails  = line.strip().split(":")
                if int(id) == int(StudentDetails[0]):
                    return False;
            return  True

    # Remove Student
    def removeStudent(self, id):
        ans = self.checkId(id)
        if ans == False:
            with open("studentDatabase.dat","r") as f:
                content = f.readlines()

            with open("studentDatabase.dat", "w") as fd:
                for line in content:
                    n = line.strip().split(":")
                    if id != n[0]:
                        fd.write(line)

            print("--------------Successfully Deleted The Record _-------------")
        else:
            print("Student ID Does not matched!!!")

    # Get STDUENT INFO
    def getStudentInfoFunc(self):
                        print("ID: %s"%(self.id))
                        print("Name: %s"%(self.name))
                        print("Semester: %s"%(self.semester))
                        print("Email: %s"%(self.mail))
                        print("Number of Courses: %s"%(self.nofcourse))
                        print("Course Code: %s"%(self.coursecodes))

                        print("\n")

    def editStudent(self):
                print("Select What You want to edit:")
                print("e) for edit email")
                print("s) for edit semester")
                editStatus = input("Enter e or s: ")
                if  editStatus == "e":
                    newEmail = input("Enter New Email: ")
                    self.mail = newEmail
                    with open("studentDatabase.dat", "w+") as fn:
                        for line in StudentDB.students:
                            stdInfo = line.id + ":" + line.name + ":" +line.mail+ ":" + str(line.semester)+":" +str(line.nofcourse) +"[" +line.coursecodes +"]"
                            print(stdInfo)
                            fn.write("\n")
                            fn.write(stdInfo)
                            print("")
                        print("Email Has Been Changed!!!!")
                # Upate The File According to the cahnged data.
                elif editStatus == "s":
                    newsem = input("Enter New Semester: ")

                    self.semester = newsem
                    with open("studentDatabase.dat", "w+") as fn:

                        for line in StudentDB.students:
                            stdInfo = line.id + ":" + line.name + ":" +line.mail+ ":" + str(line.semester)+":" +str(line.nofcourse) +"[" +line.coursecodes +"]"
                            fn.write("\n")
                            fn.write(stdInfo)
                            print("\n")

                        print("Semester Has Been Changed!!!!")
                else: 
                    print("You Entered A Wrong Input!!")
    
    # DROP STUDENT
    def dropCourseOfStudent(self):  
            dropStatus = True
            while dropStatus == True:
                if int(self.nofcourse) > 0:
                    # cleaningFile()
                    print("Enter The Course Code You Want To Drop:")
                    courses = self.coursecodes.split(",")
                    print(courses)
                    length = len(courses)
                    if (length == 1 and courses[0] == "") or length == 0:
                        dropStatus = False
                        print("You Removed All The Course!!!!!!!!!!")
                        print("\n")
                                                           
                    if dropStatus:
                                j = 1;
                                print("Courses Of %s: "%(self.name))
                                while j <= length:
                                    print("Course %d:  %s"%(j, courses[j-1]))
                                    j = j +1
                                print("Enter The course you want to drop: ")
                                code = input("Enter Course Code: ")
                        
                                if code in courses:
                                    # REMOVING FROM THE COURSSE LIST
                                    courses.remove(code)
                                    self.nofcourse = int(self.nofcourse) - 1
                                    if int(self.nofcourse == 0 ):
                                        dropStatus = False
                                    courseList = ",".join(courses) 
                                    self.coursecodes = courseList                      

                                    with open("studentDatabase.dat", "w+") as fn:
                                        for line in StudentDB.students:
                                            stdInfo = line.id + ":" + line.name + ":" +line.mail+ ":" + str(line.semester)+":" +str(line.nofcourse) +"[" +line.coursecodes +"]"
                                            fn.write(stdInfo)
                                            fn.write("\n")
                                        # cleaningFile()                                 
                                        print("\n**********************Course HAS BEEN DROPPED SUCCESSFULLY***********************")
                                else:
                                    print("You Entered A Wrong Course Code")

