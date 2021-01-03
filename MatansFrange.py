def frange(start: float, end: float, increments: float) -> tuple:
    """
    return values starting with start and ending with end, or less than end if another increment would exceed.
    """
    # print(round((start-end)/increments)+1)
    return tuple((round(start + increments*i, 5) for i in range(0, round((end-start)*((end-start)/increments))+2, 1) if start + increments*i <= end))
