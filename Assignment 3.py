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
   
#STUDENT CLASS [REWORK NEEDED]
class Student: 
    'Base class for all students' 
    Count = 0   
    def __init__(self,name,ID,t1,t2,a1,a2,a3,a4,total):
        self.name = name
        self.ID = ID
        self.t1 = t1
        self.t2 = t2
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
        self.a4 = a4
        self.total = total
        self.letter = ""

    def __repr__(self):
        return("{:5s} {:4s} {:6s} {:6s} {:6s} {:6s} {:6s} {:6s} {:6.1f} {:6s}".format(self.name,self.ID,self.t1,self.t2,self.a1,self.a2,self.a3,self.a4,self.total,self.letter))
               
    #LETTER GRADE IDENTIFIER 
    def LetterGradeIdentifier(self):
        letter = 0
        grade = self.total #This is the position for the grade in the dictionary
        if grade >= 87:
            letter = "A" #If the value at the position is higher than 87, it return A

        elif grade >= 75 and grade <= 86: #If the value at the position is higher than 75 and lower than 86, it returns B
            letter = "B"

        elif grade >= 65 and grade <= 74: #if the value at the position is higher than 65 and lower than 74, it returns C
            letter = "C"

        else:
            letter = "F" 

        return letter
    
    #TOTAL GRADE OF STUDENT FINDER 
    def TotalGradeFinder(self):
        ''' This retrieves the total grade of a specified student using his/her student ID'''
        return self.total #It will get the value 

    #CLASS AVERAGE CALCULATOR 
    def ClassAverage(): 
        numb = 0 #used to indicate how many times this function will run
        totalPercent = 0 #The total percentage
        while numb != numStu: #once numb equals to numStu, this function will stop
            for ID in studentDICT.keys(): #for each key in the dictionary
                totalPercent += studentDICT.get(ID)[1] #sum of all grades
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
studentDICT = {} #empty student dictionary
    
#INPUT AND LOOP
loop = 0
while loop == 0: #making a loop
    answer = input("Select an Option by Entering It's Number: ")

    #EXIT FUNCTION
    if answer == "5":
        print("Exiting Program...")
        break
    
    #PROCESSING ALL THE STUDENT DATAS
    elif answer == "1":
        
        lineNUM = 0
        condition = True #used to prevent the number of students exceeding 10 seen below
        while lineNUM != numStu:
            if lineNUM <= 10: #Preventing the program from taking more than 10 students
                row = lines[lineNUM].split(",")
                row[7] = row[7].strip("\n") #Takes away the annoying \n from the last evaluation
                totalGRADE = (float(row[2]) + float(row[3]) + float(row[4]) + float(row[5]) + float(row[6]) + float(row[7])) #Sum of all the two test grades and the 4 assignment grades
                studentINFO = Student(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7], totalGRADE) #has all the information of the student in a form of a list in order to put it in the dictionary
                studentINFO.LetterGradeIdentifier()
                studentDICT.setdefault(row[1], studentINFO) #The student's record is bounded with his/her ID
                lineNUM += 1 #extra error checking
                
            else:
                condition = False
                print("Number of students can't exceed 10 or an error has occured")

        if condition == True:
            print("Record Accepted")
            txt.close() #Closes student.txt file
            #print(studentDICT) #For testing Only
            continue

    #ERROR IF DIDNT PICK OPTION 1 FIRST
    elif studentDICT == {}: #if the dicitonary is empty, it is because you didnt choose option one
        print("Error: either you didn't let the program read or process student records ")

    #DISPLAY ALL STUDENT RECORDS
    elif answer == "2":
        print("")
        print('{:5s}'.format("Name"),'{:5s}'.format("ID"),'{:6s}'.format("T 1"),'{:6s}'.format("T 2"),'{:6s}'.format("A1"),'{:6s}'.format("A 2"),'{:6s}'.format("A 3"),'{:6s}'.format("A 4"),'{:6s}'.format("Grade"))
        #printing a template / Category for the table (Name, ID, T1, T2, A1, A2, A3, A4)
        for i in studentDICT:#This will take the ID of each student in the dictionary
            print('{}'.format(studentDICT.get(i)))
            #printing the values for the table
        print("")
        
    #DISPLAY INFORMATION FOR SPECIFIC STUDENT
    elif answer == "3":
        ID = input("Please enter the ID of the student: ")
        student = studentDICT.get(ID,0)
        if not student:
            print("Error: entered an invalid ID")
        else:

            totGRADE = student.TotalGradeFinder() #This will find the total grade of the student with the specific ID
            letGRADE = student.LetterGradeIdentifier() #This will find the letter grade of the student with the specific ID
            print(student.name + "'s total grade is:",totGRADE) #studentDICT[0][0] is the naem of  the student
            print(student.name + "'s letter grade is:",letGRADE)

        

    #DISPLAY CLASS AVERAGE OR GRADE DISTRIBUTION
    elif answer == "4":
        if studentDICT != {}: #preventing an error from ocurring since if the dictionary is empty, it would be impossible to calculate the average / letter grade
            print("The class average is:",Student.ClassAverage())
            print("The Grade Distribution is:\n" + Student.LetterGradeDistribution())

    #IF INPUT ISN'T IN THE RANGE
    else:
        print("Please Select an Option Within the Range")


#THINGS TO DO:
#STUDENT CLASS[X]
#INPUT[X]
#ANALYZE[X]
#REPORT[X]
#TOTAL GRADE[X]
#LETTER GRADE[X]
#CLASS AVERAGE[X]
#GRADE DISTRIBUTION[X]
#VISUALIZATION OF THE STORED DATA AS REQUESTED[X]
#IF THERE ARE TWO IDENTICAL IDS IN THE TEXT FILE[]
#DIFFERENT IDS AND DUPLICATES
