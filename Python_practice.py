
#voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
#               {"county":"Denver", "registered_voters": 463353},
#                {"county":"Jefferson", "registered_voters": 432438}]

#counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

## with concatenation 
#for county, voters in counties_dict.items():
#    print(county + " county has " + str(voters) + " registered voters.")

## with f-strings
#for county, voters in counties_dict.items():
#    msg = f"{county} county has {voters:,} registered voters."
#    print(msg)

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

#for i in range(len(voting_data)):
#    county = voting_data[i]['county']
#    voters = voting_data[i]['registered_voters']
#    msg = f"{county} county has {voters:,} registered voters."
#    print(msg)

for place in voting_data:
    county = place['county']
    voters = place['registered_voters']
    print(f"{county} county has {voters:,} registered voters.")