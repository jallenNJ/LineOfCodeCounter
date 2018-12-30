import sys
import os

singleLineComment = "//"
multiLineCommentStart = "/*"
multiLineCommentEnd = "*/"
preProcessorDirectives = "#"

def parseFile(name):
    file = open(name, "r")
    output = open("output.txt", "w")


    skippingLines = False

 

    counts = {
    "preProcessor" : 0,
    "multiLine" : 0,
    "singleLine" : 0,
    "whiteSpace" : 0,
    "code" : 0,
    }

    for rawLine in file:
        if rawLine.find(preProcessorDirectives) >=0 :
            counts["preProcessor"] += 1
            continue


        if skippingLines:
            counts["multiLine"] +=1
            endMultiLine = rawLine.find(multiLineCommentEnd)
            if endMultiLine >=0:
                skippingLines = False
            continue


        locationIndex = rawLine.find(multiLineCommentStart)
        if(locationIndex >= 0):
            counts["multiLine"] +=1
            skippingLines = True
            continue
        locationIndex = rawLine.find(singleLineComment)
        if(locationIndex >=0):
            counts["singleLine"] +=1
            continue    
        
        if(rawLine.isspace()):
            counts["whiteSpace"] +=1
            continue

        counts["code"] +=1
        output.write(rawLine)        



   # print("Code:", linesOfCode, "Comments:", linesOfMultiLineComments+linesOfSingleLineComments, "Whitespace", linesOfWhiteSpace, "Directives", linesOfPreProcessorDirectives )
    #print("Total:", linesOfCode+linesOfMultiLineComments+linesOfSingleLineComments+linesOfWhiteSpace+linesOfPreProcessorDirectives)
   
    sum =0
    for entry in counts:
        sum += counts[entry]
    counts["total"] = sum 
    print(counts)
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