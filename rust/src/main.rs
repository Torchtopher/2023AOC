

fn main() {
    println!("Hello, world!");
    // include file at compile time
    let data = include!("d1.txt").to_string();
    dbg!(data);

}