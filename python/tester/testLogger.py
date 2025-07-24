import time
from functools import wraps

import click
from rich.console import Console
from rich.spinner import Spinner
from rich.table import Table

console = Console()


def test_runner(expected, assert_is_array=False, message=None):
    """
    Decorator to run function tests with expected values.

    Args:
        expected: single expected value or list of expected values
        assert_is_array: True if testing with arrays of test inputs
        message: Optional custom message to show with each test
    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            test_cases = args[0] if assert_is_array else [args]
            expected_values = expected if isinstance(expected, list) else [expected]

            passed = 0
            total = len(test_cases)
            results = []

            with console.status("[bold green]Running tests...", spinner="dots"):
                time.sleep(0.3)  # spinner delay for aesthetics
                for i, test_input in enumerate(test_cases):
                    try:
                        output = (
                            func(test_input)
                            if assert_is_array
                            else func(*args, **kwargs)
                        )
                        is_pass = output == expected_values[i]
                        results.append(
                            {
                                "input": test_input,
                                "expected": expected_values[i],
                                "output": output,
                                "pass": is_pass,
                                "msg": message or f"Test case #{i + 1}",
                            }
                        )
                        passed += int(is_pass)
                    except Exception as e:
                        results.append(
                            {
                                "input": test_input,
                                "expected": expected_values[i],
                                "output": f"Error: {e}",
                                "pass": False,
                                "msg": message or f"Test case #{i + 1}",
                            }
                        )

            # Output table
            table = Table(title="Test Results Summary")
            table.add_column("Test", justify="center")
            table.add_column("Input", style="cyan")
            table.add_column("Expected", style="magenta")
            table.add_column("Output", style="yellow")
            table.add_column("Result", style="bold")

            for idx, res in enumerate(results):
                table.add_row(
                    res["msg"],
                    str(res["input"]),
                    str(res["expected"]),
                    str(res["output"]),
                    "[green]PASS[/green]" if res["pass"] else "[red]FAIL[/red]",
                )

            console.print(table)
            console.print(f"[bold blue]Passed {passed}/{total} tests[/bold blue]")

        return wrapper

    return decorator
