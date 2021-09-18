def describe_animal(animal_type, pet_name):
    '''Animal description'''
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

animal_type = 'dog'
pet_name = 'Bobik'

describe_animal(animal_type=animal_type, pet_name=pet_name)