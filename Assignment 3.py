'''
Kevin Li 1630941
420-LCU Computer Programming, Section 1
Friday, May 4th
S. Hillal, Instructor
Assignment 3
'''
#STUDENT CLASS
class Student: 
    'Base class for all students' 
    Count = 0   
    def __init__(self,st_name,st_id,total_grade = 0,st_credits=0): 
        self.name = st_name
        self.id = st_id
        self.grade = total_grade
        self.credits = st_credits
        Student.Count += 1
        
    def __del__(self):
        Student.Count -= 1
        print ("Deleting Student instance!")

    def __eq__(self,student):
        return (self.id == student.id)

    def __repr__(self):
        return("student {} {} {}".format(self.id,self.name,self.grade))


    #LETTER GRADE IDENTIFIER [FIX NEEDED]
    def LetterGradeIdentifier(StuID):
        iDpos = iD.index(StuID)
        totalGradeStudent = totalGrade[iDpos]
        letter = 0

        if totalGradeStudent >= 87:
            letter = "A"

        elif totalGradeStudent >= 75 and totalGradeStudent <= 86:
            letter = "B"

        elif totalGradeStudent >= 65 and totalGradeStudent <= 74:
            letter = "C"

        else:
            letter = "F"

        return letter
    
    #TOTAL GRADE OF STUDENT FINDER #[FIX NEEDED]
    def TotalGradeFinder(stuID):
        ''' This retrieves the total grade of a specified student using his/her student ID'''
        return studentDICT.get(stuID)[1]

    #CLASS AVERAGE CALCULATOR #[FIX NEEDED]
    def ClassAverage(): #go through the lines and retrieve ids
        numb = 0
        totalPercent = 0
        while numb != numStu:
            totalPercent += studentDICT.get(ID)[1]
            numb += 1
        return (totalPercent / numb)

    #LETTER GARDE DISTRIBUTOR #[FIX NEEDED]
        def LetterGradeDistribution():
            m = 0
            numA = 0
            numB = 0
            numC = 0
            numF = 0

            while m != studentNum:
                if matrixData[m][9].count("A") == 1:
                    numA += 1
                    m += 1
                elif matrixData[m][9].count("B") == 1:
                    numB += 1
                    m += 1
                elif matrixData[m][9].count("C") == 1:
                    numC += 1
                    m += 1
                elif matrixData[m][9].count("F") == 1:
                    numF += 1
                    m += 1
                
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

#OPENING FILE
txt = open("students.txt","r")
lines = txt.readlines()

#DETERMINING NUMBER OF STUDENTS
numStu = 0
for line in lines:
    numStu += 1
#INPUT AND LOOP
loop = 0
while loop == 0:
    answer = input("Select an Option by Entering It's Number: ")

    #PROCESSING ALL THE STUDENT DATAS
    if answer == "1":
        
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
            print(studentDICT)
            continue
        
    #DISPLAY ALL STUDENT RECORDS
    #if answer == "2":
        
    #EXIT FUNCTION
    elif answer == "5":
        print("Exiting Program...")
        break

    #IF INPUT ISN'T IN THE RANGE
    else:
        print("Please Select an Option Within the Range")


    
        




#THINGS TO DO:
#STUDENT CLASS[X]
#INPUT[X]
#ANALYZE[X]
#REPORT[]
#TOTAL GRADE[]
#LETTER GRADE[]
#CLASS AVERAGE[]
#GRADE DISTRIBUTION[]
#VISUALIZATION OF THE STORED DATA AS REQUESTED[]
