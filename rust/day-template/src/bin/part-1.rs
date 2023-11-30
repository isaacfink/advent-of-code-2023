fn main() {
    let output = part1(&2);
}

fn part1(input: &i32) -> i32 {
    input * input
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn it_works() {
        let result = part1(&2);
        assert_eq!(result, 4);
    }
}
