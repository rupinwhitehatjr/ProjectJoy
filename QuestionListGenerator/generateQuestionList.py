

buttonTemplateFile = open("buttonTemplate.html", "r")
buttonTemplateHTML=buttonTemplateFile.read()
buttonTemplateFile.close()

QuestionListTemplateFile = open("questionListTemplate.html", "r")
QuestionListHTML=QuestionListTemplateFile.read()
QuestionListTemplateFile.close()



levels=["BEG", "INT","ADV", "PRO"]
days=[7,7,7,7]

#classNumbers=[2, 2, 2, 2, 2, 2, 2]

for levelIndex in range(0,len(levels)):
	levelHTML=QuestionListHTML
	level=levels[levelIndex]
	day=days[levelIndex]
	buttonHTML=""
	for classNumberIndex in range(1, day+1):
		buttonHTML=buttonHTML+buttonTemplateHTML

		URL="level="+level+"&day="+str(classNumberIndex)
		#print("***************")
		buttonHTML=buttonHTML.replace("#URLDetail",URL)
		buttonHTML=buttonHTML.replace("#classNumber","Day "+str(classNumberIndex))
		
		#combinedHTML=combinedHTML.replace("#nextButton", buttonHTML)
		#print(levelHTML)
	#print(buttonHTML)
	levelHTML=levelHTML.replace("#nextButton", buttonHTML)
	fileName="../"+level+".html"
	with open(fileName, 'wb') as temp_file:
			temp_file.write(bytes(levelHTML, 'utf-8'))

