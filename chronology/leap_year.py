"""Leap Year utility."""

# Standard library

#3rd party library

#project library


def is_leap_year(year: int) -> bool:
    """Determine if year is a leap year."""
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True
