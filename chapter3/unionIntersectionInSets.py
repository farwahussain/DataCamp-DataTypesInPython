penguins = [{'species': 'Adlie', 'flipper_length': 190.0, 'body_mass': 3050.0, 'sex': 'FEMALE'},
            {'species': 'Adlie', 'flipper_length': 184.0, 'body_mass': 3325.0, 'sex': 'FEMALE'},
            {'species': 'Gentoo', 'flipper_length': 209.0, 'body_mass': 4800.0, 'sex': 'FEMALE'},
            {'species': 'Adlie', 'flipper_length': 193.0, 'body_mass': 4200.0, 'sex': 'MALE'},
            {'species': 'Gentoo', 'flipper_length': 210.0, 'body_mass': 4400.0, 'sex': 'FEMALE'},
            {'species': 'Gentoo', 'flipper_length': 213.0, 'body_mass': 4650.0, 'sex': 'FEMALE'},
            {'species': 'Chinstrap', 'flipper_length': 193.0, 'body_mass': 3600.0, 'sex': 'FEMALE'},
            {'species': 'Adlie', 'flipper_length': 193.0, 'body_mass': 3800.0, 'sex': 'MALE'},
            {'species': 'Chinstrap', 'flipper_length': 199.0, 'body_mass': 3900.0, 'sex': 'FEMALE'},
            {'species': 'Chinstrap', 'flipper_length': 195.0, 'body_mass': 3650.0, 'sex': 'FEMALE'},
            {'species': 'Adlie', 'flipper_length': 185.0, 'body_mass': 3700.0, 'sex': 'FEMALE'},
            {'species': 'Gentoo', 'flipper_length': 208.0, 'body_mass': 4575.0, 'sex': 'FEMALE'},
            {'species': 'Adlie', 'flipper_length': 196.0, 'body_mass': 4350.0, 'sex': 'MALE'},
            {'species': 'Adlie', 'flipper_length': 191.0, 'body_mass': 3700.0, 'sex': 'FEMALE'},
            {'species': 'Chinstrap', 'flipper_length': 195.0, 'body_mass': 3300.0, 'sex': 'FEMALE'},
            {'species': 'Adlie', 'flipper_length': 195.0, 'body_mass': 3450.0, 'sex': 'FEMALE'},
            {'species': 'Gentoo', 'flipper_length': 217.0, 'body_mass': 4875.0, 'sex': '.'},
            {'species': 'Gentoo', 'flipper_length': 212.0, 'body_mass': 4875.0, 'sex': 'FEMALE'},
            {'species': 'Adlie', 'flipper_length': 205.0, 'body_mass': 4300.0, 'sex': 'MALE'},
            {'species': 'Gentoo', 'flipper_length': 220.0, 'body_mass': 6000.0, 'sex': 'MALE'}]


# Use a list comprehension to iterate over each penguin in penguins saved as female_species_list
# If the the sex of the penguin is 'FEMALE', return the species value
female_species_list = [penguin["species"] for penguin in penguins if penguin["sex"] == 'FEMALE']

# Create a set using the female_species_list as female_penguin_species
female_penguin_species = set(female_species_list)

# Use a list comprehension to iterate over each penguin in penguins saved as female_species_list
# If the the sex of the penguin is 'FEMALE', return the species value
male_species_list = [penguin["species"] for penguin in penguins if penguin["sex"] == 'MALE']

# Create a set using the female_species_list as female_penguin_species
male_penguin_species = set(male_species_list)

# Find the union: all_species
all_species = female_penguin_species.union(male_penguin_species)

# Print the count of names in all_species
print(len(all_species))

# Find the intersection: overlapping_species
overlapping_species = female_penguin_species.intersection(male_penguin_species)

# Print the count of species in overlapping_species
print(len(overlapping_species))