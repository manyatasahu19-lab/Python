temperature = int(input("Enter today's temperature in Celsius: "))
if temperature < 20:
    outfit="jacket"
    print("It is cold today.")
    print("wear a",outfit)
else:
    outfit="T-shirt"
    print("It is warm today.")
    print("wear a",outfit)
is_raining = input("Is it raining today?(yes/no):")
if is_raining == "yes":
    print("Bring an umbrella.")
wind_speed = int(input("Enter the wind speed in km/h:"))
if wind_speed > 30:
    needs_windbreaker = "yes"
    print("It is windy today.")
    print("wear a windbreaker on your",outfit)
else:
    needs_windbreaker="no"
    print("It is calm today.")
    print("no windbreaker needed over your",outfit)
    has_puddles = input("Are there puddles on the ground? (yes/no): ")
    if has_puddles == "yes":
        shoes= "boots"
        print("The ground is wet.")
        print("wear",shoes)
    else:
        shoes="sneakers"
        print("the ground is dry.")
        print("wear",shoes)
        print("")
        print("weather check complete!")
        print("==== WEATHER OUTFIT PICKER =====")
        print("temperature:",temperature)
        print("outfit chosen:",outfit)
        print("raining:",is_raining)
        print("windbreaker needed:",needs_windbreaker)
        print("shoes chosen:",shoes)
        print("===============")