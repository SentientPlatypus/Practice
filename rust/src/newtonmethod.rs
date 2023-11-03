

fn d_kepler(theta_radian:&f64) -> f64 {
    1 - 0.2 * theta_radian.cos()
}


fn kepler(theta_radian:&f64) -> f64 {
    let pi: f64 = std::f64::consts::PI;
    theta_radian - 0.2 * theta_radian.sin() - pi/2
}



fn newton_method(x:f64, thresh:f64) -> f64 {
    let x_next = x + kepler(&x) / d_kepler(&x);
    if (0 - x_next).abs() < thresh {
        return x_next
    }
    newton_method(x_next, thresh)
}


fn main() {
    let initial_guess = 1.0;
    let threshold = 1e-6; // Adjust the threshold as needed
    println!("Running Newtons Method with Initial guess as {} and threshold as {}", initial_guess, threshold);


    let root = newton_method(initial_guess, threshold);
    let root_degrees = root * 180 / std::f64::consts::PI;
    println!("Approximate root: {} degrees", root_degrees);
    if root_degrees > 90 {
        println!("Mercury has completed over 1/4 of its orbit!")
    } else {
        println!("Mercury has not completed less than 1/4 of its orbit!")
    }
}