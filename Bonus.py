from abc import ABC, abstractmethod


class Galaxy(ABC):
    def __init__(
        self,
        name,
        radius_in_m,
        mass_in_kg,
        mean_temperature_in_celsius,
        age_in_years,
        number_of_stars,
    ):
        self.__name = name
        self.__radius_in_m = radius_in_m
        self.__mass_in_kg = mass_in_kg
        self.__mean_temperature_in_celsius = mean_temperature_in_celsius
        self.__age_in_years = age_in_years
        self.__number_of_stars = number_of_stars

    @abstractmethod
    def galaxy_type(self):
        """Return the type of galaxy."""
        pass

    def summary(self):
        return (
            f"{self.__name} ({self.galaxy_type()} galaxy)\n"
            f"Radius: {self.__radius_in_m:.2e} m\n"
            f"Mass: {self.__mass_in_kg:.2e} kg\n"
            f"Mean temperature: {self.__mean_temperature_in_celsius} °C\n"
            f"Age: {self.__age_in_years:,} years\n"
            f"Number of stars: {self.__number_of_stars:,}"
        )

    def diameter_in_m(self):
        return 2 * self.__radius_in_m

    def add_stars(self, count):
        if count <= 0:
            raise ValueError("The number of stars to add must be positive.")
        self.__number_of_stars += count


class SpiralGalaxy(Galaxy):
    def galaxy_type(self):
        return "spiral"


class EllipticalGalaxy(Galaxy):
    def galaxy_type(self):
        return "elliptical"


galaxies = [
    SpiralGalaxy("Aurora", 4.7e20, 2.0e42, -200, 10_000_000_000, 200_000_000_000),
    EllipticalGalaxy("Orion", 6.0e20, 3.0e42, -180, 12_000_000_000, 500_000_000_000),
]

for galaxy in galaxies:
    print(galaxy.summary())
    print()