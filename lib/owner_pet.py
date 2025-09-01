class Pet:
   all = []
   PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

   def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.pet_type = pet_type
        if pet_type not in self.PET_TYPES:
            raise ValueError(f"Invalid pet type: {pet_type}. Must be one of {self.PET_TYPES}.")

        self.owner = owner
        if owner is not None:
            if not isinstance(owner, Owner):
                raise ValueError("Owner must be an instance of Owner class.")
            owner.add_pet(self)
        Pet.all.append(self)

class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []  # Changed from pets to _pets to avoid conflict

    def pets(self):
        return self._pets

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise ValueError("Only instances of Pet can be added.")
        pet.owner = self
        if pet not in self._pets:
            self._pets.append(pet)

    def get_sorted_pets(self):
        return sorted(self._pets, key=lambda pet: pet.name)