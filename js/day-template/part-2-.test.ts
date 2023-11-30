import { expect, test } from 'bun:test'
import { main } from './part-2'

test('part 2 test', () => {
    expect(main(2)).toBe(4)
})
