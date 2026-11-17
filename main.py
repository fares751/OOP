class Galaxy:
    def __init__(
        self,
        name,
        radius_in_m,
        mass_in_kg,
        mean_temperature_in_celsius,
        age_in_years,
        number_of_stars,
        galaxy_type,
    ):
        self.__name = name
        self.__radius_in_m = radius_in_m
        self.__mass_in_kg = mass_in_kg
        self.__mean_temperature_in_celsius = mean_temperature_in_celsius
        self.__age_in_years = age_in_years
        self.__number_of_stars = number_of_stars
        self.__galaxy_type = galaxy_type

    def summary(self):
        return (
            f"{self.__name} ({self.__galaxy_type} galaxy)\n"
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


galaxy = Galaxy(
    name="Aurora",
    radius_in_m=4.7e20,
    mass_in_kg=2.0e42,
    mean_temperature_in_celsius=-200,
    age_in_years=10_000_000_000,
    number_of_stars=200_000_000_000,
    galaxy_type="spiral",
)

galaxy.add_stars(1_000)

print(galaxy.summary())
print(f"Diameter: {galaxy.diameter_in_m():.2e} m")