import { expect, test, describe } from 'bun:test'
import { partOne, partTwo } from '.'

describe('day 02', () => {
    test('part 1', async () => {
        expect(partOne('test.txt')).resolves.toBe(288)
    })

    test('part 1 solution', () => {
        expect(partOne('input.txt')).resolves.toBe(633080)
    })
    test('part 2', async () => {
        expect(partTwo('test.txt')).resolves.toBe(71503)
    })

    test('part 2 solution', () => {
        expect(partTwo('input.txt')).resolves.toBe(20048741)
    })
}
)

