"""Module to run calculator."""

from calculator import Calculator


def main():
    """Perform basic arithmetic operations."""
    calculator = Calculator()

    result = calculator.add(7, 5)
    print("7 + 5 =", result)

    result = calculator.subtract(34, 21)
    print("34 - 21 =", result)

    result = calculator.multiply(54, 2)
    print("54 * 2 =", result)

    result = calculator.divide(144, 2)
    print("144 / 2 =", result)

    result = calculator.divide(45, 10)
    print("45 / 10 =", result)


if __name__ == "__main__":
    main()
