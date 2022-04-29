import os, getopt, sys, time

def main(argv):
    inputFile = ''
    outputFile = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print('SQLSanitizer.py -i <inputfile> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('SQLSanitizer.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputFile = arg
        elif opt in ("-o", "--ofile"):
            outputFile = arg

    if(inputFile != ''):
        outputFile = outputFile.replace(".sql","") if outputFile != '' else 'output'
        start_time = time.time()
        processFile(inputFile, outputFile)
        print("--- Elapsed time: %s seconds ---" % (time.time() - start_time))
    else:
        print('SQLSanitizer.py -i <inputfile> -o <outputfile>')

def extractKeywords():
    keywords = {}

    with open('keywords.csv', 'r') as keywordsFile:
        for line in keywordsFile.readlines(): 
            for s in line[:-1].split('\r'):
                keywords[s.lower()] = s
    keywordsFile.close()

    return keywords

def readSqlFileAsString(filename):
    outputText = ''
    with open(filename, 'r') as sqlFile:
        lines = sqlFile.readlines()
        outputText = outputText.join(lines)
    sqlFile.close()

    return outputText

def getOutputFileName(filepath="output", num = 2):
    filePathWithoutNum = filepath + ".sql"
    fullFilepath = filepath + str(num) + ".sql"
    
    if not os.path.isfile(filePathWithoutNum):
        return filePathWithoutNum
    elif os.path.isfile(fullFilepath):
        num += 1
        return getOutputFileName(filepath, num)
    else:
        return fullFilepath

def processFile(inputFile, outputFile):
    keywords = extractKeywords()
    outputText = readSqlFileAsString(inputFile)

    for keyword in keywords:
       outputText=outputText.replace(keyword, keywords[keyword])

    outputFileName = getOutputFileName(outputFile)

    # open output file
    outputFile = open(outputFileName,"a")
    outputFile.writelines(outputText)
    outputFile.close()

if __name__ == "__main__":
    main(sys.argv[1:])