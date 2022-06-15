import logging

# map(func, *iterables)
# list(map(func, *iterables))

my_pets = ['alfred', 'tabitha', 'william', 'arla']

uppered_pets = []

for pet in my_pets:
    pet_ = pet.upper()
    uppered_pets.append(pet_)
print("the uppered pets are: ", uppered_pets)
logging.info("This is info of pets name with upper case letter.")
logging.warning("This is warning of pets name with upper case letter.")
logging.debug("This is debug of pets name with upper case letter.")
logging.error("This is error of pets name with upper case letter.")
logging.critical("This is critical of pets name with upper case letter.")