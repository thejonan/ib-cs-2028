def park_car(parking: list, plate: str):
    pass


def unpark_car(parking: list, plate: str) -> bool:
    return False


def get_last(parking: list) -> str | None:
    return None


parking = []

park_car(parking, "CA1285KH")

park_car(parking, "CB4567KA")

unpark_car(parking, "CB1285KH")

last = get_last(parking)
unpark_car(parking, last)
