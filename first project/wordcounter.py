class analysedText(object):

    def __init__(self, text):
        text = text.lower()
        for i in [".", ",", "!", "?"]:
            text = text.replace(i, "")
        self.words_list = text.split(" ")
        self.words_set = set(self.words_list)

    def freqAll(self):
        words_dict = {}
        for i in self.words_set:
            words_dict[i] = self.words_list.count(i)
        return words_dict

    def freqOf(self, word):
        word = word.lower()
        return self.words_list.count(word)


entry = "Hello world hi hello, hello"
text1 = analysedText(entry)
print("Text: ", entry)
print("Word frequency: ", text1.freqAll())
print("Amount: ", text1.freqOf(input("Search for: ")))
