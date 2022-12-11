/*
* expect: 
Part 1
Total: 15
Part 1
Total: 12855
Part 2
Total: 12
Part 2
Total: 13726
*/
use std::{
    fs,
    io::{BufRead, BufReader, Lines},
};

enum RPS {
    Rock,
    Paper,
    Scissors,
}

enum Outcome {
    Lose,
    Draw,
    Win,
}

fn main() {
    let file = "../data.txt".to_string();
    let testfile = "../testdata.txt".to_string();
    let res = part1(&testfile);
    println!("Part 1 test: {res}");
    let res = part1(&file);
    println!("Part 2: {res}");
    let res = part2(&testfile);
    println!("Part 2 test: {res}");
    let res = part2(&file);
    println!("Part 2: {res}");
}

fn part1(file: &String) -> i32 {
    let mut tot = 0;
    let data = read_data(&file);
    for line in data {
        match line {
            Ok(line) => {
                // process line
                tot = tot + process_line_p1(line);

            }
            Err(err) => println!("{}", err),
        }
    }
    tot
}

fn read_data(file: &String) -> Lines<BufReader<fs::File>> {
    let file = fs::File::open(file).expect("Failed to open file");
    let reader = BufReader::new(file);
    reader.lines()
}


fn part2(file: &String) -> i32 {
    // X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win
    let mut tot = 0;
    let data = read_data(file);
    for line in data {
        match line {
            Ok(line) => {
                // process line
                tot = tot + process_line_p2(line);

            }
            Err(err) => println!("{}", err),
        }
    }
    tot
}
fn process_line_p1(line: String) -> i32 {
    let arr: Vec<&str> = line.split(" ").collect();
    if arr.len() != 2 {
        panic!("Line split not equal to two");
    }
    let (opp, me) = play_p1(arr[0], arr[1]);
    let p1 = points_from_play_p1(&me);
    let p2 = points_from_outcome_p1(&opp, &me);
    p1 + p2
}


fn process_line_p2(line: String) -> i32 {
    let arr: Vec<&str> = line.split(" ").collect();
    if arr.len() != 2 {
        panic!("Line split not equal to two");
    }
    let (opp, me) = play_p2(arr[0], arr[1]);
    let p1 = points_from_play_p1(&me);
    let p2 = points_from_outcome_p1(&opp, &me);
    p1 + p2
}

fn play_p1(txt1: &str, txt2: &str) -> (RPS, RPS) {
    // Determines which moves the opponent and user make
    let opp = match txt1 {
        "A" => RPS::Rock,
        "B" => RPS::Paper,
        "C" => RPS::Scissors,
        _ => panic!("Text not recognized as valid RPS"),
    };
    let me = match txt2 {
        "X" => RPS::Rock,
        "Y" => RPS::Paper,
        "Z" => RPS::Scissors,
        _ => panic!("Text not recognized as valid RPS"),
    };
    
    (opp, me)
}


fn play_p2(txt1: &str, txt2: &str) -> (RPS, RPS) {
    // Determines which moves the opponent and user make
    // X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win
    let opp = match txt1 {
        "A" => RPS::Rock,
        "B" => RPS::Paper,
        "C" => RPS::Scissors,
        _ => panic!("Text not recognized as valid RPS"),
    };
    let outcome = match txt2 {
        "X" => Outcome::Lose,
        "Y" => Outcome::Draw,
        "Z" => Outcome::Win,
        _ => panic!("Text not recognized as valid RPS"),
    };

    let me = match outcome {
        Outcome::Lose => {
            match opp {
                RPS::Rock => RPS::Scissors,
                RPS::Paper => RPS::Rock,
                RPS::Scissors => RPS::Paper,
            }
        },
        Outcome::Draw => {
            match opp {
                RPS::Rock => RPS::Rock,
                RPS::Paper => RPS::Paper,
                RPS::Scissors => RPS::Scissors,
            }
        },
        Outcome::Win => {
            match opp {
                RPS::Rock => RPS::Paper,
                RPS::Paper => RPS::Scissors,
                RPS::Scissors => RPS::Rock,
            }
        }
    };
    
    (opp, me)
}

fn points_from_play_p1(me: &RPS) -> i32 {
    match me {
        RPS::Rock => 1,
        RPS::Paper => 2,
        RPS::Scissors => 3,
    }
}

fn points_from_outcome_p1(opp: &RPS, me: &RPS) -> i32 {
    match (opp, me) {
        (RPS::Rock, RPS::Rock) => 3,
        (RPS::Rock, RPS::Paper) => 6,
        (RPS::Rock, RPS::Scissors) => 0,
        (RPS::Paper, RPS::Rock) => 0,
        (RPS::Paper, RPS::Paper) => 3,
        (RPS::Paper, RPS::Scissors) => 6,
        (RPS::Scissors, RPS::Rock) => 6,
        (RPS::Scissors, RPS::Paper) => 0,
        (RPS::Scissors, RPS::Scissors) => 3,
    }
}
