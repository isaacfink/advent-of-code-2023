import { readFile } from "fs/promises"
import { join } from "path"

export const partOne = async (value: string) => {
    const maxCounts = {
        blue: 14,
        green: 13,
        red: 12
    }
    const fileContents = await readFile(join(import.meta.dir, '..', 'data', value), 'utf-8')

    let score = 0
    const games = fileContents.split('\n')
    games.forEach(game => {
        let [id, moves] = game.split(':')
        id = id.trim().split('Game ')[1]
        let rounds = moves.split(';').map(move => move.trim())
        let gameIsPossible = true
        rounds.forEach(round => {
            const cubes = round.split(',').map(cube => cube.trim())
            cubes.forEach(cube => {
                const [count, color] = cube.split(' ')
                // @ts-ignore
                if (maxCounts[color] < parseInt(count)) {
                    gameIsPossible = false
                }
            })
        })
        if (gameIsPossible) {
            score += parseInt(id)
        }
    })

    return score
}

export const partTwo = async (value: string) => {
    const fileContents = await readFile(join(import.meta.dir, '..', 'data', value), 'utf-8')

    let score = 0
    const games = fileContents.split('\n')
    games.forEach(game => {
        let maxCounts = {
            blue: 0,
            green: 0,
            red: 0
        }
        let [id, moves] = game.split(':')
        let rounds = moves.split(';').map(move => move.trim())
        rounds.forEach(round => {
            const cubes = round.split(',').map(cube => cube.trim())
            cubes.forEach(cube => {
                const [count, color] = cube.split(' ')
                // @ts-ignore
                maxCounts[color] = Math.max(maxCounts[color], parseInt(count))

            })
        })
        score += (maxCounts.blue * maxCounts.green * maxCounts.red)
    })

    return score
}
