#![feature(let_chains)]

use std::{io::stdin, iter::once};

fn main() {
    let mut data = Vec::<Vec<char>>::new();
    data.push(Vec::new());
    let mut buf = String::new();
    while let Ok(len) = stdin().read_line(&mut buf)
        && len > 0
    {
        assert_eq!(buf.pop(), Some('\n'));
        data.push(once('.').chain(buf.chars()).chain(once('.')).collect());
        buf.clear();
    }
    let w = data[1].len();
    data[0] = vec!['.'; w];
    data.push(vec!['.'; w]);

    let mut sum = 0;

    for y in 1..data.len() - 1 {
        let mut num_start = None;
        for x in 1..w {
            match (data[y][x].is_numeric(), num_start) {
                (true, None) => num_start = Some(x),
                (true, Some(_)) => {}
                (false, None) => {}
                (false, Some(startx)) => {
                    if data[y - 1][startx - 1..=x]
                        .iter()
                        .chain(data[y + 1][startx - 1..=x].iter())
                        .chain(once(&data[y][startx - 1]))
                        .chain(once(&data[y][x]))
                        .any(|c| !(c.is_numeric() || *c == '.'))
                    {
                        println!("{:?}", &data[y][startx - 1..=x]);
                        sum += data[y][startx..x]
                            .iter()
                            .collect::<String>()
                            .parse::<u64>()
                            .unwrap();
                    }
                    num_start = None;
                }
            }
        }
    }
    println!("{}", sum);
}
