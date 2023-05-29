class ParkingSystem:
    
    def __init__(self, big: int, medium: int, small: int):
        self.bs = big
        self.ms = medium
        self.ss = small    

    def addCar(self, carType: int) -> bool:
        b = False
        if carType == 1:
            if self.bs > 0:
                b = True
                self.bs -= 1
        if carType == 2:
            if self.ms > 0:
                b = True
                self.ms -= 1
        if carType == 3:
            if self.ss > 0:
                b = True
                self.ss -= 1
        return b


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)