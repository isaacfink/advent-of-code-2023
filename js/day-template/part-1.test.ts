import { expect, test } from 'bun:test'
import { main } from './part-1'

test('part 1 test', () => {
    expect(main(2)).toBe(4)
})

