inputWord = raw_input("Ask user for something.")
if len(inputWord)>0:
    stringLength = len(inputWord)
    firstLetter = inputWord[0:1]
    finalWord = inputWord[1:stringLength] + firstLetter.lower() + "ay"
    print finalWord
