class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        def shiftandInsert(d:list[int], newdeck):
            toshift = newdeck[-1]
            newdeck.pop()
            num = d[-1]
            d.pop()
            newdeck.insert(0, toshift)
            newdeck.insert(0, num)
            

        deck.sort()
        newdeck = [deck[-1]]
        deck.pop()
        for i in reversed(range(-1, len(deck) - 1)):
            shiftandInsert(deck, newdeck)
        
        return newdeck

