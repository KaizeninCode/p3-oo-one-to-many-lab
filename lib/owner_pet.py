class Owner:
    def __init__(self, name):
        self.name = name
        self.pet_list = []

    def pets(self):
        return self.pet_list

    def add_pet(self, pet):
        if isinstance(pet, Pet):
            pet.owner = self
            self.pet_list.append(pet)
        else:
            raise Exception("Invalid pet type.")

    def get_sorted_pets(self):
        return sorted(self.pet_list, key=lambda pet: pet.name)
class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        if pet_type in self.PET_TYPES:
            self.pet_type = pet_type
        else:
            raise Exception("Invalid pet type.")
        self.owner = owner
        self.__class__.all.append(self)

    @classmethod
    def get_all(cls):
        return cls.all

