'''
Kevin Li 1630941
420-LCU Computer Programming, Section 1
Friday, May 4th
S. Hillal, Instructor
Assignment 3
'''
#OPENING FILE
txt = open("students.txt","r") 
lines = txt.readlines()

#DETERMINING NUMBER OF STUDENTS
numStu = 0
for line in lines: #everytime the program goes through a line in the txt, numStu will + 1
    numStu += 1
   
#STUDENT CLASS
class Student: 
    'Base class for all students' 
    Count = 0   
    def __init__(self,st_name,st_id,total_grade = 0): 
        self.name = st_name
        self.id = st_id
        self.grade = total_grade
        Student.Count += 1

    def __eq__(self,student):
        return (self.id == student.id)
    
    #LETTER GRADE IDENTIFIER 
    def LetterGradeIdentifier(stuID):
        letter = 0
        grade = int(studentDICT.get(stuID)[1]) 
        if grade >= 87:
            letter = "A"

        elif grade >= 75 and grade <= 86:
            letter = "B"

        elif grade >= 65 and grade <= 74:
            letter = "C"

        else:
            letter = "F"

        return letter
    
    #TOTAL GRADE OF STUDENT FINDER 
    def TotalGradeFinder(stuID):
        ''' This retrieves the total grade of a specified student using his/her student ID'''
        return studentDICT.get(stuID)[1]

    #CLASS AVERAGE CALCULATOR 
    def ClassAverage(): 
        numb = 0
        totalPercent = 0
        while numb != numStu:
            for ID in studentDICT.keys():
                totalPercent += studentDICT.get(ID)[1]
                numb += 1
        return (totalPercent / numb)

    #LETTER GARDE DISTRIBUTOR #[FIX NEEDED]
    def LetterGradeDistribution():
        numA = 0
        numB = 0
        numC = 0
        numF = 0
        for ID in studentDICT.keys():
            if Student.LetterGradeIdentifier(ID) == "A":
                numA += 1
                
            elif Student.LetterGradeIdentifier(ID) == "B":
                numB += 1
                
            elif Student.LetterGradeIdentifier(ID) == "C":
                numC += 1
                
            elif Student.LetterGradeIdentifier(ID) == "F":
                numF += 1
            
        return "A: " +str(numA)+ "\nB: " +str(numB)+ "\nC: " +str(numC)+ "\nF: " +str(numF)
        
#MENU
print("Welcome to the Teacher's Simple Class Calculator")
print("----------------")
print("1- Read and Process Student's Record")
print("2- Display All Student Records")
print("3- Display Record For Specific Student")
print("4- Display Class Average and Grade Distribution")
print("5- Exit")
print("----------------")

#STUDENT INFORMATION LIST
studentDICT = {}
    
#INPUT AND LOOP
loop = 0
while loop == 0:
    answer = input("Select an Option by Entering It's Number: ")

    #EXIT FUNCTION
    if answer == "5":
        print("Exiting Program...")
        break
    
    #PROCESSING ALL THE STUDENT DATAS
    elif answer == "1":
        
        lineNUM = 0
        condition = True
        while lineNUM != numStu:
            if lineNUM <= 10:
                row = lines[lineNUM].split(",")
                row[7] = row[7].strip("\n") #Takes away the annoying \n from the last evaluation
                totalGRADE = (float(row[2]) + float(row[3]) + float(row[4]) + float(row[5]) + float(row[6]) + float(row[7]))
                studentINFO = [row, totalGRADE] #has all the information of the student in a form of a list in order to put it in the dictionary
                studentDICT.setdefault(row[1], studentINFO) #The student's record is bounded with his/her ID
                lineNUM += 1
                
            else:
                condition = False
                print("Number of students can't exceed 10 or an error has occured")

        if condition == True:
            print("Record Accepted")
            txt.close() #Closes student.txt file
            print(studentDICT) #For testing Only
            continue

    #ERROR IF DIDNT PICK OPTION 1 FIRST
    elif studentDICT == {}:
        print("Error: either you didn't let the program read or process student records ")

    #DISPLAY ALL STUDENT RECORDS
    #elif answer == "2":

    #DISPLAY INFORMATION FOR SPECIFIC STUDENT
    elif answer == "3":
        ID = input("Please enter the ID of the student: ")
        if ID in studentDICT.keys():
            totGRADE = Student.TotalGradeFinder(ID)
            letGRADE = Student.LetterGradeIdentifier(ID)
            print(studentDICT.get(ID)[0][0] + "'s total grade is:",totGRADE)
            print(studentDICT.get(ID)[0][0] + "'s letter grade is:",letGRADE)
        elif ID not in studentDICT.keys():
            print("Error: entered an invalid ID")
        

    #DISPLAY CLASS AVERAGE OR GRADE DISTRIBUTION
    elif answer == "4":
        if studentDICT != {}:
            print("The class average is:",Student.ClassAverage())
            print("The Grade Distribution is:\n" + Student.LetterGradeDistribution())

    #IF INPUT ISN'T IN THE RANGE
    else:
        print("Please Select an Option Within the Range")


#THINGS TO DO:
#STUDENT CLASS[X]
#INPUT[X]
#ANALYZE[X]
#REPORT[]
#TOTAL GRADE[X]
#LETTER GRADE[X]
#CLASS AVERAGE[X]
#GRADE DISTRIBUTION[]
#VISUALIZATION OF THE STORED DATA AS REQUESTED[]
