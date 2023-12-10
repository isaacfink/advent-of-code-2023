import { expect, test, describe } from "bun:test";
import { partOne, partTwo } from ".";

describe("day 09", () => {
  test("part 1", async () => {
    expect(partOne("test.txt")).resolves.toBe(114);
  });

  // test("part 1 solution", async () => {
  //   expect(partOne("input.txt")).resolves.toBe(1681758908);
  // });

  // test("part 2", () => {
  //   expect(partTwo("test.txt")).resolves.toBe(2);
  // });

  // test("part 2 solution", () => {
  //   expect(partTwo("input.txt")).resolves.toBe(803);
  // });
});
