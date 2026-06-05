
def Emoji(Message, output):
	Words = Message.split(" ")
	
	emojis = {
		":)" : "😁",
		":(" : "😞"
	}
	output = ""
	for Word in Words:
		output += emojis.get(Word, Word) + " "
	return output


Message = input("> ")
result = Emoji(Message, " ")
print(result)
