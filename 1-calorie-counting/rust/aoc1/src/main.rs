use std::{
    fs,
    io::{BufRead, BufReader, Lines},
};

fn main() {
    // print each line in data file
    let file = "../../data.txt".to_string();
    let testfile = "../../test_data.txt".to_string();
    let res = part1(&testfile);
    assert_eq!(res, 24_000);
    println!("Part 1 test: {res}");
    let res = part1(&file);
    println!("Part 1: {res}");

    let res = part2(&testfile);
    assert_eq!(res, 45_000);
    println!("Part 2 test: {res}");
    let res = part2(&file);
    println!("Part 2: {res}");
}

fn read_data(file: &String) -> Lines<BufReader<fs::File>> {
    let file = fs::File::open(file).expect("Failed to open file");
    let reader = BufReader::new(file);
    reader.lines()
}

// processes data stream and returns an integer
fn process_data_p1(data: Lines<BufReader<fs::File>>) -> i32 {
    let mut max_val = 0;
    let mut tot_chunk = 0;
    // loop over data and add to buffer if line is not empty
    for line in data {
        match line {
            Ok(val) => {
                // check if val is not numeric
                match val.parse::<i32>() {
                    Ok(num) => {
                        tot_chunk = tot_chunk + num;
                    }
                    Err(_) => {
                        // add to tot
                        if tot_chunk > max_val {
                            max_val = tot_chunk;
                        }
                        tot_chunk = 0;
                    }
                }
            }
            Err(e) => panic!("{e}"),
        }
    }
    max_val
}

fn process_data_p2(data: Lines<BufReader<fs::File>>, n: usize) -> i32 {
    // get max_val of top three results
    let mut top_n = vec![0; n];
    let mut tot_chunk = 0;
    // loop over data and add to buffer if line is not empty
    for line in data {
        match line {
            Ok(val) => {
                // check if val is not numeric
                match val.parse::<i32>() {
                    Ok(num) => {
                        tot_chunk = tot_chunk + num;
                    }
                    Err(_) => {
                        // add to tot
                        update_top_n(&tot_chunk, &mut top_n);
                        tot_chunk = 0;
                        continue;
                    }
                }
            }
            Err(e) => panic!("{e}"),
        }
    }
    update_top_n(&tot_chunk, &mut top_n);
    sum(top_n)
}

fn update_top_n(tot_chunk: &i32, top_n: &mut Vec<i32>) {
    let (idx, mut min_val) = minimum(&top_n);
    if *tot_chunk > min_val {
        min_val = *tot_chunk;
        top_n[idx] = min_val;
    }
}

fn minimum(vec: &Vec<i32>) -> (usize, i32) {
    let mut minidx = 0;
    let mut minval = vec[minidx];
    for (idx, val) in vec.iter().enumerate() {
        if val < &minval {
            minidx = idx;
            minval = *val;
        }
    }
    (minidx, minval)
}

fn sum(vec: Vec<i32>) -> i32 {
    let mut tot = 0;
    for val in vec {
        tot = tot + val;
    }
    tot
}

fn part1(file: &String) -> i32 {
    // read data into a lazy vector
    let data = read_data(file);
    process_data_p1(data)
}
fn part2(file: &String) -> i32 {
    // read data into a lazy vector
    let data = read_data(file);
    process_data_p2(data, 3)
}
