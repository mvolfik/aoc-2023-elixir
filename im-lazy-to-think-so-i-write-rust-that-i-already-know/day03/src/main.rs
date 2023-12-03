#![feature(let_chains)]

use std::{collections::HashMap, io::stdin, iter::once};

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

    let mut gears = HashMap::<_, Vec<u64>>::new();

    for y in 1..data.len() - 1 {
        let mut num_start = None;
        for x in 1..w {
            match (data[y][x].is_numeric(), num_start) {
                (true, None) => num_start = Some(x),
                (true, Some(_)) => {}
                (false, None) => {}
                (false, Some(startx)) => {
                    let num = data[y][startx..x]
                        .iter()
                        .collect::<String>()
                        .parse::<u64>()
                        .unwrap();

                    for (x, y) in (startx - 1..=x)
                        .map(|x| (x, y - 1))
                        .chain((startx - 1..=x).map(|x| (x, y + 1)))
                        .chain(once((startx - 1, y)))
                        .chain(once((x, y)))
                    {
                        if data[y][x] == '*' {
                            gears.entry((x, y)).or_default().push(num);
                        }
                    }

                    num_start = None;
                }
            }
        }
    }

    let res = gears
        .into_iter()
        .filter(|(_, v)| v.len() == 2)
        .map(|(_, v)| v[0] * v[1])
        .sum::<u64>();

    println!("{}", res);
}
