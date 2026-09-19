countries = {
    "Pakistan": ["Lahore", "Karachi", "Islamabad"],
    "India": ["Delhi", "Mumbai", "Chennai"],
    "USA": ["New York", "Chicago", "Boston"]
}

# Add a new country
if "Canada" not in countries:
    countries["Canada"] = []

countries["Canada"].append("Toronto")
countries["Canada"].append("Vancouver")
countries["Canada"].append("Montreal")

print(countries)
