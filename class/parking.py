def park_car(parking: list, plate: str):
    parking.append(plate)
    return parking
    
def unpark_car(parking: list, plate: str) -> bool:
    if parking[-1] == plate:
        parking.pop(-1)
        return True
    else:
        return False


def get_last(parking: list) -> str | None:
    return parking[-1]


parking = []

park_car(parking, "CA1285KH")

park_car(parking, "CB4567KA")

unpark_car(parking, "CB1285KH")

last = get_last(parking)
unpark_car(parking, last)

