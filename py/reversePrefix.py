class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        l = word.find(ch) + 1
        return ''.join(reversed(word[:l])) + word[l:]