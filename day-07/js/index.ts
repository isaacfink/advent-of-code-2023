import { readFile } from "fs/promises";
import { join } from "path";

const handScores = {
  A: "13",
  K: "12",
  Q: "11",
  J: "10",
  T: "09",
  "9": "08",
  "8": "07",
  "7": "06",
  "6": "05",
  "5": "04",
  "4": "03",
  "3": "02",
  "2": "01",
  "*": "00",
};

const hands = Object.keys(handScores);

const handTypesScores = {
  five_of_a_kind: "7",
  four_of_a_kind: "6",
  full_house: "5",
  three_of_a_kind: "4",
  two_pairs: "3",
  two_of_a_kind: "2",
  distinct: "1",
};

const handTypes = Object.keys(handTypesScores);

const getHandType: (hl: string[]) => (typeof handTypes)[number] = (hl) => {
  let matches: number[] = [];

  const distinct = [...new Set(hl)];
  for (const h of distinct) {
    matches.push(hl.filter((x) => x === h).length);
  }

  let countOfFive = matches.filter((x) => x === 5).length;
  let countOfFour = matches.filter((x) => x === 4).length;
  let countOfThree = matches.filter((x) => x === 3).length;
  let countOfTwo = matches.filter((x) => x === 2).length;

  if (countOfFive === 1) {
    return handTypes[0];
  } else if (countOfFour === 1) {
    return handTypes[1];
  } else if (countOfThree === 1 && countOfTwo === 1) {
    return handTypes[2];
  } else if (countOfThree === 1) {
    return handTypes[3];
  } else if (countOfTwo === 2) {
    return handTypes[4];
  } else if (countOfTwo === 1) {
    return handTypes[5];
  } else {
    return handTypes[6];
  }
};

function getScoreForHand(hand: string, originalHand: string) {
  const h = hand.split("");
  const oh = originalHand.split("");
  // @ts-ignore
  let fs = handTypesScores[getHandType(h)];

  for (let i = 0; i < oh.length; i++) {
    // @ts-ignore
    fs += handScores[oh[i]];
  }

  return parseInt(fs);
}

function cartesianProduct(arr: string[], repeat: number): string[][] {
  let result: string[][] = [];
  let f = function (prefix: string[], arr: string[], n: number) {
    if (n === 0) {
      result.push(prefix);
      return;
    }
    for (let i = 0; i < arr.length; i++) {
      f(prefix.concat(arr[i]), arr, n - 1);
    }
  };
  f([], arr, repeat);
  return result;
}

function getJokerReplacements(hand: string): [string, string][] {
  let jokerPositions: number[] = [];
  Array.from(hand).forEach((char, pos) => {
    if (char === "J") jokerPositions.push(pos);
  });

  let possibleReplacements: [string, string][] = [];
  let product = cartesianProduct(hands, jokerPositions.length);
  product.forEach((replacement) => {
    let newHand = Array.from(hand);
    replacement.forEach((rep, index) => {
      newHand[jokerPositions[index]] = rep;
    });
    possibleReplacements.push([newHand.join(), hand.replace(/J/g, "*")]);
  });

  return possibleReplacements;
}

function getHighestScore(hands: string[][]) {
  let highestScore = 0;
  for (const hand of hands) {
    let score = getScoreForHand(hand[0], hand[1]);
    if (score > highestScore) highestScore = score;
  }

  return highestScore;
}

export const partOne = async (value: string) => {
  let score = 0;

  const rounds: string[] = (
    await readFile(join(import.meta.dir, "..", "data", value), "utf-8")
  ).split("\n");
  const sortedRounds = rounds.sort((a, b) => {
    const aScore = getScoreForHand(a.split(" ")[0], a.split(" ")[0]);
    const bScore = getScoreForHand(b.split(" ")[0], b.split(" ")[0]);
    return bScore - aScore;
  });

  for (let i = 0; i < sortedRounds.length; i++) {
    score += (i + 1) * parseInt(sortedRounds[i].split(" ")[1]);
  }

  return score;
};

export const partTwo = async (value: string) => {
  let score = 0;

  const rounds: string[] = (
    await readFile(join(import.meta.dir, "..", "data", value), "utf-8")
  ).split("\n");
  const sortedRounds = rounds.sort((a, b) => {
    const aScore = getHighestScore(getJokerReplacements(a.split(" ")[0]));
    const bScore = getHighestScore(getJokerReplacements(b.split(" ")[0]));
    return bScore - aScore;
  });

  for (let i = 0; i < sortedRounds.length; i++) {
    score += (i + 1) * parseInt(sortedRounds[i].split(" ")[1]);
  }

  return score;
};
