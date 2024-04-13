import random

class RandomizedSet:

    def __init__(self):
        self.set = set()
        

    def insert(self, val: int) -> bool:
        b = True
        if self.set.__contains__(val):
            b = False
        self.set.add(val)
        return b

    def remove(self, val: int) -> bool:
        try:
            self.set.remove(val)
            return True
        except:
            self.set.discard(val)
            return False

    def getRandom(self) -> int:
        return random.choice(list(self.set))




if __name__ == "__main__":
    s = RandomizedSet()
    s.add(1)
    s.add(4)
    s.add(1)
    print(s.set)
    print(s.getVal())
    

