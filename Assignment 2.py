'''
Kevin Li 1630941
420-LCU Computer Programming, Section 1
Friday, April 6th
S. Hillal, Instructor
Assignment 2
'''
import copy
student = []
iD = []
test1 = []
test2 = []
assign1 = []
assign2 = []
assign3 = []
assign4 = []
totalGrade = []

studentNum = 0


#Student grade,ID and name data management
while studentNum < 10:
    record = input("Enter Student Record [Name,ID,Test1-2,Assignment1-4](Separated by commas,no spaces): ")
    
    if record == "done":
        break
    
    else: 
        recordSplit = record.split(",")#this is so input can become a list in order to faciliatate organization

        if len(recordSplit) != 8: #This is a function that will notify the user that their information is incomplete
            print("Please insert the complete data of the student")
                  
        elif recordSplit[1] in iD: #This is a function for duplicates ID and update information if needed
            update = input("Record already exists. Do you wish to update the Record? (y/n): ")
            dupPos = iD.index(recordSplit[1])

            if update == "y": #this will update the grades
                student[dupPos] = recordSplit[0]
                test1[dupPos] = recordSplit[2]
                test2[dupPos] = recordSplit[3]
                assign1[dupPos] = recordSplit[4]
                assign2[dupPos] = recordSplit[5]
                assign3[dupPos] = recordSplit[6]
                assign4[dupPos] = recordSplit[7]
        else:
            student.append(recordSplit[0])#this will add the name of the student in the name database
            iD.append(recordSplit[1])#this will add the ID of the student in the ID database
            test1.append(recordSplit[2])#this will add the grade for test 1 in the test 1 database
            test2.append(recordSplit[3])#this will add the grade for test 2 in the test 2 database
            assign1.append(recordSplit[4])#this will add the grade for assignment 1 in the assignment 1 database
            assign2.append(recordSplit[5])#this will add the grade for assignemnt 2 in the assignemnt 2 database
            assign3.append(recordSplit[6])#this will add the grade for assignment 3 in the assignment 3 database
            assign4.append(recordSplit[7])#this will add the grade for assignment 4 in the assignment 4 database
            totalGrade.append((0.20 * float(recordSplit[2])) + (0.20 * float(recordSplit[3])) + (0.15 * float(recordSplit[4])) + (0.15 * float(recordSplit[5])) + (0.15 * float(recordSplit[6])) + (0.15 * float(recordSplit[7])))
            #this is used to calculate the final grade for a specific student
            studentNum += 1
            print("Record Accepted")

#Letter Grade Identifier
def LetterGradeIdentifier(StuID = input("Enter the Name and ID of the student: ")):
    iDpos = iD.index(StuID)
    totalGradeStudent = totalGrade[iDpos]
    letter = 0
    if totalGradeStudent >= 87:
        letter = "A"
    if totalGradeStudent >= 75 and totalGradeStudent <= 86:
        letter = "B"
    if totalGradeStudent >= 65 and totalGradeStudent <= 74:
        letter = "C"
    else:
        letter = "F"
    return(letter)


x = 0
letterGrade = []
while x != studentNum: #everything here is to give a letter grade associated to the total grade of the student
    if totalGrade[x] >= 87:
        letterGrade.append("A")
        x += 1
    elif totalGrade[x] >= 75 and totalGrade[x] <= 86:
        letterGrade.append("B")
        x += 1
    elif totalGrade[x] >= 65 and totalGrade[x] <= 74:
        letterGrade.append("C")
        x += 1
    else:
        letterGrade.append("F")
        x += 1

#Class Average
def ClassAverage():
    numb = 0
    totalPercent = 0
    while numb != studentNum:
        totalPercent += totalGrade[numb]
        numb += 1
    return (totalPercent / numb)

y = 0
totalPer = 0
while y != studentNum:
    totalPer += totalGrade[y]
    y += 1

classAvg = totalPer / studentNum

#Matrix Database
k = 0
matrixData = []
while k != studentNum:
    matrixData.append([iD[k],student[k],test1[k],test2[k],assign1[k],assign2[k],assign3[k],assign4[k],totalGrade[k],letterGrade[k]])
    k += 1
    
#Rank the students (if the total Grade equivalent)
def rankSystem(stuID = int(input("Enter the name and ID of the student: "))):
    rankData = copy.copy(matrixData)
    orderedRankData = sorted(rankData, key = lambda x: x[8], reverse = True) 
    
    j = 0
    while j != len(orderedRankData)-1:
        if str(stuID) == orderedRankData[j][0]:
            break
        else:
            j += 1
            
    rankStu = j + 1
    return(rankStu)

#Graph for distribution
    
#Give information for students when given ID

    
#Testing the functions             
print(student)
print(iD)
print(test1)
print(test2)
print(assign1)
print(assign2)
print(assign3)
print(assign4)
print(totalGrade)
print(LetterGradeIdentifier())
print(classAvg)
print(ClassAverage())
print(matrixData)
print(rankSystem())
print("----------------")

#Menu System
print("1- Enter student records (Name, ID, and 6 marks separated by commas")
print("2- Give the total grade, letter grade, and rank of a student")
print("3- Calculate class average")
print("4- Display a simple chart to show grade distribution")
print("5- Exit")

answer = input("Enter a number: ")