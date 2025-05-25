# Property Tax Calculator in Python

This project is a simplified implementation of a **property tax calculator** using **object-oriented programming** in Python. It supports land parcels and residential/commercial buildings, calculates taxes based on area and location, and allows multiple properties to be grouped into a tax report.

---

## Class Structure

### Locality
Represents the location (municipality or cadastral unit) where the property is situated.

- `name`: name of the locality
- `locality_coefficient`: numeric coefficient used in tax calculation

### Property (abstract class)
Base class for all property types.

- `locality`: instance of `Locality`
- `calculate_tax()`: abstract method implemented by subclasses

### Estate (inherits from Property)
Represents a land parcel.

- `estate_type`: `EstateType` enum (e.g. land, garden, forrest, building site)
- `area`: area in square meters
- `calculate_tax()`: tax based on land type and locality

### Residence (inherits from Property)
Represents a residential or commercial building.

- `area`: floor area in square meters
- `commercial`: boolean flag indicating commercial use
- `calculate_tax()`: tax based on floor area and locality

### EstateType (Enum)
Enumeration of allowed land parcel types. Prevents invalid values.

### TaxReport
Represents a complete tax report for a person.

- `name`: name of the tax declarant
- `property_list`: list of properties
- `add_property()`: adds a property to the report
- `calculate_tax()`: returns total tax across all properties

---

## ▶️ How to Run

1. Make sure Python 3.8+ is installed.
2. Save the project files (`main.py`, `README.md`) in one directory.
3. Run the script:

```bash
property-tax-calculator.py
property-tax-calculator_bonus.py
