import PerlinNoise from "perlin-noise-2d";
const perlin = new PerlinNoise(8, 12); // Width is 8, Height is 12

perlin.perlin(4.5, 2.5);
console.log(perlin);
