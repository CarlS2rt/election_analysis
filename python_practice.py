voting_data = []
voting_data.append({'county':'Arapahoe', 'registered_voters': 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
voting_data
voting_data.insert(1,{'county':'El Paso', 'registered_voters':461149})
voting_data.pop(0)
voting_data.pop(1)
voting_data.insert(2,{'county':'Denver', 'registered_voters': 463353})
voting_data.append({'county':'Arapahoe', 'registered_voters': 422829})
print(voting_data)

voting_data[2] == 'Denver'
counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

for i in range(len(counties)):
    print(counties[i])
    
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)