use std::f64::consts::PI;

fn main() {
    let n = 1000000000;

    let mut estimation = 0.0;
    for i in 0..=n {
        estimation += (-1.0 as f64).powf(i as f64) / (2.0 * i as f64 + 1.0);
    }
    estimation *= 4.0;

    let truth = PI;
    let actual_error = estimation - truth;
    let alternating_error = 1.0 / (2.0 * n as f64 + 3.0);
    let lagrange_error = 1.0 / (2.0 * n as f64 + 2.0);

    println!("Estimation = {:.50}", estimation);
    println!("True Value = {:.50}", truth);
    println!("Act. Error = {:.50}", actual_error);
    println!("Alt. Error = {:.50}", alternating_error);
    println!("Lag. Error = {:.50}", lagrange_error);
}