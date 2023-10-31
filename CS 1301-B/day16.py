def pet_choices(animallist,preferred_weight):

    considered_animals = []
    for animal,weight in animallist:
        if weight <= preferred_weight:
            considered_animals.append(animal)

    considered_animals.sort()

    return considered_animals





