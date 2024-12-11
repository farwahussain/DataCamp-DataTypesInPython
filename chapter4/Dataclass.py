from dataclasses import dataclass

weight_log =[('Gentoo', 230.0, 5500.0, 'MALE'), ('Gentoo', 229.0, 5800.0, 'MALE'),
             ('Gentoo', 225.0, 5400.0, 'MALE'), ('Gentoo', 219.0, 5250.0, 'MALE'),
             ('Gentoo', 210.0, 4300.0, 'FEMALE'), ('Gentoo', 216.0, 4925.0, 'MALE')]

@dataclass
class WeightEntry:
    #Define the fields on the class
    species : str
    body_mass : int
    flipper_length : int
    sex : str
    
    #define property that returns the body mass/ flipper length
    @property
    def mass_to_flipper_length_ratio(self):
        return self.body_mass / self.flipper_length
    
# Create the empty list: labeled_entries
labeled_entries = []

# Iterate over the weight_log entries
for species, body_mass, flipper_length, sex in weight_log:
    # Append a new WeightEntry instance to labeled_entries
    labeled_entries.append(WeightEntry(species, body_mass, flipper_length, sex))
    
# Print a list of the first 5 mass_to_flipper_length_ratio values
print([entry.mass_to_flipper_length_ratio for entry in labeled_entries[:5]])