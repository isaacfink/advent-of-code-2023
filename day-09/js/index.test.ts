import { expect, test, describe } from "bun:test";
import { partOne, partTwo } from ".";

describe("day 08", () => {
  test("part 1", async () => {
    expect(partOne("test.txt")).resolves.toBe(2);
  });

  test("part 1 test 2", () => {
    expect(partOne("test2.txt")).resolves.toBe(6);
  });
  test("part 1 solution", async () => {
    expect(partOne("input.txt")).resolves.toBe(13939);
  });

  test("part 2", () => {
    expect(partTwo("testPart2.txt")).resolves.toBe(6);
  });

  test("part 2 solution", () => {
    expect(partTwo("input.txt")).resolves.toBe(8906539031197);
  });
});
