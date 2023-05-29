struct ParkingSystem {
    Bs:i32,
    Ms:i32,
    Ss:i32
}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl ParkingSystem {

    fn new(big: i32, medium: i32, small: i32) -> Self {
        Self{
            Bs:big,
            Ms:medium,
            Ss:small
        }
    }
    
    fn add_car(&mut self, car_type: i32) -> bool {
        let mut b:bool = false;
        let mut slot = match car_type {
            1 => &mut self.Bs,
            2 => &mut self.Ms,
            3 => &mut self.Ss,
            _ => &mut self.Bs
        };

        if slot > &mut 0 {
            *slot -= 1;
            b = true;
        }
        b
    }
}

/**
 * Your ParkingSystem object will be instantiated and called as such:
 * let obj = ParkingSystem::new(big, medium, small);
 * let ret_1: bool = obj.add_car(carType);
 */