outFile = open("names.txt", "w")
nameList = ['Charlie','Roger','Romeo', 'Tom', 'Jerry', 'Cindia','Jack']
markList = [80,85,95, 81, 100, 90, 95]

for i in range(len(nameList)):
    outFile.write(nameList[i] + " " + str(markList[i]) + "\n")
outFile.close()
