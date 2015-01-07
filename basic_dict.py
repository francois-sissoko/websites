#basic dictionary in Python opens youtube video

import sys 
import webbrowser

quotes = {
	"Moe" : "A wise guy,, huh?",
	"Larry" : "Ow!",
	"Curly" : "nyak,NYAK",
	"Nyan cat"  : "https://www.youtube.com/watch?v=QH2-TGUlwu4"
	}
	
stooge = "Curly"
cat = "Nyan cat"
print(stooge, "Says:", quotes[stooge])
webbrowser.open(quotes[cat])
	