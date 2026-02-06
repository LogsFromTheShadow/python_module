class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def arroser(litres):
    if litres < 0:
        raise WaterError("Impossible d'arroser avec une"
                         "quantité négative d'eau !")


try:
    arroser(-10)
except WaterError as e:
    print(f"erreur detecte: {e}")
