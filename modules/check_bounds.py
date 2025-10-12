def parse_bounds(
    bounds: int | float | tuple[float, float] | tuple[int, int],
    default: tuple[int, int],
) -> tuple[float, float]:
    """
    Convert input bounds (number or tuple) into a uniform (start, end) tuple.

    Arguments:
    bounds (int | float | tuple[int, int] | tuple[float, float]): The user-provided boundary values.
    default (tuple[float, float]): The default bounds to use if the input type is invalid.

    Return:
    tuple[float, float]: A pair of numeric bounds in the form (start, end).
    """
    if isinstance(bounds, (int, float)):
        return 0, bounds
    if isinstance(bounds, (tuple)):
        return bounds
    else:
        return default
