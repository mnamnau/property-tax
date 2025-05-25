from math import ceil  # import pro zaokrouhlení daně nahoru (calculate_tax())

class Locality: # Definice třídy Locality, označuje lokalitu, kde se nemovitost nachází
    def __init__(self, name, locality_coefficient):
        self.name = name  # název katastru/obce
        self.locality_coefficient = locality_coefficient  # tzv. místní koeficient, který se používá k výpočtu daně
"""
manetin = Locality("Manětín", 0.8)
print("Název lokality:", manetin.name)
print("Koeficient lokality:", manetin.locality_coefficient)
"""
class Property: # bude reprezentovat nějakou nemovitost.
    def __init__(self, locality):
        self.locality = locality  # Lokalita, kde se nemovitost nachází, bude to objekt třídy Locality
"""
brno = Locality("Brno", 3.0)
# Vytvoření základní nemovitosti (pouze pro test)
some_property = Property(brno)
# Výpis údajů
print("Nemovitost se nachází v lokalitě:", some_property.locality.name)
print("Koeficient této lokality je:", some_property.locality.locality_coefficient)
"""
class Estate(Property):  # reprezentuje pozemek a je potomkem třídy Property
    def __init__(self, locality, estate_type, area):
        super().__init__(locality)  # volání konstruktoru rodičovské třídy
        self.estate_type = estate_type
        self.area = area

    def calculate_tax(self):  
        # Tento slovník slouží jako přehledné přiřazení koeficientů ke konkrétním typům pozemků.
        # Klíčem je typ pozemku (řetězec), hodnotou je číselný koeficient používaný při výpočtu daně.
        # Použití slovníku je efektivní způsob, jak nahradit dlouhý seznam if/elif podmínek.
        type_coefficients = {
            "land": 0.85,           # zemědělský pozemek
            "building site": 9,     # stavební pozemek
            "forrest": 0.35,        # les
            "garden": 2             # zahrada
        }
        # Získání správného koeficientu podle typu pozemku z atributu instance
        if self.estate_type not in type_coefficients:
            raise ValueError(f"Neznámý typ pozemku: {self.estate_type}")
        type_coef = type_coefficients[self.estate_type]  # koeficient pro daný typ pozemku
        loc_coef = self.locality.locality_coefficient    # místní koeficient z objektu Locality
        tax = self.area * type_coef * loc_coef # plocha pozemku * koeficient dle typu pozemku (atribut estate_type) * místní koeficient
        # Výsledná daň je zaokrouhlena nahoru na celé číslo
        return ceil(tax)
"""
# Testovací lokalita
manetin = Locality("Manětín", 0.8)
# Vytvoření instance pozemku typu "land"
estate = Estate(locality=manetin, estate_type="land", area=900)
# Výpočet a výpis daně
tax = estate.calculate_tax()
print("Vypočtená daň z pozemku:", tax)
"""
class Residence(Property): # reprezentuje byt, dům či jinou stavbu a je potomkem třídy Property
    def __init__(self, locality, area, commercial):
        super().__init__(locality)
        self.area = area
        self.commercial = commercial

    def calculate_tax(self): # spočítá výši daně pro byt a vrátí hodnotu jako číslo
        base_tax = self.area * self.locality.locality_coefficient * 15 # podlahová plocha * koeficient lokality * 1

        if self.commercial: # Pokud je hodnota parametru commercial True, tj. pokud jde o komerční nemovitost, vynásob celou daň číslem 2.
            return base_tax * 2
        else:
            return base_tax

# === Testovací data ===

# Lokalita Manětín s koeficientem 0.8
manetin = Locality("Manětín", 0.8)

# Lokalita Brno s koeficientem 3.0
brno = Locality("Brno", 3.0)

# Zemědělský pozemek o ploše 900 metrů čtverečních v lokalitě Manětín s koeficientem 0.8. Daň z této nemovitosti je 900 * 0.85 * 0.8 = 612.
estate = Estate(locality=manetin, estate_type="land", area=900)
print("Daň za zemědělský pozemek:", estate.calculate_tax())  # Očekáváno: 612

# Dům s podlahovou plochou 120 metrů čtverečních v lokalitě Manětín s koeficientem 0.8. Daň z této nemovitosti je 120 * 0.8 * 15 = 1440.
residence_house = Residence(locality=manetin, area=120, commercial=False)
print("Daň za obytný dům:", residence_house.calculate_tax())  # Očekáváno: 1440

# Kancelář (tj. komerční nemovitost) s podlahovou plochou 90 metrů čtverečních v lokalitě Brno s koeficientem 3. Daň z této nemovitosti je 90 * 3 * 15 * 2 = 8100.
residence_office = Residence(locality=brno, area=90, commercial=True)
print("Daň za komerční kancelář:", residence_office.calculate_tax())  # Očekáváno: 8100
