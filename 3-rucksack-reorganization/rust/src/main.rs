use std::{
    fs,
    io::{BufRead, BufReader, Lines},
};

fn main() {
    let file = "../data.txt".to_string();
    let testfile = "../test_data.txt".to_string();
    let res = part1(&testfile);
    println!("Part 1 test: {res}");
    let res = part1(&file);
    println!("Part 2: {res}");
    let res = part2(&testfile);
    println!("Part 2 test: {res}");
    let res = part2(&file);
    println!("Part 2: {res}");
}

fn create_buffer(file: &str) -> BufReader<fs::File> {
    let file = fs::File::open(file).expect("Unable to open file");
    BufReader::new(file)
}

fn read_data(file: &str) -> Lines<BufReader<fs::File>> {
    let reader = create_buffer(file);
    reader.lines()
}

fn part1(file: &str) -> i32 {
    let mut tot = 0;
    let data = read_data(file);
    for line in data {
        match line {
            Ok(val) => {
                tot = tot + process_line_p1(val);
            },
            Err(e) => panic!("Error: {}", e),
        }
    }
    tot
}
fn part2(file: &str) -> i32 {
    let mut buf = create_buffer(&file);
    let mut tot = 0;
    // loop until buf is empty
    while buf.fill_buf().unwrap().len() > 0 {
        let mut line1 = String::new();
        let mut line2 = String::new();
        let mut line3 = String::new();
        // read from buffer three times filling each line
        buf.read_line(&mut line1).expect("Unable to read line");
        buf.read_line(&mut line2).expect("Unable to read line");
        buf.read_line(&mut line3).expect("Unable to read line");
        // process each line1, line2, line3
        tot = tot + process_lines_p2(line1, line2, line3);
    }
    tot
}

fn priority(c: char) -> i32 {
    // lowercase items a-z have priorities 1-26
    // uppercase items A-Z have priorities 27-52
    // return the priority of c
    let mut p = 0;
    if c.is_lowercase() {
        p = c as i32 - 96;
    } else if c.is_uppercase() {
        p = c as i32 - 64 + 26;
    }
    p
}

fn process_line_p1(line: String) -> i32 {
    // get the length of the line
    let len = line.len();
    // split the line in two equal halves
    let (first, second) = line.split_at(len / 2);
    // find the common character between first and second
    let common: char = find_first_common_char(first, second).unwrap();
    priority(common)
}

fn process_lines_p2(line1: String, line2: String, line3: String) -> i32 {
    // find the common characters between line1, line2, and line3
    let common = match find_common_chars(line1, line2, line3) {
        Ok(val) => val,
        Err(e) => panic!("Error: {}", e),
    };
    priority(common)
}

fn find_first_common_char<'a>(first: &'a str, second: &str) -> Result<char, &'a str> {
    for c in first.chars() {
        if second.contains(c) {
            return Ok(c);
        }
    }
    Err("No common character found")
}

fn find_common_chars(line1: String, line2: String, line3: String) -> Result<char, &'static str> {
    // find the common characters between line1, line2, and line3
    for c in line1.chars() {
        if line2.contains(c) && line3.contains(c) {
            let common = c;
            return Ok(common)
        }
    }
    Err("Cannot find a common character between the three lines")
}
