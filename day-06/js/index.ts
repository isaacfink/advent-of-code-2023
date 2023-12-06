import { readFile } from "fs/promises"
import { join } from "path"


export const partOne = async (value: string) => {
    let score = 0

    const rounds: string[] = (await readFile(join(import.meta.dir, '..', 'data', value), 'utf-8')).split('\n')
    const times = rounds[0].split(':')[1].trim().split(' ').map(str => parseInt(str)).filter(str => !isNaN(str))
    const scores = rounds[1].split(':')[1].trim().split(' ').map(str => parseInt(str)).filter(str => !isNaN(str))

    for (let i = 0; i < times.length; i++) {
        const timeToBeat = times[i]
        const scoreToBeat = scores[i]
        let possibleMethods: number = 0
        for (let j = 0; j < timeToBeat; j++) {
            const achievedScore = j * (timeToBeat - j)
            if (achievedScore > scoreToBeat) {
                possibleMethods += 1
            }

        }
        score = score === 0 ? possibleMethods : score * possibleMethods
    }


    return score
}

export const partTwo = async (value: string) => {
    let score = 0

    const rounds: string[] = (await readFile(join(import.meta.dir, '..', 'data', value), 'utf-8')).split('\n')
    const times = parseInt(rounds[0].split(':')[1].trim().replaceAll(' ', ''))
    const scores = parseInt(rounds[1].split(':')[1].trim().replaceAll(' ', ''))

    let lowestPossible = 0
    let highestPossible = 0

    for (let i = 0; i < times; i++) {
        const achievedScore = i * (times - i)
        if (achievedScore > scores) {
            lowestPossible = i
            break
        }
    }

    for (let i = times; i > 0; i--) {
        const achievedScore = i * (times - i)
        if (achievedScore > scores) {
            highestPossible = i
            break
        }
    }

    score = highestPossible - lowestPossible + 1


    return score
}


