import streamlit as st

# Conversion functions for all categories
def convert_length(value, from_unit, to_unit):
    # Conversion factors to meters
    to_meter = {
        'Kilometers': 1000,
        'Centimeters': 0.01,
        'Millimeters': 0.001,
        'Nanometers': 1e-9,
        'Miles': 1609.34,
        'Yards': 0.9144,
        'Feet': 0.3048,
        'Inches': 0.0254,
        'Nautical Miles': 1852
    }
    meters = value * to_meter[from_unit]
    converted_value = meters / to_meter[to_unit]
    return converted_value

def convert_area(value, from_unit, to_unit):
    # Conversion factors to square meters
    to_square_meter = {
        'Square Miles': 2589988.11,
        'Square Yards': 0.836127,
        'Square Feet': 0.092903,
        'Square Meters': 1,
        'Square Kilometers': 1e6,
        'Square Inches': 0.00064516,
        'Hectares': 10000,
        'Acres': 4046.86
    }
    square_meters = value * to_square_meter[from_unit]
    converted_value = square_meters / to_square_meter[to_unit]
    return converted_value

def convert_data_rate(value, from_unit, to_unit):
    # Conversion factors to bits per second
    to_bits_per_second = {
        'Bits per Second': 1,
        'Kilobits per Second': 1e3,
        'Kilobytes per Second': 8e3,
        'Kibibits per Second': 1024,
        'Megabits per Second': 1e6,
        'Megabytes per Second': 8e6,
        'Mebibits per Second': 1.049e6,
        'Gigabits per Second': 1e9,
        'Gigabytes per Second': 8e9,
        'Gibibits per Second': 1.074e9,
        'Terabits per Second': 1e12,
        'Terabytes per Second': 8e12
    }
    bits_per_second = value * to_bits_per_second[from_unit]
    converted_value = bits_per_second / to_bits_per_second[to_unit]
    return converted_value

def convert_digital_storage(value, from_unit, to_unit):
    # Conversion factors to bits
    to_bits = {
        'Kilobit': 1e3,
        'Kibibit': 1024,
        'Megabit': 1e6,
        'Mebibit': 1.049e6,
        'Gigabit': 1e9,
        'Gibibit': 1.074e9,
        'Terabit': 1e12,
        'Tebibit': 1.1e12,
        'Petabit': 1e15,
        'Pebibit': 1.126e15,
        'Byte': 8,
        'Kilobyte': 8e3,
        'Kibibyte': 8192,
        'Megabyte': 8e6,
        'Mebibyte': 8.389e6,
        'Gigabyte': 8e9,
        'Gibibyte': 8.59e9,
        'Terabyte': 8e12,
        'Tebibyte': 8.796e12,
        'Petabyte': 8e15,
        'Pebibyte': 9.007e15
    }
    bits = value * to_bits[from_unit]
    converted_value = bits / to_bits[to_unit]
    return converted_value

def convert_energy(value, from_unit, to_unit):
    # Conversion factors to joules
    to_joules = {
        'Joules': 1,
        'Kilojoules': 1e3,
        'Gram Calories': 4.184,
        'Kilocalories': 4184,
        'Watt Hours': 3600,
        'Kilowatt-hours': 3.6e6,
        'Electronvolts': 1.60218e-19,
        'British Thermal Units': 1055.06,
        'US Therms': 1.055e8,
        'Foot-pounds': 1.35582
    }
    joules = value * to_joules[from_unit]
    converted_value = joules / to_joules[to_unit]
    return converted_value

def convert_frequency(value, from_unit, to_unit):
    # Conversion factors to hertz
    to_hertz = {
        'Hertz': 1,
        'Kilohertz': 1e3,
        'Megahertz': 1e6,
        'Gigahertz': 1e9
    }
    hertz = value * to_hertz[from_unit]
    converted_value = hertz / to_hertz[to_unit]
    return converted_value

def convert_fuel_economy(value, from_unit, to_unit):
    # Conversion factors to kilometers per liter
    to_km_per_liter = {
        'Kilometers per Liter': 1,
        'Miles per US Gallon': 0.425144,
        'Miles per Gallon': 0.354006,
        'Liters per 100 Kilometers': 100 / value if value != 0 else 0
    }
    km_per_liter = value * to_km_per_liter[from_unit]
    converted_value = km_per_liter / to_km_per_liter[to_unit]
    return converted_value

def convert_mass(value, from_unit, to_unit):
    # Conversion factors to kilograms
    to_kilograms = {
        'Kilograms': 1,
        'Tonnes': 1000,
        'Grams': 0.001,
        'Milligrams': 1e-6,
        'Micrograms': 1e-9,
        'Imperial Tons': 1016.05,
        'US Tons': 907.185,
        'Stones': 6.35029,
        'Pounds': 0.453592,
        'Ounces': 0.0283495
    }
    kilograms = value * to_kilograms[from_unit]
    converted_value = kilograms / to_kilograms[to_unit]
    return converted_value

def convert_plane_angle(value, from_unit, to_unit):
    # Conversion factors to degrees
    to_degrees = {
        'Degrees': 1,
        'Radians': 57.2958,
        'Arcseconds': 1 / 3600,
        'Gradians': 0.9,
        'Milliradians': 0.0572958,
        'Minutes of Arc': 1 / 60
    }
    degrees = value * to_degrees[from_unit]
    converted_value = degrees / to_degrees[to_unit]
    return converted_value

def convert_pressure(value, from_unit, to_unit):
    # Conversion factors to pascals
    to_pascals = {
        'Pascals': 1,
        'Bars': 1e5,
        'Standard Atmospheres': 101325,
        'Pounds per Square Inch': 6894.76,
        'Torr': 133.322
    }
    pascals = value * to_pascals[from_unit]
    converted_value = pascals / to_pascals[to_unit]
    return converted_value

def convert_speed(value, from_unit, to_unit):
    # Conversion factors to meters per second
    to_meters_per_second = {
        'Meters per Second': 1,
        'Kilometers per Hour': 0.277778,
        'Miles per Hour': 0.44704,
        'Feet per Second': 0.3048,
        'Knots': 0.514444
    }
    meters_per_second = value * to_meters_per_second[from_unit]
    converted_value = meters_per_second / to_meters_per_second[to_unit]
    return converted_value

def convert_temperature(value, from_unit, to_unit):
    # Conversion logic for temperature
    if from_unit == 'Degrees Celsius':
        if to_unit == 'Fahrenheit':
            return (value * 9/5) + 32
        elif to_unit == 'Kelvin':
            return value + 273.15
        else:
            return value
    elif from_unit == 'Fahrenheit':
        if to_unit == 'Degrees Celsius':
            return (value - 32) * 5/9
        elif to_unit == 'Kelvin':
            return (value - 32) * 5/9 + 273.15
        else:
            return value
    elif from_unit == 'Kelvin':
        if to_unit == 'Degrees Celsius':
            return value - 273.15
        elif to_unit == 'Fahrenheit':
            return (value - 273.15) * 9/5 + 32
        else:
            return value
    else:
        return value

def convert_time(value, from_unit, to_unit):
    # Conversion factors to seconds
    to_seconds = {
        'Seconds': 1,
        'Nanoseconds': 1e-9,
        'Microseconds': 1e-6,
        'Milliseconds': 0.001,
        'Minutes': 60,
        'Hours': 3600,
        'Days': 86400,
        'Weeks': 604800,
        'Months': 2.628e6,
        'Calendar Years': 3.154e7,
        'Decades': 3.154e8,
        'Centuries': 3.154e9
    }
    seconds = value * to_seconds[from_unit]
    converted_value = seconds / to_seconds[to_unit]
    return converted_value

def convert_volume(value, from_unit, to_unit):
    # Conversion factors to liters
    to_liters = {
        'Liters': 1,
        'US Liquid Gallons': 3.78541,
        'US Liquid Quarts': 0.946353,
        'US Liquid Pints': 0.473176,
        'US Legal Cups': 0.24,
        'US Fluid Ounces': 0.0295735,
        'US Tablespoons': 0.0147868,
        'US Teaspoons': 0.00492892,
        'Cubic Meters': 1000,
        'Milliliters': 0.001,
        'Imperial Gallons': 4.54609,
        'Imperial Quarts': 1.13652,
        'Imperial Pints': 0.568261,
        'Imperial Cups': 0.284131,
        'Imperial Fluid Ounces': 0.0284131,
        'Imperial Tablespoons': 0.0177582,
        'Imperial Teaspoons': 0.00591939,
        'Cubic Feet': 28.3168,
        'Cubic Inches': 0.0163871
    }
    liters = value * to_liters[from_unit]
    converted_value = liters / to_liters[to_unit]
    return converted_value

# Main function to create the Streamlit app
def main():
    st.title("Comprehensive Unit Converter")

    # Category selection
    category = st.selectbox("Select Category", [
        "Length", "Area", "Data Transfer Rate", "Digital Storage", "Energy",
        "Frequency", "Fuel Economy", "Mass", "Plane Angle", "Pressure",
        "Speed", "Temperature", "Time", "Volume"
    ])

    # Unit selection and conversion logic
    if category == "Length":
        units = ["Kilometers", "Centimeters", "Millimeters", "Nanometers",
                 "Miles", "Yards", "Feet", "Inches", "Nautical Miles"]
    elif category == "Area":
        units = ["Square Miles", "Square Yards", "Square Feet", "Square Meters",
                 "Square Kilometers", "Square Inches", "Hectares", "Acres"]
    elif category == "Data Transfer Rate":
        units = ["Bits per Second", "Kilobits per Second", "Kilobytes per Second",
                 "Kibibits per Second", "Megabits per Second", "Megabytes per Second",
                 "Mebibits per Second", "Gigabits per Second", "Gigabytes per Second",
                 "Gibibits per Second", "Terabits per Second", "Terabytes per Second"]
    elif category == "Digital Storage":
        units = ["Kilobit", "Kibibit", "Megabit", "Mebibit", "Gigabit", "Gibibit",
                 "Terabit", "Tebibit", "Petabit", "Pebibit", "Byte", "Kilobyte",
                 "Kibibyte", "Megabyte", "Mebibyte", "Gigabyte", "Gibibyte",
                 "Terabyte", "Tebibyte", "Petabyte", "Pebibyte"]
    elif category == "Energy":
        units = ["Joules", "Kilojoules", "Gram Calories", "Kilocalories",
                 "Watt Hours", "Kilowatt-hours", "Electronvolts",
                 "British Thermal Units", "US Therms", "Foot-pounds"]
    elif category == "Frequency":
        units = ["Hertz", "Kilohertz", "Megahertz", "Gigahertz"]
    elif category == "Fuel Economy":
        units = ["Kilometers per Liter", "Miles per US Gallon", "Miles per Gallon",
                 "Liters per 100 Kilometers"]
    elif category == "Mass":
        units = ["Kilograms", "Tonnes", "Grams", "Milligrams", "Micrograms",
                 "Imperial Tons", "US Tons", "Stones", "Pounds", "Ounces"]
    elif category == "Plane Angle":
        units = ["Degrees", "Radians", "Arcseconds", "Gradians", "Milliradians",
                 "Minutes of Arc"]
    elif category == "Pressure":
        units = ["Pascals", "Bars", "Standard Atmospheres", "Pounds per Square Inch",
                 "Torr"]
    elif category == "Speed":
        units = ["Meters per Second", "Kilometers per Hour", "Miles per Hour",
                 "Feet per Second", "Knots"]
    elif category == "Temperature":
        units = ["Degrees Celsius", "Fahrenheit", "Kelvin"]
    elif category == "Time":
        units = ["Seconds", "Nanoseconds", "Microseconds", "Milliseconds", "Minutes",
                 "Hours", "Days", "Weeks", "Months", "Calendar Years", "Decades",
                 "Centuries"]
    elif category == "Volume":
        units = ["Liters", "US Liquid Gallons", "US Liquid Quarts", "US Liquid Pints",
                 "US Legal Cups", "US Fluid Ounces", "US Tablespoons", "US Teaspoons",
                 "Cubic Meters", "Milliliters", "Imperial Gallons", "Imperial Quarts",
                 "Imperial Pints", "Imperial Cups", "Imperial Fluid Ounces",
                 "Imperial Tablespoons", "Imperial Teaspoons", "Cubic Feet", "Cubic Inches"]

    # Input fields
    from_unit = st.selectbox("From", units)
    to_unit = st.selectbox("To", units)
    value = st.number_input("Enter value", min_value=0.0)

    # Conversion button
    if st.button("Convert"):
        try:
            if category == "Length":
                result = convert_length(value, from_unit, to_unit)
            elif category == "Area":
                result = convert_area(value, from_unit, to_unit)
            elif category == "Data Transfer Rate":
                result = convert_data_rate(value, from_unit, to_unit)
            elif category == "Digital Storage":
                result = convert_digital_storage(value, from_unit, to_unit)
            elif category == "Energy":
                result = convert_energy(value, from_unit, to_unit)
            elif category == "Frequency":
                result = convert_frequency(value, from_unit, to_unit)
            elif category == "Fuel Economy":
                result = convert_fuel_economy(value, from_unit, to_unit)
            elif category == "Mass":
                result = convert_mass(value, from_unit, to_unit)
            elif category == "Plane Angle":
                result = convert_plane_angle(value, from_unit, to_unit)
            elif category == "Pressure":
                result = convert_pressure(value, from_unit, to_unit)
            elif category == "Speed":
                result = convert_speed(value, from_unit, to_unit)
            elif category == "Temperature":
                result = convert_temperature(value, from_unit, to_unit)
            elif category == "Time":
                result = convert_time(value, from_unit, to_unit)
            elif category == "Volume":
                result = convert_volume(value, from_unit, to_unit)
            st.success(f"{value} {from_unit} is {result:.6f} {to_unit}")
        except Exception as e:
            st.error(f"An error occurred: {e}")

# Run the app
if __name__ == "__main__":
    main()