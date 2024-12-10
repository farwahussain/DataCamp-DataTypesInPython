squirrels_by_park = {'J. Hood Wright Park': {'primary_fur_color': 'Gray', 'highlights_in_fur_color': 'Cinnamon', 'activities': 'Running', 'interactions_with_humans': 'Indifferent'},
                     'Stuyvesant Square Park': {'primary_fur_color': 'Gray', 'highlights_in_fur_color': 'Cinnamon', 'activities': 'Foraging', 'interactions_with_humans': 'Indifferent'},
                     'Highbridge Park': {'primary_fur_color': 'Gray', 'highlights_in_fur_color': 'White', 'activities': 'Climbing', 'interactions_with_humans': None},
                     'Tompkins Square Park': {'primary_fur_color': 'Gray', 'highlights_in_fur_color': 'Gray', 'activities': 'Foraging', 'interactions_with_humans': None},
                     'Union Square Park': {'primary_fur_color': 'Gray', 'activities': 'Eating, Foraging', 'interactions_with_humans': None},
                     'City Hall Park': {'primary_fur_color': 'Gray', 'highlights_in_fur_color': 'White', 'activities': 'Eating, Foraging', 'interactions_with_humans': 'Indifferent'},
                     'Msgr. McGolrick Park': {'primary_fur_color': 'Gray', 'highlights_in_fur_color': 'Cinnamon', 'activities': 'Running', 'interactions_with_humans': 'Indifferent'},
                     'John V. Lindsay East River Park': {'primary_fur_color': 'Gray', 'highlights_in_fur_color': 'Gray', 'activities': 'Running, Chasing, Eating', 'interactions_with_humans': None}}

#Task 1:
# Print a list of keys from the squirrels_by_park dictionary
print(squirrels_by_park.keys())

# Print the keys from the squirrels_by_park dictionary for 'Union Square Park'
print(squirrels_by_park['Union Square Park'].keys())

# Loop over the dictionary
for park_name in squirrels_by_park:
    # Safely print the park_name and the highlights_in_fur_color or 'N/A'
    print(park_name, squirrels_by_park[park_name].get('highlights_in_fur_color', 'N/A'))

#Task 2:
# Use a for loop to iterate over the squirrels in Tompkins Square Park:
for squirrel in squirrels_by_park["Tompkins Square Park"]:
	# Safely print the activities of each squirrel or None
    print(squirrels_by_park["Tompkins Square Park"].get("activities"))
    
# Print the list of 'Cinnamon' primary_fur_color squirrels in Union Square Park
print([squirrel for squirrel in squirrels_by_park["Union Square Park"] if "Cinnamon" in squirrel])