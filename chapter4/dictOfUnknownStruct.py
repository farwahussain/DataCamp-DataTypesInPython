weight_log = [('Chinstrap', 'FEMALE', 3800.0), ('Adlie', 'FEMALE', 3450.0),
              ('Gentoo', 'FEMALE', 4300.0), ('Adlie', 'FEMALE', 3550.0),
              ('Adlie', 'FEMALE', 3175.0)]

# Create an empty dictionary: female_penguin_weights
female_penguin_weights = {}

# Iterate over each tuple in weight_log
for species, sex, body_mass in weight_log:
    if species not in weight_log:
        female_penguin_weights[species] = []
    
    female_penguin_weights[species].append((sex, body_mass))
    
print(female_penguin_weights)