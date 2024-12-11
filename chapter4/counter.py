#import counter
from collections import Counter

penguins = [{'Species': 'Gentoo', 'Flipper Length (mm)': 230.0, 'Body Mass (g)': 5500.0, 'Sex': 'MALE'},
            {'Species': 'Chinstrap', 'Flipper Length (mm)': 201.0, 'Body Mass (g)': 4300.0, 'Sex': 'MALE'},
            {'Species': 'Adlie', 'Flipper Length (mm)': 180.0, 'Body Mass (g)': 3800.0, 'Sex': 'MALE'},
            {'Species': 'Gentoo', 'Flipper Length (mm)': 229.0, 'Body Mass (g)': 5800.0, 'Sex': 'MALE'},
            {'Species': 'Chinstrap', 'Flipper Length (mm)': 210.0, 'Body Mass (g)': 4100.0, 'Sex': 'MALE'},
            {'Species': 'Adlie', 'Flipper Length (mm)': 200.0, 'Body Mass (g)': 3975.0, 'Sex': 'MALE'},
            {'Species': 'Gentoo', 'Flipper Length (mm)': 225.0, 'Body Mass (g)': 5400.0, 'Sex': 'MALE'},
            {'Species': 'Chinstrap', 'Flipper Length (mm)': 210.0, 'Body Mass (g)': 4800.0, 'Sex': 'MALE'},
            {'Species': 'Chinstrap', 'Flipper Length (mm)': 193.0, 'Body Mass (g)': 3800.0, 'Sex': 'FEMALE'},
            {'Species': 'Adlie', 'Flipper Length (mm)': 176.0, 'Body Mass (g)': 3450.0, 'Sex': 'FEMALE'},
            {'Species': 'Chinstrap', 'Flipper Length (mm)': 210.0, 'Body Mass (g)': 3950.0, 'Sex': 'MALE'},
            {'Species': 'Gentoo', 'Flipper Length (mm)': 219.0, 'Body Mass (g)': 5250.0, 'Sex': 'MALE'},
            {'Species': 'Gentoo', 'Flipper Length (mm)': 210.0, 'Body Mass (g)': 4300.0, 'Sex': 'FEMALE'},
            {'Species': 'Gentoo', 'Flipper Length (mm)': 216.0, 'Body Mass (g)': 4925.0, 'Sex': 'MALE'},
            {'Species': 'Adlie', 'Flipper Length (mm)': 187.0, 'Body Mass (g)': 3550.0, 'Sex': 'FEMALE'},
            {'Species': 'Adlie', 'Flipper Length (mm)': 192.0, 'Body Mass (g)': 3950.0, 'Sex': 'MALE'},
            {'Species': 'Chinstrap', 'Flipper Length (mm)': 193.0, 'Body Mass (g)': 3800.0, 'Sex': 'MALE'},
            {'Species': 'Chinstrap', 'Flipper Length (mm)': 201.0, 'Body Mass (g)': 4050.0, 'Sex': 'MALE'},
            {'Species': 'Adlie', 'Flipper Length (mm)': 190.0, 'Body Mass (g)': 3650.0, 'Sex': 'MALE'},
            {'Species': 'Adlie', 'Flipper Length (mm)': 181.0, 'Body Mass (g)': 3175.0, 'Sex': 'FEMALE'}]

#Task 1: Using counter on list
#Create a Counter of the penguins sex using a list comprehension
penguins_sex_count = Counter([penguin['Sex'] for penguin in penguins])

print(penguins_sex_count)

#Task 2: Finding most common elements
#Create a counter of the penguin list to find species
penguins_species_count = Counter([penguin['Species'] for penguin in penguins])

print(penguins_species_count)