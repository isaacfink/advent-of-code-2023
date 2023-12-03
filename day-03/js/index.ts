import { readFile } from "fs/promises"
import { join } from "path"

const digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
function getNumbersInRow(row: string[]) {
    let index = 0
    let isPart: boolean = false
    let parts: [number, number][] = []
    while (index < row.length) {
        const char = parseInt(row[index])
        if (digits.indexOf(char) >= 0 && !isPart) {
            parts.push([index, index])
            isPart = true
        } else if (digits.indexOf(char) >= 0 && isPart) {
            parts[parts.length - 1][1] = index
        } else {
            isPart = false
        }
        index++
    }

    return parts
}

export const partOne = async (value: string) => {
    let score = 0

    const readings: string[][] = (await readFile(join(import.meta.dir, '..', 'data', value), 'utf-8')).split('\n').map(line => line.split(''))

    function lowerEnd(index: number) {
        return Math.max(0, index)
    }

    function higherEndRows(index: number) {
        return Math.min(readings[0].length - 1, index)
    }

    function higherEndCols(index: number) {
        return Math.min(readings.length - 1, index)
    }

    for (let fileIndex = 0; fileIndex < readings.length; fileIndex++) {
        const regex = /[^a-z0-9\.]/
        function isSymbol(str: string) {
            return regex.test(str)
        };
        const reading = readings[fileIndex];

        let parts = getNumbersInRow(reading)
        parts.forEach(part => {

            if (!part[1]) {
                console.log(part)
            }
            const start = lowerEnd(part[0] - 1)
            const end = higherEndRows(part[1] ? part[1] + 1 : 0)

            const toScan = [
                ...readings[lowerEnd(fileIndex - 1)].slice(start, end + 1),
                ...readings[fileIndex].slice(start, end + 1),
                ...readings[higherEndCols(fileIndex + 1)].slice(start, end + 1)
            ]


            if (isSymbol(toScan.join(''))) {
                score += parseInt(reading.slice(part[0], part[1] ? part[1] + 1 : 0).join(''))
            }
        })
    }


    return score
}

export const partTwo = async (value: string) => {
    const readings: string[][] = (await readFile(join(import.meta.dir, '..', 'data', value), 'utf-8')).split('\n').map(line => line.split(''))

    let score = 0

    let numbers: [number, number][][] = readings.map(line => getNumbersInRow(line))

    function getInRangeNumbersRow(index: number, row: [number, number][]) {
        return row.filter(number => {
            return number.some(num => Math.abs(num - index) <= 1)
        })
    }
    for (let fileIndex = 0; fileIndex < readings.length; fileIndex++) {
        const reading = readings[fileIndex];

        for (let i = 0; i < reading.length; i++) {
            const char = reading[i];
            if (char === '*') {
                const rowsIndexes = fileIndex == 0 ? [0, 1] : fileIndex === readings.length - 1 ? [fileIndex - 1, fileIndex] : [fileIndex - 1, fileIndex, fileIndex + 1]
                let adjacentNumbers: number[] = rowsIndexes.map(rowIndex => {
                    return getInRangeNumbersRow(i, numbers[rowIndex]).map(number => {
                        return parseInt(readings[rowIndex].slice(number[0], number[1] + 1).join(''))
                    })
                }).flat()


                if (adjacentNumbers.length == 2) {
                    score += (adjacentNumbers[0] * adjacentNumbers[1])
                }
            }
        }

    }

    return score
}

if (import.meta.main) {
    console.log(await partTwo('input.txt'))
}
