fn main() {
    let output = part2(&2);
}

fn part2(input: &i32) -> i32 {
    input * input
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn it_works() {
        let result = part2(&2);
        assert_eq!(result, 4);
    }
}
