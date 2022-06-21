def main(a):
    """Check the natural number.Natural numbers are numbers used in counting.
    Args:
        a: int
    Returns:
        bool
    """
    # Write your code here
    return a > 1 and a % 2 == 0
print(main(4))