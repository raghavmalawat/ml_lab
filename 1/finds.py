#Name : Raghav Malawat
#USN  : 1PE16IS080

#CODE

import csv
filename ='finds_data.csv'
lines = csv.reader(open(filename))
data = list()


for row in lines:
    # Find S uses only positive examples
	if row[-1] == "yes":
		data.append(row)
print(data)

for x in data:
	print(x)
numberOfRows = len(data)

numberOfColumns = len(data[0])-1

hypothesis = ['%' for _ in range(numberOfColumns)]

print ("Number Of Rows : ", numberOfRows)
print ("Number Of Columns : ", numberOfColumns)
print ("Initial Hypothesis : ", hypothesis)
# Set Initial Hypothesis To First Training Example
# data[0][:-1] copies the first row but NOT the last column which is the class label
hypothesis = data[0][:-1]

for i in range(numberOfRows):
    for j in range(numberOfColumns):
        
        if hypothesis[j] != data[i][j]:
            hypothesis[j] = '?'
        
        else:
            None
print ("Final Hypothesis : ", hypothesis)
testCase = input("Enter Test Case : \n")
testCase = testCase.split(",")
print ("Test Case : ")
print (testCase)
acceptFlag = 1

for i in range(len(hypothesis)):
    if hypothesis[i] != '?':
        if hypothesis[i] != testCase[i]:
            acceptFlag = 0
            break
if acceptFlag == 1:
    print ("Hypothesis Accepted")
else : 
    print ("Hypothesis Rejected")
