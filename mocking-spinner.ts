/**
 * Create a function to mock a spinner.
 * The spinner runs clock wise:
 *            - 1 represent the cell to turn / active cell
 *            - 0 represent the other cells
 *
 * The duration of the each cell should be 1 sec for a full cycle.
 * do this in typescript and if possible incorporate classes.
 
 * */
class Spinner {
  cells: any
  duration: number
  constructor(public cycles: number) {
    this.cells = [[0, 1], [0, 0], [0, 0]];
    this.duration = 0;
    this.cycles = cycles;
  }

  /**
   * start
   */
  public start() {
    let cycle = this.cells.length;
    let width = this.cells[0].length;

    for (let i = 0; i < this.cycles; i++) {
      for (let j = 0; j < width; i++) {
        if (this.cells[i][j] === 1) {
          let prev = this.cells[i][j];
          this.cells[i][j + 1] = 1;
          this.cells[i][j] = 0;
        } 
      }
    }

    return this.cycles;
  }
}

let val = new Spinner(2);
console.log(val.start());
