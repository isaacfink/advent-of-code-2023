import { expect, test, describe } from 'bun:test'
import { partOne, partTwo } from '.'

describe('day 02', () => {
    test('part 1', async () => {
        expect(partOne('test.txt')).resolves.toBe(13)
    })

    test('part 1 solution', () => {
        expect(partOne('input.txt')).resolves.toBe(28538)
    })
    test('part 2', async () => {
        expect(partTwo('test.txt')).resolves.toBe(30)
    })

    test('part 2 solution', () => {
        expect(partTwo('input.txt')).resolves.toBe(9425061)
    })
}
)

