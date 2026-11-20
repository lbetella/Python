def count(current: int, day: int) -> None:
    if current > day:
        return
    print("Day", current)
    count(current + 1, day)


def ft_count_harvest_recursive() -> None:
    day = int(input("Days until harvest: "))
    count(1, day)
    print("Harvest time!")
