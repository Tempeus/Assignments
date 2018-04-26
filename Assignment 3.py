'''
Kevin Li 1630941
420-LCU Computer Programming, Section 1
Friday, May 4th
S. Hillal, Instructor
Assignment 3
'''
#MENU
print("Welcome to the Teacher's Simple Class Calculator")

print("----------------")
print("1- Process Text File and Store Data")
print("2- Display All Student Information")
print("3- Display Record For Specific Student")
print("4- Display Class Average and Grade Distribution")
print("5- Exit")
print("----------------")

#STUDENT INFORMATION LIST
student = []
iD = []
test1 = []
test2 = []
assign1 = []
assign2 = []
assign3 = []
assign4 = []
totalGrade = []

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

    #LISTING ALL THE STUDENT DATAS
    if answer == 1:
        
        lineNUM = 0
        condition = True
        while lineNUM != numStu:
            if lineNUM <= 10:
                row = lines[lineNUM].split(",")
                student.append(row[0])
                iD.append(row[1])
                test1.append(row[2])
                test2.append(row[3])
                assign1.append(row[4])
                assign2.append(row[5])
                assign3.append(row[6])
                assign4.append(row[7])
                totalGrade.append(float(row[2]) + float(row[3]) + float(row[4]) + float(row[5]))
                lineNUM += 1
                
            else:
                condition = False
                print("Number of students can't exceed 10 or an error has occured")

        if condition == True:
            print("Record Accepted")

        #STUDENT DICTIONARY
        student1 = {
        #https://stackoverflow.com/questions/42504450/create-student-database-in-python
        
        #STUDENT CLASS
        class Student:
            "Options for all students"
            def __init__(self,st_name,st_id):
                self.name = st_name
                self.id = st_id






'''
THINGS TO DO:
STUDENT CLASS
INPUT
ANALYZE
REPORT
TOTAL GRADE
LETTER GRADE
CLASS AVERAGE
GRADE DISTRIBUTION
VISUALIZATION OF THE STORED DATA AS REQUESTED
'''
