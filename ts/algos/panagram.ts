function identifyPanagram(test_string: String): boolean {
  const alpha = Array.from(Array(26)).map((e, i) => i + 65);
  const alphabet: string[] = alpha.map((x) => String.fromCharCode(x));
  const ourSentence = new Set(test_string.split(" ").join());
  if (ourSentence.size < alphabet.length) {
    return false;
  } else {
    return true;
  }
}

let shouldBeTrue = identifyPanagram(
  "The quick brown fox jumps over the lazy dog",
);
let shouldBeFalse = identifyPanagram("Hello world");
let otherTest = identifyPanagram("abcdefgh");

console.log(`Test 1 was ${shouldBeTrue}`);
console.log(`Test 2 was ${shouldBeFalse}`);
