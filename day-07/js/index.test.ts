import { expect, test, describe } from "bun:test";
import { partOne, partTwo } from ".";

describe("day 07", () => {
  test("part 1", async () => {
    expect(partOne("test.txt")).resolves.toBe(6440);
  });

  test("part 1 solution", () => {
    expect(partOne("input.txt")).resolves.toBe(250898830);
  });
  test("part 2", async () => {
    expect(partTwo("test.txt")).resolves.toBe(5905);
  });

  test("part 2 solution", () => {
    expect(partTwo("input.txt")).resolves.toBe(252127335);
  });
});
