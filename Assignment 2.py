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
print("Welcome to the Teacher's Simple Class Calculator")
#Menu System
print("----------------")
print("1- Enter student records (Name, ID, and 6 marks separated by commas")
print("2- Give the Total Grade, Letter Grade, and Rank of a student")
print("3- Calculate Class Average")
print("4- Display Distribution of Letter Grades")
print("5- Exit")
print("----------------")
p = 0
while p == 0:
    answer = input("Select an Option by Entering Its Number: ")
    if answer == "1": #Option 1:gives student records
        while studentNum < 10:
            record = input("Enter Student Record [Name,ID,Test1-2,Assignment1-4](Separated by commas,no spaces): ")
            
            if record.lower() == "done":
                break
            
            else: 
                recordSplit = record.split(",")#this is so input can become a list in order to faciliatate organization

                if len(recordSplit) != 8: #This is a function that will notify the user that their information is incomplete
                    print("Please insert the complete data of the student")
                elif len(recordSplit[1]) != 3: #This will reject data where ID has less or more than 3 digits
                    print("The ID of each student must have 3 digits")
                elif recordSplit[1] in iD: #This is a function for duplicates ID and update information if needed
                    update = input("Record already exists. Do you wish to update the Record? (y/n): ")
                    dupPos = iD.index(recordSplit[1])

                    if update.lower() == "y": #this will update the grades
                        student[dupPos] = recordSplit[0]
                        test1[dupPos] = recordSplit[2]
                        test2[dupPos] = recordSplit[3]
                        assign1[dupPos] = recordSplit[4]
                        assign2[dupPos] = recordSplit[5]
                        assign3[dupPos] = recordSplit[6]
                        assign4[dupPos] = recordSplit[7]
                        print("Record Updated")

                    elif update.lower() != "y" and update.lower() != "n":
                        print("Please input either y for yes and n for no")
                else:
                    student.append(recordSplit[0])#this will add the name of the student in the name database
                    iD.append(recordSplit[1])#this will add the ID of the student in the ID database
                    test1.append(recordSplit[2])#this will add the grade for test 1 in the test 1 database
                    test2.append(recordSplit[3])#this will add the grade for test 2 in the test 2 database
                    assign1.append(recordSplit[4])#this will add the grade for assignment 1 in the assignment 1 database
                    assign2.append(recordSplit[5])#this will add the grade for assignemnt 2 in the assignemnt 2 database
                    assign3.append(recordSplit[6])#this will add the grade for assignment 3 in the assignment 3 database
                    assign4.append(recordSplit[7])#this will add the grade for assignment 4 in the assignment 4 database
                    totalGrade.append(float(recordSplit[2]) + float(recordSplit[3]) + float(recordSplit[4]) + float(recordSplit[5]) + float(recordSplit[6]) + float(recordSplit[7]))
                    #this is used to calculate the final grade for a specific student
                    studentNum += 1
                    print("Record Accepted")

        #Letter Grade for Matrix Data
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
                
        #Total Grade for Matrix Data
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
            
    elif answer == "2": #Option 2: Gives Total grade, letter Grade and Rank of student
        
        #Total Grade Finter
        def TotalGradeFinder(StuID):
            idPosition = iD.index(StuID)
            return totalGrade[idPosition]

        #Letter Grade Identifier
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
        
        #Rank the students
        def RankSystem(StuID):
            rankData = copy.copy(matrixData)
            orderedRankData = sorted(rankData, key = lambda x: x[8], reverse = True)
            j = 0
                    
            while j != len(orderedRankData) - 1:
                if str(StuID) == orderedRankData[j][0]:
                    break
                
                else:
                    j += 1

            rankStu = j + 1 
            return rankStu
        
        StuID = str(input("Enter the Name and ID of the Student [name,id]: "))
        SplitStuID = StuID.split(",")
        if len(SplitStuID) == 2 and SplitStuID[0] in student: #If the length of the list isn't 2, it would give an index error, in order to prevent that we need this code
            posStudent = student.index(SplitStuID[0])
            if SplitStuID[0] in student[posStudent] and SplitStuID[1] in iD[posStudent]: #it will print total grade, letter grade and the rank with the input
                print("The Student's Total Grade is:",TotalGradeFinder(SplitStuID[1]),"\nThe student's letter grade is:", LetterGradeIdentifier(SplitStuID[1]), "\nThe student's Rank is:",RankSystem(SplitStuID[1]))

            elif SplitStuID[0] in student[posStudent] and SplitStuID[1] not in iD[posStudent]: #There will be an error if the iD is in the list but the given name is not on the list, this code is to prevent that error
                rankAnswer = input("The Student's ID does not correspond to the given name, did you mean " +iD[posStudent]+ " (y/n)?: ")
                if rankAnswer.lower() == "y":
                    print("The Student's Total Grade is:",TotalGradeFinder(iD[posStudent]),"\nThe student's letter grade is:", LetterGradeIdentifier(iD[posStudent]), "\nThe student's Rank is:",RankSystem(iD[posStudent]))
                elif rankAnswer.lower() != "y" and rankAnswer.lower() != "n":
                    print("Please input y for yes and n for no")
                    
            elif SplitStuID[0] in iD[posStudent] or SplitStuID[1] in student[posStudent]: #There will be an error if the user mixed up the order of input, this code is to prevent that error
                print("Error please enter appropriate information in appropriate order")
                
            elif SplitStuID[0] not in student[posStudent] and SplitStuID[1] in iD[posStudent]: #there will be an error if the name is in the list but the given id is not on the list, this code is to prevent that error
                print("The Student's name does not correspond to the given ID, did you mean " +student[posStudent]+ " (y/n)?")
                if rankAnswer.lower() == "y":
                    print("The Student's Total Grade is:",TotalGradeFinder(iD[posStudent]),"\nThe student's letter grade is:", LetterGradeIdentifier(iD[posStudent]), "\nThe student's Rank is:",RankSystem(iD[posStudent]))
                elif rankAnswer.lower() != "y" and rankAnswer.lower() != "n":
                    print("Please input y for yes and n for no")
                    
            else:
                print("ID and name not found, please add it in the database")
        else:
            print("Missing some information")
        
        
            
        
#need an index for students because what if Bob,123
    elif answer == "3": #Option 3: Gives the Class Average

        #Class Average
        def ClassAverage():
            numb = 0
            totalPercent = 0
            while numb != studentNum:
                totalPercent += totalGrade[numb]
                numb += 1
            return (totalPercent / numb)

        if studentNum > 0:
            print("The class average is: ", ClassAverage())
        else:
            print("Please enter student record before choosing this option")

    elif answer == "4": #Option 4: Gives Letter Grade Distribution
            
        #Letter Grade distribution
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
        if studentNum > 0:
            print(LetterGradeDistribution())
        else:
            print("Please enter student record before choosing this option")
        
    elif answer == "5":
        print("Exiting Program...")
        break
    else:
        print("Please Select an Option Within its Range")


#Issues: if total grade is equivavlent (rank system)
#Issues: the rank system occasionally work
'''
matrix.count(max) >1
    print(rank.index() + 1)
'''




#Testing the functions             

'''
print(student)
print(iD)
print(test1)
print(test2)
print(assign1)
print(assign2)
print(assign3)
print(assign4)
print(totalGrade)
'''
