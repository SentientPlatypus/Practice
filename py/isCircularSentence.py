class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        wordlist = sentence.split(" ")
        wordlist.append(wordlist[0])


        for i in range(1, len(wordlist)):
            if not wordlist[i][0] == wordlist[i - 1][-1]:
                return False
            
        return True