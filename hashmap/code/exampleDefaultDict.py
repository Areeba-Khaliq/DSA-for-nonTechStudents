from collections import defaultdict

countries = defaultdict(list)

countries["Pakistan"] = ["Lahore", "Karachi", "Islamabad"]
countries["India"] = ["Delhi", "Mumbai", "Chennai"]
countries["USA"] = ["New York", "Chicago", "Boston"]

countries["Canada"].append("Toronto")
countries["Canada"].append("Vancouver")
countries["Canada"].append("Montreal")

print(countries)
