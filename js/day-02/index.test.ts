import { expect, test, describe } from 'bun:test'
import { partOne, partTwo } from '.'

describe('day 02', () => {
    test('part 1', async () => {
        expect(await partOne('test.txt')).toBe(8)
    })
    test('part 2', async () => {
        expect(await partTwo('test.txt')).toBe(2286)
    })
}
)

