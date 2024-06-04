"""Basic calculator."""


class Calculator:
    """Class that performs basic arithmetic operations."""

    def add(self, x: float, y: float):
        """A method for addition that takes two arguments and returns their sum.

        Parameters
        ----------
        x: float
            First summand.
        y: float
            Second summand.
            
        Returns
        -------
        float
            Sum of the arguments.
        """
        return x + y

    def subtract(self, x: float, y: float):
        """A method for subtraction that takes two arguments and returns their difference.

        Parameters
        ----------
        x: float
            Minuend.
        y: float
            Subtrahend.

        Returns
        -------
        float
            Difference between arguments.
        """
        return x - y

    def multiply(self, x: float, y: float):
        """A method for multiplication that takes two arguments and returns their product.

        Parameters
        ----------
        x: float
            Multiplicand.
        y: float
            Multiplier.

        Returns
        -------
        float
            Product.
        """
        return x * y

    def divide(self, x: float, y: float):
        """A method for division.

        It takes two arguments and returns the result if the denominator is not zero,
        or raises an ValueError if the denominator is zero

        Parameters
        ----------
        x: float
            Numerator.
        y: float
            Denominator.

        Returns
        -------
        float
            Quotient.
        """
        assert y != 0, "Invalid Operation"
        return x / y
