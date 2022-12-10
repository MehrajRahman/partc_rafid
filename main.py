
# GREET USER for THE FIRST TIME
def showMainMenu():
    print("########################################################################" )
    print("###########################"   +  "   WELCOME ADMIN    " +  "##############################" )
    print(  " Please Choose Any Option Below: " )
    print( " [a] to add new student record " )
    print(" [e] to edit an existing student record" )
    print( " [d] to drop a course for an existing student record" )
    print( " [i] to get information about a student record " )
    print( " [r] to remove an existing student record" )
    print( " [q] to quit" )
    choice  = input("Enter Your choice: ")

    return choice


# Cleaning FIle TO remove space:
def cleaningFile():
    with open("studentDatabase.dat","r") as f:
            content = f.readlines()        
    with open("studentDatabase.dat", "w") as fd:
        for student_line in content:
            if student_line.strip():
                fd.write(student_line)
  
############################################## CALLING MAIN FUNCTION ######################################################################################################################
def main():
    import student_1 
    import studentdb_1 

    # Student = student_1.Student
    StudentDB = studentdb_1.StudentDB
    print(dir(student_1))
    # Printing Greet Mesage
    # IMPORT ALL STUDENT DATA FROM THE DB
    StudentDB.importStudentData()

    while True:
        cleaningFile()
        choice  = showMainMenu()
        # Validating user choice input
        if choice.lower() == "e":
            StudentDB.editStudent()
        elif choice.lower() == "d":
            StudentDB.dropCourseOfStudent()
        elif choice.lower() == "r":
            StudentDB.removeStudent()
        elif choice.lower() == "a":
            StudentDB.addStudent()
        elif choice.lower() == "i":
            StudentDB.getStudentInfoFunc()
        elif choice.lower() == "q":
            print("Quiting!")
            break
        else:
            print("Invalid Input, please enter a valid choice")

main()
