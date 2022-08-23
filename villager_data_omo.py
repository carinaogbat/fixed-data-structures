def all_species(filename):
    """Takes in the name of a data file and returns unique species found"""
    #set[str]
    file = open(filename)
    all_species = set()
    for line in file:
        _, species, _, _, _ = line.rstrip().split('|')
        all_species.add(species)
        
    return all_species
# print(all_species('villagers.csv'))

def get_villagers_by_species(filename, search_string='All'):
    """Takes in name of file and name of species, returns names of all villagers of that species
    in alphabetical order"""
    #list[str]
    file = open(filename)
    villagers_by_species = []
    for line in file:
        names, species, _, _, _ = line.rstrip().split('|')
        if search_string == species:
            villagers_by_species.append(names)
        
    return sorted(villagers_by_species)


# def get_villagers_by_species_dict(filename, search_string='All'):
#     """Takes in name of file and name of species, returns names of all villagers of that species
#     in alphabetical order, trying as dictionary"""
#     file = filename
#     villagers_by_species = {}
#     for line in file:
#         char = line.rstrip().split('|')
#         name = char[0]
#         species = char[1]
#         if search_string == species:
#             villagers_by_species[species] = name
#     return villagers_by_species
# print(get_villagers_by_species_dict('villagers.csv', 'Bird'))



def all_names_by_hobby(filename):
    """Returns list of villagers with names grouped by hobby"""
    #should be list with 6 lists list[list[string]]
    file = open(filename)
    hobby_and_names = {}
    for line in file:
        names, _, _, hobby, _ = line.rstrip().split('|')
        if hobby in hobby_and_names:
            hobby_and_names[hobby] = hobby_and_names[hobby] + [names]
        else:
            hobby_and_names[hobby] = [names]
  
    return hobby_and_names

# print(all_names_by_hobby('villagers.csv'))



def all_data(filename):
    """Return all the data in file as a list of tuples"""
    #list[tuple[str]]
    file = open(filename)
    villager_data = []
    for line in file:
        villager_data.append(tuple(line.rstrip().split('|')))
        
    return villager_data

print(all_data('villagers.csv'))




def find_motto(filename, villager_name):
    """Take in the name of the villager and return villager's motto or none is unable to find"""
    #str
    file = open(filename)
    for line in file:
        name, _, _, _, quote = line.rstrip().split('|')
        if villager_name == name:
            return quote
  
print(find_motto('villagers.csv', 'Rowan'))

def find_likeminded_villagers(filename, villager_name):
    """Take in the file and name of villager, return a set of villagers with the same personality"""
    #set[str]
    file = open(filename)
    name_set = set()
    villagers_personality = None
    for line in file:
        name, _, personality, _, _ = line.rstrip().split('|')
        if name == villager_name:
            villagers_personality = personality
            break
    if villagers_personality:
        for line in file:
            name, _, personality, _, _ = line.rstrip().split('|')
            if personality == villagers_personality:
                name_set.add(name)
    return name_set

print(find_likeminded_villagers('villagers.csv', 'Leonardo'))


    # target_personality = None
    # for villager_data in all_data(filename):
    #     name, _, personality = villager_data[:3]

    #     if name == villager_name:
    #         target_personality = personality
    #         break

    # if target_personality:
    #     for villager_data in all_data(filename):
    #         name, _, personality = villager_data[:3]
    #         if personality == target_personality:
    #             likeminded.add(name)

    # return likeminded
