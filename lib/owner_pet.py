class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in self.PET_TYPES:
            raise Exception(f"{pet_type} is not a valid pet type. Allowed types are {', '.join(self.PET_TYPES)}.")
        self.name = name
        self.pet_type = pet_type
        self.owner = None
        if owner:
            if not isinstance(owner, Owner):
                raise Exception("Owner must be of type Owner.")
            self.owner = owner
        Pet.all.append(self)







class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("The provided object is not of type Pet.")
        pet.owner = self

    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)
