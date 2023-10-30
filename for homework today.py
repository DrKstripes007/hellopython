travel_log = [
    {
                 "Name": "Suzan",
                 "age": "45",
                 "countries travelled": ["Italy", "Belgium", "France"]
            },
    {
                 "Name": "Maloney",
                 "age": "31",
                 "countries travelled": ["Cuba", "Portugal","Comoros Island"]
            },
    {
                 "Name": "Tray",
                 "age": "29",
                 "countries travelled": ["Nigeria ", "Mexico","Canada"]
            },
    {
                 "Name": "Chandler",
                 "age": "20",
                 "countries travelled": [" Netherlands", "Austria", "Fiji"]
            },
    {
                 "Name": "Brice",
                 "age": "23",
                 "countries travelled": [" Congo", "Mauritania", "Peru"]
            }

            ]
print(travel_log[0]["countries travelled"][0])

countries_in_tuplesProfile1 = tuple(travel_log[0]["countries travelled"])
countries_in_tuplesProfile2 = tuple(travel_log[1]["countries travelled"])
countries_in_tuplesProfile3 = tuple(travel_log[2]["countries travelled"])
countries_in_tuplesProfile4 = tuple(travel_log[3]["countries travelled"])
countries_in_tuplesProfile5 = tuple(travel_log[4]["countries travelled"])


print((countries_in_tuplesProfile1),
      (countries_in_tuplesProfile2),
      (countries_in_tuplesProfile3),
      (countries_in_tuplesProfile4),
      (countries_in_tuplesProfile5)
      )