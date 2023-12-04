#![feature(let_chains)]
use std::collections::HashSet;
use std::io::stdin;

fn main() {
    let mut buf = String::new();
    let mut total = 0;
    while let Ok(len) = stdin().read_line(&mut buf)
        && len > 1
    {
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
        for x in split
            .next()
            .unwrap()
            .split(' ')
            .filter(|x| !x.is_empty())
        {
            let x = x.parse().unwrap();
            if c1.contains(&x) {
                if sum == 0 {
                    sum = 1;
                } else {
                    sum = sum * 2;
                }
            }
        }
        total += sum;
        buf.clear();
    }
    println!("{}", total)
}
