from math import ceil  # Zaokrouhlení daně nahoru
from abc import ABC, abstractmethod  # BONUS 2 – abstraktní třída
from enum import Enum  # BONUS 4 – výčtové typy (enum)


# === BONUS 4 ===
# Výčet typů pozemků
class EstateType(Enum):
    LAND = "land"
    BUILDING_SITE = "building site"
    FORREST = "forrest"
    GARDEN = "garden"


# Lokalita, kde se nemovitost nachází
class Locality:
    def __init__(self, name, locality_coefficient):
        self.name = name
        self.locality_coefficient = locality_coefficient


# === BONUS 2 ===
# Abstraktní třída – základ pro všechny typy nemovitostí
class Property(ABC):
    def __init__(self, locality):
        self.locality = locality

    @abstractmethod
    def calculate_tax(self):
        pass


# Třída pro pozemky – dědí z Property
class Estate(Property):
    def __init__(self, locality, estate_type: EstateType, area):
        if not isinstance(estate_type, EstateType):
            raise ValueError("estate_type musí být instance typu EstateType")
        super().__init__(locality)
        self.estate_type = estate_type
        self.area = area

    def calculate_tax(self):
        type_coefficients = {
            EstateType.LAND: 0.85,
            EstateType.BUILDING_SITE: 9,
            EstateType.FORREST: 0.35,
            EstateType.GARDEN: 2
        }

        type_coef = type_coefficients[self.estate_type]
        loc_coef = self.locality.locality_coefficient
        tax = self.area * type_coef * loc_coef
        return ceil(tax)

    def __str__(self):
        return (
            f"{self.estate_type.value.capitalize()}, lokalita {self.locality.name} "
            f"(koeficient {self.locality.locality_coefficient}), "
            f"{self.area} metrů čtverečních, daň {self.calculate_tax()} Kč"
        )


# Třída pro stavby – dědí z Property
class Residence(Property):
    def __init__(self, locality, area, commercial):
        super().__init__(locality)
        self.area = area
        self.commercial = commercial

    def calculate_tax(self):
        base_tax = self.area * self.locality.locality_coefficient * 15
        return base_tax * 2 if self.commercial else base_tax

    def __str__(self):
        return (
            f"Nemovitost, lokalita {self.locality.name} (koeficient {self.locality.locality_coefficient}), "
            f"{self.area} m², komerční: {'Ano' if self.commercial else 'Ne'}, "
            f"daň {self.calculate_tax()} Kč"
        )


# === BONUS 3 ===
# Daňové přiznání obsahující více nemovitostí
class TaxReport:
    def __init__(self, name):
        self.name = name
        self.property_list = []

    def add_property(self, property_obj):
        self.property_list.append(property_obj)

    def calculate_tax(self):
        return sum(p.calculate_tax() for p in self.property_list)

    def __str__(self):
        result = f"Daňové přiznání: {self.name}\n"
        result += "\n".join(str(p) for p in self.property_list)
        result += f"\nCelková daň: {self.calculate_tax()} Kč"
        return result


# === TESTOVACÍ DATA ===

manetin = Locality("Manětín", 0.8)
brno = Locality("Brno", 3.0)

estate = Estate(locality=manetin, estate_type=EstateType.LAND, area=900)
residence_house = Residence(locality=manetin, area=120, commercial=False)
residence_office = Residence(locality=brno, area=90, commercial=True)

print(estate)
print(residence_house)
print(residence_office)

# BONUS 2: pokus o vytvoření instance abstraktní třídy
try:
    invalid_property = Property(manetin)
except TypeError as e:
    print("Správně vyvolána chyba při pokusu o vytvoření abstraktní třídy Property:")
    print(e)

# BONUS 3: daňové přiznání
report = TaxReport("Tereza K.")
report.add_property(estate)
report.add_property(residence_house)
report.add_property(residence_office)

print()
print(report)
