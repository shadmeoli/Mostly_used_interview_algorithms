package tester

type Test struct{}

func NewTestRunner() *Test {
	return &Test{}
}

type Runner[T any] struct {
	Expected      T
	AssertIsArray bool
	Message       string
}

func (t *Test) Run(
	Expected any,
	AssertIsArray bool,
	Message string,
	args ...any,
) {
	// var passed int
	// var total int
	// var results []any

	if AssertIsArray {
		// for asser := range Expected {
		// 	//
		// }
	}

}
