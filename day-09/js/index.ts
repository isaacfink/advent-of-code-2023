import { readFile } from "fs/promises";
import { join } from "path";

function getDifferences(list: number[]) {
  let differences = [];
  for (let i = 0; i < list.length - 2; i++) {
    differences.push(list[i + 1] - list[i]);
  }
  return differences;
}

export const partOne = async (value: string) => {
  let score = 0;

  const readings: string[] = (
    await readFile(join(import.meta.dir, "..", "data", value), "utf-8")
  ).split("\n");

  for (const reading of readings) {
    let readingSplit = reading.split(" ").map((r) => parseInt(r));
    let newReadings = [getDifferences(readingSplit)];

    while (true) {
      newReadings.push(getDifferences(newReadings[newReadings.length - 1]));
      if (newReadings.at(-1)?.every((r) => r == 0)) {
        break;
      }
    }

    let reversedNewReadings = newReadings.toReversed();
    for (let i = 1; i < reversedNewReadings.length; i++) {
      let values = reversedNewReadings[i];
      console.log(reversedNewReadings, values);
      let prevDiff = reversedNewReadings[i - 1].at(-1);
      console.log("prevDiff: ", prevDiff);
      values.push(values.at(-1)! + prevDiff!);
    }

    console.log(reversedNewReadings);

    score += readingSplit.at(-1)! + reversedNewReadings.at(-1)!.at(-1)!;
  }

  return score;
};

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
