travelLog= [
    {
        "country" : "US",
        "visits" : "6",
        "locations" : ["New York", "Washington", "Ohio"],
    },
    {
        "country" : "India",
        "visits" : "10",
        "locations" : ["Lucknow", "Mumbai", "Pune"],
    },
]

def addNewCountry(country, visits, locations):
    newCountry= {}
    newCountry["country"] = country
    newCountry["visits"] = visits
    newCountry["locations"] = locations
    travelLog.append(newCountry)

addNewCountry("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travelLog)