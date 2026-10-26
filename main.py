
from pyscript import document

# Dictionary containing non-metal element information
non_metals = {
    "H": {"name": "Hydrogen", "number": 1, "mass": 1.008},
    "C": {"name": "Carbon", "number": 6, "mass": 12.011},
    "N": {"name": "Nitrogen", "number": 7, "mass": 14.007},
    "O": {"name": "Oxygen", "number": 8, "mass": 15.999},
    "P": {"name": "Phosphorus", "number": 15, "mass": 30.974},
    "S": {"name": "Sulfur", "number": 16, "mass": 32.06},
    "F": {"name": "Fluorine", "number": 9, "mass": 18.998},
    "Cl": {"name": "Chlorine", "number": 17, "mass": 35.45},
    "Se": {"name": "Selenium", "number": 34, "mass": 78.971},
    "Br": {"name": "Bromine", "number": 35, "mass": 79.904},
    "I": {"name": "Iodine", "number": 53, "mass": 126.904},
    "He": {"name": "Helium", "number": 2, "mass": 4.0026},
    "Ne": {"name": "Neon", "number": 10, "mass": 20.180},
    "Ar": {"name": "Argon", "number": 18, "mass": 39.948},
    "Kr": {"name": "Krypton", "number": 36, "mass": 83.798},
    "Xe": {"name": "Xenon", "number": 54, "mass": 131.293},
    "Rn": {"name": "Radon", "number": 86, "mass": 222}
}


# Function to search for an element
def search_element(event):
    # Get the symbol entered by the user
    symbol = document.getElementById("symbol").value.strip().capitalize()

    # Retrieve element information from the dictionary
    element = non_metals.get(symbol, {})

    # Display the element information using element IDs
    document.getElementById("element_symbol").innerText = element.get("name") and symbol or "-"
    document.getElementById("element_name").innerText = element.get("name", "-")
    document.getElementById("atomic_number").innerText = element.get("number", "-")
    document.getElementById("atomic_mass").innerText = element.get("mass", "-")

    # Display an error message for an unknown symbol
    document.getElementById("message").innerText = {
        True: "",
        False: "Element does not exist in the non-metals list."
    }[bool(element)]
