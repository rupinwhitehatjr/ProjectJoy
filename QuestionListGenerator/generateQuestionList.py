

buttonTemplateFile = open("buttonTemplate.html", "r")
buttonTemplateHTML=buttonTemplateFile.read()
buttonTemplateFile.close()

QuestionListTemplateFile = open("questionListTemplate.html", "r")
QuestionListHTML=QuestionListTemplateFile.read()
QuestionListTemplateFile.close()



levels=["BEG-V1", "INT-V1","BEG-V2", "INT-V2", "PRO-V1", "PRO-V2", "ADV-V1"]
classNumbers=[144, 144, 40, 40, 144, 24, 144]

#classNumbers=[2, 2, 2, 2, 2, 2, 2]

for levelIndex in range(0,len(levels)):
	levelHTML=QuestionListHTML
	level=levels[levelIndex]
	maxClass=classNumbers[levelIndex]
	buttonHTML=""
	for classNumberIndex in range(1, maxClass+1):
		buttonHTML=buttonHTML+buttonTemplateHTML

		URL="level="+level+"&class="+str(classNumberIndex)
		#print("***************")
		buttonHTML=buttonHTML.replace("#URLDetail",URL)
		buttonHTML=buttonHTML.replace("#classNumber","C"+str(classNumberIndex))
		
		#combinedHTML=combinedHTML.replace("#nextButton", buttonHTML)
		#print(levelHTML)
	#print(buttonHTML)
	levelHTML=levelHTML.replace("#nextButton", buttonHTML)
	fileName=level+".html"
	with open(fileName, 'wb') as temp_file:
			temp_file.write(bytes(levelHTML, 'utf-8'))

