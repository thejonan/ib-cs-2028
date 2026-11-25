def park_car(parking: list, plate: str):
    parking.append[plate]

def unpark_car(parking: list, plate: str) -> bool:
    if get_last(parking) == plate:
      parking.pop()
      return True
    else:
      return False
    

def get_last(parking: list) -> str | None:
    if len(parking) > 0:
      last = parking[-1]
      return last
    else:
      return None

parking = []

park_car(parking, "CA1285KH")

park_car(parking, "CB4567KA")

unpark_car(parking, "CB1285KH")

last = get_last(parking)
unpark_car(parking, last)
