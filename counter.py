import sys
import os
import argparse

singleLineComment = "//"
multiLineCommentStart = "/*"
multiLineCommentEnd = "*/"
preProcessorDirectives = "#"

def parseFile(name):
    file = open(name, "r")
    #output = open("output.txt", "w")


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
            #Note: If a new multi line comment open on the same line one closes on, it will not find it
            if endMultiLine >=0:
                skippingLines = False
            continue


        #Note: If multi line starts on a line that contains code before, it will be marked as a comment
        locationIndex = rawLine.find(multiLineCommentStart)
        if(locationIndex >= 0):
            counts["multiLine"] +=1
            endOnSameLine = rawLine.find(multiLineCommentEnd, locationIndex)
            if(endOnSameLine < 0):
                skippingLines = True
            continue
        locationIndex = rawLine.find(singleLineComment)


        #TODO: Add a counter for inline comments, must be stored different as it occupies same line of code
        if(locationIndex >=0):
            line = rawLine[:locationIndex]
            possSingleLine = True
        else:
            line = rawLine 
            possSingleLine = False;   
        
        if(line.isspace()):
            if possSingleLine:
                counts["singleLine"] +=1
            else:
                counts["whiteSpace"] +=1
            continue

        counts["code"] +=1
   #     output.write(line)        



   
    sum =0
    for entry in counts:
        sum += counts[entry]
   # counts["total"] = sum 
    print(counts)
    print("Total", sum)
    file.close()


    return {
        "name" : name,
        "total" : sum,
        "counts":counts
    }
  #  output.close()


def checkDirectory(directory):


    counts = {
        "preProcessor" : 0,
        "multiLine" : 0,
        "singleLine" : 0,
        "whiteSpace" : 0,
        "code" : 0,
        "total" :0
    }
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        result = parseFile(directory+"\\"+filename)
        for field in result["counts"]:
            counts[field] += result["counts"][field]
        counts["total"] += result["total"]    

    print ("For directory" + directory)
    print(counts)        




#Main

parser = argparse.ArgumentParser(description="Count lines of code in a directory or file")
parser.add_argument('-i', '--input', metavar="", required=True, help="The file or directory to check the lines of code")

args = parser.parse_args()


if(not os.path.exists(args.input)):
    print("File/Directory does not exist")
    exit(-2)

if os.path.isdir(args.input):
    checkDirectory(args.input)
elif os.path.isfile(args.input):
    parseFile(args.input)