import { readFile } from "fs/promises"
import { join } from "path"

export const partOne = async (value: string) => {
    const fileContents = await readFile(join(import.meta.dir, '..', 'data', value), 'utf-8')

    let score = 0
    const lines = fileContents.split('\n')
    lines.forEach(line => {
        const digits = line.split('').filter(char => !Number.isNaN(parseInt(char)))
        score += parseInt(`${digits[0]}${digits[digits.length - 1]}}`)
    })
    return score
}

export const partTwo = async (value: string) => {
    const mapper = {
        one: 1,
        two: 2,
        three: 3,
        four: 4,
        five: 5,
        six: 6,
        seven: 7,
        eight: 8,
        nine: 9,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9
    }

    const re = /(one|two|three|four|five|six|seven|eight|nine|[1-9])/g
    const fileContents = await readFile(join(import.meta.dir, '..', 'data', value), 'utf-8')

    let score = 0
    const lines = fileContents.split('\n')
    lines.forEach(line => {
        const matches: string[] = [];

        for (let i = 0; i < line.length; i++) {
            for (const match of line.slice(i).matchAll(re)) {
                if (match[1]) {
                    matches.push(match[1]);
                }
            }
        }

        // @ts-ignore
        const first = mapper[matches[0]]
        // @ts-ignore
        const second = mapper[matches[matches.length - 1]]

        score += parseInt(`${first}${second}`)

    })
    return score
}