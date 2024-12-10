#Task - Create a tuple using lists and loop through it

#lists
girl_names = ['Emily', 'Ava', 'Serenity', 'Claire', 'Sophia', 'Sarah', 'Ashley', 'Chaya', 'Abigail', 'Zoe', 'Leah', 'Ava', 'Olivia', 'Emma', 'Chloe', 'Sophia', 'Aaliyah', 'Angela', 'Camila', 'Savannah', 'Serenity', 'Chloe', 'Fatoumata']
boy_names = ['Jada', 'Ethan', 'David', 'Jayden', 'Mason', 'Ryan', 'Christian', 'Isaiah', 'Jayden', 'Michael', 'Noah', 'Samuel', 'Sebastian', 'Noah', 'Daylan', 'Lucas', 'Joshua', 'Angel', 'Jacob', 'Matthew', 'Josiah', 'Jacob', 'Muhammad', 'Alexander', 'Jason']

#pair up both lists
pairs = zip(girl_names, boy_names)

#Iterate over pairs
for rank, pair in enumerate(pairs):
    
    #Unpack pairs
    girl_name , boy_name = pair
    #Print the rank and names associated with each rank
    print(f"Rank {rank + 1} : {girl_name} and {boy_name}")