package main

import "fmt"

type Node struct {
	Value int
	Next  *Node
}

type Stack struct {
	top  *Node
	size int
}

func NewStack() *Stack {
	return &Stack{}
}

func (s *Stack) push(value int) {
	newNode := &Node{Value: value, Next: s.top}
	s.top = newNode
	s.size++
}

func (s *Stack) pop() int {
	if s.isEmpty() {
		fmt.Println("Stack is empty")
		return -1
	}
	poppedValue := s.top.Value
	s.top = s.top.Next
	s.size--
	return poppedValue
}

func (s *Stack) peek() int {
	if s.isEmpty() {
		return -1
	}
	return s.top.Value
}

func (s *Stack) isEmpty() bool {
	return s.top == nil
}

func main() {
	stack := NewStack()
	fmt.Println(stack.top)  // nil
	fmt.Println(stack.size) // 0

	stack.push(10)
	stack.push(20)
	fmt.Println(stack.top.Value) // 20
	fmt.Println(stack.size)      // 2

	fmt.Println(stack.pop())     // 20
	fmt.Println(stack.top.Value) // 10
	fmt.Println(stack.size)      // 1

	fmt.Printf("%v\n", stack.isEmpty()) // false
	fmt.Println(stack.peek())           // 10
}
