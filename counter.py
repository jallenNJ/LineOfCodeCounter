import sys
import os

singleLineComment = "//"
multiLineCommentStart = "/*"
multiLineCommentEnd = "*/"

def parseFile(name):
    file = open(name, "r")
    output = open("output.txt", "w")


    skippingLines = False


    for rawLine in file:
        if skippingLines:
            endMultiLine = rawLine.find(multiLineCommentEnd)
            if endMultiLine >=0:
                skippingLines = False
            continue


        locationIndex = rawLine.find(multiLineCommentStart)
        if(locationIndex >= 0):
            skippingLines = True
            continue
        locationIndex = rawLine.find(singleLineComment)
        if(locationIndex >=0):
            continue    
        
        output.write(rawLine)        


    file.close()
    output.close()





#Main
if len(sys.argv) < 2:
    print ("Please include the name of the directory to search.")
    exit(-1)


if(not os.path.exists(sys.argv[1])):
    print("File/Directory does not exist")
    exit(-2)

if os.path.isdir(sys.argv[1]):
    print("is directory")
elif os.path.isfile(sys.argv[1]):
    parseFile(sys.argv[1])