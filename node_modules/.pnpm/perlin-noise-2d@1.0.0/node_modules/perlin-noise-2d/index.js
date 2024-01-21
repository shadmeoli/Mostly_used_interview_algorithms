import seedrandom from 'seedrandom';
const { alea } = seedrandom;
const smoothstep = (x) => x * x * x * (x * (x * 6 - 15) + 10);
const interpolation = (a, b, t) => a + (b - a) * smoothstep(t);
const dotProduct = (a, b) => a[0] * b[0] + a[1] * b[1];
export default class PerlinNoise {
    constructor(width, height, seed = Math.floor(Math.random() * 4294967296)) {
        this.random = alea(seed.toString());
        this.vectors = this._createVectorField(width, height);
    }
    _dotProdGrid(x, y, cellX, cellY) {
        const vector = this.vectors[cellY][cellX];
        const distVector = [x - cellX, y - cellY];
        return dotProduct(vector, distVector);
    }
    _createRandomVector() {
        const random = this.random() * Math.PI * 2;
        return [Math.cos(random), Math.sin(random)];
    }
    _createVectorField(width, height) {
        return Array(height + 1)
            .fill([])
            .map(() => Array(width + 1)
            .fill(0)
            .map(() => this._createRandomVector()));
    }
    perlin(x, y) {
        const [x0, y0] = [Math.floor(x), Math.floor(y)];
        const [x1, y1] = [x0 + 1, y0 + 1];
        const corners = [this._dotProdGrid(x, y, x0, y0), this._dotProdGrid(x, y, x1, y0), this._dotProdGrid(x, y, x0, y1), this._dotProdGrid(x, y, x1, y1)];
        return interpolation(interpolation(corners[0], corners[1], x - x0), interpolation(corners[2], corners[3], x - x0), y - y0);
    }
}
