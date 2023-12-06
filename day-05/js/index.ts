import { readFile } from "fs/promises"
import { join } from "path"


export const partOne = async (value: string) => {
    let score = 0

    const cards: string[] = (await readFile(join(import.meta.dir, '..', 'data', value), 'utf-8')).split('\n')
    for (const card of cards) {
        let cardScore = 0
        const [_, numbers] = card.split(':')
        const [winningNumbers, playingNumbers] = numbers.split('|').map(str => str.trim().split(' ').filter(str => str !== ''))
        for (const number of winningNumbers) {
            if (playingNumbers.includes(number)) {
                cardScore > 0 ? cardScore = cardScore * 2 : cardScore = 1
            }
        }
        score += cardScore
    }

    return score
}

export const partTwo = async (value: string) => {
    const fileContent: string[] = (await readFile(join(import.meta.dir, '..', 'data', value), 'utf-8')).split('\n')

    const cards: {
        winning: string[],
        playing: string[],
        copies: number
    }[] = []

    for (const line of fileContent) {
        const [_, numbers] = line.split(':')
        const [winningNumbers, playingNumbers] = numbers.split('|').map(str => str.trim().split(' ').filter(str => str !== ''))
        cards.push({
            copies: 1,
            winning: winningNumbers,
            playing: playingNumbers
        })
    }

    for (let i = 0; i < cards.length; i++) {
        const card = cards[i];
        let score = 0
        for (const number of card.winning) {
            if (card.playing.includes(number)) {
                score += 1
            }
        }

        for (let index = i + 1; index < Math.min(i + score + 1, cards.length - 1); index++) {
            cards[index].copies += card.copies
        }

    }

    return cards.reduce((acc, card) => acc + card.copies, 0)
}

if (import.meta.main) {
    console.log(await partOne('test.txt'))
}

