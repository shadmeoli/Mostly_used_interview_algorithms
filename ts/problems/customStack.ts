class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

class Stack {
  constructor() {
    this.top = null;
    this.count = 0;
  }

  push(value) {
    // Add value to stack
    const newNode = new Node(value);
    newNode.next = this.top;
    this.top = newNode;
    this.count++;
  }

  pop() {
    if (this.isEmpty()) return -1;
    const popped = this.top.value;
    this.top = this.top.next;
    this.count--;
    return popped;
  }

  peek() {
    // Return the top value without removing it
    if (this.isEmpty()) return -1;
    return this.top.value;
  }

  isEmpty() {
    // Return true if the stack is empty
    return this.top === null;
  }

  size() {
    // Return the number of elements in the stack
    return this.count;
  }
}

const stack = new Stack();
stack.push(10);
stack.push(20);
console.log(stack.peek()); // Output: 20
console.log(stack.pop()); // Output: 20
console.log(stack.size()); // Output: 1
console.log(stack.isEmpty()); // Output: false
console.log(stack.pop()); // Output: 10
console.log(stack.isEmpty()); // Output: true
