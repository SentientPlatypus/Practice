
///Second derivative of Keplers equation at quarter of year for Mercury. Takes in radians.
fn d_d_kepler(theta_radian:&f64) -> f64 {
    0.2 * theta_radian.sin()
}

///First derivative of Keplers equation at quarter of year for Mercury. Takes in radians.
fn d_kepler(theta_radian:&f64) -> f64 {
    1.0 - 0.2 * theta_radian.cos()
}

///Keplers equation at quarter of year for Mercury. Takes in radians.
fn kepler(theta_radian:&f64) -> f64 {
    let pi: f64 = std::f64::consts::PI;
    theta_radian - 0.2 * theta_radian.sin() - pi/2.0
}

///Uses Newtons Method to find a root recursively.
fn newton_method(x:f64, thresh:f64) -> f64 {
    let concave = d_d_kepler(&x) / d_d_kepler(&x).abs();
    let x_next = x - concave * (kepler(&x) / d_kepler(&x));
    
    if (x - x_next).abs() < thresh {
        return x_next;
    }
    
    newton_method(x_next, thresh)
}

fn main() {
    let initial_guess = -144.0;
    let threshold = 0.0001; // Adjust the threshold as needed
    println!("Running Newtons Method with Initial guess as {} and threshold as {}", initial_guess, threshold);

    //run newtons method
    let root = newton_method(initial_guess, threshold);

    let root_degrees = root * 180.0 / std::f64::consts::PI;
    let formatted_degrees = format!("{:.3}", root_degrees);
    let formatted_root = format!("{:.3}", root);
    println!("Approximate root: {} radians ({} degrees). ", formatted_root, formatted_degrees);
    println!("Real value at approximate root: {}", kepler(&root));
    if root_degrees > 90.0 {
        println!("Mercury has completed over 1/4 of its orbit!")
    } else {
        println!("Mercury has not completed less than 1/4 of its orbit!")
    }
}