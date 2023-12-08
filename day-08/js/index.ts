import { readFile } from "fs/promises";
import { join } from "path";

const instructionsMap: Record<string, number> = {
  L: 0,
  R: 1,
};

export const partOne = async (value: string) => {
  let steps = 0;

  const rounds: string[] = (
    await readFile(join(import.meta.dir, "..", "data", value), "utf-8")
  ).split("\n");

  const instructions: string[] = rounds[0].split("");

  let map: Record<string, [string, string]> = {};

  for (let i = 2; i < rounds.length; i++) {
    const [key, value] = rounds[i].split(" = ");
    const parsedValues = value.split(", ").map((v) => {
      return v.replace(")", "").replace("(", "");
    });
    map[key] = [parsedValues[0], parsedValues[1]];
  }

  let position: string = "AAA";
  while (true) {
    if (position == "ZZZ") {
      break;
    }
    let move = instructions[steps % instructions.length];
    position = map[position][instructionsMap[move]];
    steps++;
  }

  return steps;
};

function gcd(a: number, b: number) {
  while (b !== 0) {
    let t = b;
    b = a % b;
    a = t;
  }
  return a;
}

function lcm(a: number, b: number) {
  return (a * b) / gcd(a, b);
}

function lcmOfList(list: number[]) {
  let result = list[0];
  for (let i = 1; i < list.length; i++) {
    result = lcm(result, list[i]);
  }
  return result;
}

export const partTwo = async (value: string) => {
  let steps = 0;

  const rounds: string[] = (
    await readFile(join(import.meta.dir, "..", "data", value), "utf-8")
  ).split("\n");

  const instructions: string[] = rounds[0].split("");

  let map: Record<string, [string, string]> = {};

  for (let i = 2; i < rounds.length; i++) {
    const [key, value] = rounds[i].split(" = ");
    const parsedValues = value.split(", ").map((v) => {
      return v.replace(")", "").replace("(", "");
    });
    map[key] = [parsedValues[0], parsedValues[1]];
  }

  const positions = Object.keys(map);

  let startingPositions = positions.filter((p) => p[2] == "A");
  let scores: number[] = [];

  for (let pos of startingPositions) {
    let localStep = 0;
    while (true) {
      if (pos[2] == "Z") {
        scores.push(localStep);
        break;
      }
      let move = instructions[localStep % instructions.length];
      pos = map[pos][instructionsMap[move]];
      localStep++;
    }
  }

  return lcmOfList(scores);
};
