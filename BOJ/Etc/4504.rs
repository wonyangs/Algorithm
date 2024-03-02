use std::io;

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("");
    
    let n: i32 = input.trim().parse().expect("");
    
    loop {
        let mut input = String::new();
        io::stdin().read_line(&mut input).expect("");

        let num: i32 = input.trim().parse().expect("");
        if num == 0 {
            break;
        }
        if num % n != 0 {
            println!("{} is NOT a multiple of {}.", num, n);
        } else {
            println!("{} is a multiple of {}.", num, n);
        }
    }
}
