import { expect, test, describe } from 'bun:test'
import { partOne, partTwo } from '.'

describe('day 01', () => {


    test('part 1', async () => {
        expect(await partOne('test.txt')).toBe(142)
    })
    test('part 2', async () => {
        expect(await partTwo('test-part-2.txt')).toBe(281)
    })
}
)

