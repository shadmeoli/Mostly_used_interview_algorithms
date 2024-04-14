/**
 * I am trying to learn the concepts of:
 * [ ] dunder methods
 * [ ] cls methods
 * [ ] self methods
 * [ ] walrus methods
 * [ ] how to avoid reference counting and also circular imports
 * [ ] Decorator pattern with classes
 * [ ] Instance and class methods
 */
import java.util.function.BiConsumer;
import java.util.function.Consumer;
import java.util.function.Function;

class Decorator<T, U> {
    private Function<T, U> func;
    private T args;

    public Decorator(Function<T, U> f, T a) {
        this.func = f;
        this.args = a;
    }

    public void call(T... rest) {
        T result = memoize();
        Consumer<T[]> wrapper_function = () -> {
            func.apply(result);
        };
        wrapper_function.accept(rest);
    }

    private T memoize() {
        return args;
    }
}

// Example usage
public class Main {
    public static void myFunction(Integer a) {
        System.out.println("Value: " + a);
    }

    public static void main(String[] args) {
        Decorator<Integer, Void> decorator = new Decorator<>(Main::myFunction, 10);
        decorator.call(20);
    }
}

