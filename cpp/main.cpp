#include <iostream>
#include <tuple>
#include <functional>

template<typename Func, typename... Args>
class Decorator {
private:
    Func func;
    std::tuple<Args...> args;

public:
    Decorator(Func f, Args... a) : func(f), args(std::make_tuple(a...)) {}

    template<typename... Rest>
    void operator()(Rest... rest) {
        auto result = memoize();
        auto wrapper_function = [this, result, rest...](){
            std::apply(func, std::tuple_cat(result, std::make_tuple(rest...)));
        };
        wrapper_function();
    }

private:
    std::tuple<Args...> memoize() {
        return args;
    }
};

// Example usage
void my_function(int a, int b) {
    std::cout << "Sum: " << a + b << std::endl;
}

int main() {
    Decorator<decltype(my_function), int, int> decorator(my_function, 10, 20);
    decorator(30);
    return 0;
}

