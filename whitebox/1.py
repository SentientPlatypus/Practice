
class RingBuffer():
    def __init__(self, cap:int):
        self.start = 0
        self.count = 0
        self.cap = cap
        self.content = ["" for i in range(self.cap)]
    

    def push(self, event:str):
        self.content[(self.start + self.count) % self.cap] = event

        if self.count == self.cap:
            self.start += 1
            self.start %= self.cap
        else:
            self.count += 1
    
    def snapshot(self):
        res = []
        for i in range(self.count):
            res.append(self.content[(self.start + i) % self.cap])
        return res
    


def main():
    buf:RingBuffer = None
    while True:
        try:
            line = input()
        except:
            break
        tokens = line.split()
        if len(tokens) == 1:
            #snapshot
            print(" ".join(buf.snapshot()))
        else:
            cmd, i = tokens
            if cmd == "RingBuffer":
                buf = RingBuffer(int(i))
            else:
                #push
                buf.push(i)
                print("null")

if __name__ == "__main__":
    main()


