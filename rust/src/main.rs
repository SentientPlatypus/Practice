

#[derive(Debug)]
struct Cli {
    pattern: String,
    path: std::path::PathBuf,
}


fn main() {
    let pattern: String = Default::default();
    let path: String = Default::default();
    let args = Cli {
        pattern: pattern,
        path: std::path::PathBuf::from(path),
    };

    println!("{:#?}, {:#?}", args.path, args.pattern);
}