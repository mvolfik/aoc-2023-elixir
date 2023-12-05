#![feature(let_chains)]
use std::collections::{HashMap, HashSet};
use std::io::stdin;

fn main() {
    let mut buf = String::new();
    let mut total = 0;
    let mut copies = HashMap::new();
    let mut i = 0;
    while let Ok(len) = stdin().read_line(&mut buf)
        && len > 1
    {
        i += 1;
        assert_eq!(buf.pop(), Some('\n'));
        let mut split = buf.split(": ").nth(1).unwrap().split(" | ");
        let c1 = split
            .next()
            .unwrap()
            .split(' ')
            .filter(|x| !x.is_empty())
            .map(|s| s.parse().unwrap())
            .collect::<HashSet<u64>>();

        let mut sum = 0;
        for x in split.next().unwrap().split(' ').filter(|x| !x.is_empty()) {
            let x = x.parse().unwrap();
            if c1.contains(&x) {
                sum += 1;
            }
        }
        let my_copies = *copies.get(&i).unwrap_or(&1);
        println!("{}: {} {}", i, sum, my_copies);
        for j in i..=i + sum {
            *copies.entry(j).or_insert(1) += my_copies;
        }
        total += my_copies;
        buf.clear();
    }
    println!("{}", total)
}
