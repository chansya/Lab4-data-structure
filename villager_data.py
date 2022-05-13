"""Functions to parse a file containing villager data."""

# name|species|personality|hobby|motto


def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - set[str]: a set of strings
    """
    villagers_data = open(filename)
    species_lst = []

    for line in villagers_data:
        villager_summary = line.split("|")
        species_lst.append(villager_summary[1])

    species = set(species_lst)

    # TODO: replace this with your code

    return species


all_species("villagers.csv")


def get_villagers_by_species(filename, search_string="All"):
    """Return a list of villagers' names by species.

    Arguments:
        - filename (str): the path to a data file
        - search_string (str): optional, the name of a species

    Return:
        - list[str]: a list of names
    """

    villagers = []
    villagers_data = open(filename)
    for line in villagers_data:
        name, species = line.rstrip().split('|')[:2]

        if search_string == "All":
            villagers.append(name)
        elif species == search_string:
            villagers.append(name)

    # TODO: replace this with your code

    return sorted(villagers)


get_villagers_by_species("villagers.csv", search_string="All")


def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """

    # TODO: replace this with your code

    villagers_data = open(filename)
    hobby_fitness = []
    hobby_nature = []
    hobby_education = []
    hobby_music = []
    hobby_fashion = []
    hobby_play = []
    for line in villagers_data:
        name = line.rstrip().split('|')[0]
        hobby = line.rstrip().split('|')[3]
        if hobby == "Fitness":
            hobby_fitness.append(name)
        elif hobby == "Nature":
            hobby_nature.append(name)
        elif hobby == "Education":
            hobby_education.append(name)
        elif hobby == "Music":
            hobby_music.append(name)
        elif hobby == "Fashion":
            hobby_fashion.append(name)
        elif hobby == "Play":
            hobby_play.append(name)

    return [sorted(hobby_fitness), sorted(hobby_nature), sorted(hobby_education), sorted(hobby_education),
            sorted(hobby_music), sorted(hobby_fashion), sorted(hobby_play)]


all_names_by_hobby("villagers.csv")


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """

    all_data = []
    villagers_data = open(filename)
    for line in villagers_data:
        data = line.rstrip().split('|')
        tup_data = tuple(data)

        all_data.append(tup_data)

    # TODO: replace this with your code
    return all_data


all_data("villagers.csv")


def find_motto(filename, villager_name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - str: the villager's motto or None
    """
    villagers_data = open(filename)
    for line in villagers_data:
        name = line.rstrip().split('|')[0]
        motto = line.rstrip().split('|')[-1]
        if villager_name == name:

            return motto

    return None

    # TODO: replace this with your code


find_motto("villagers.csv", "Claudia")


def find_likeminded_villagers(filename, villager_name):
    """Return a set of villagers with the same personality as the given villager.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - set[str]: a set of names

    For example:
        >>> find_likeminded_villagers('villagers.csv', 'Wendy')
        {'Bella', ..., 'Carmen'}
    """

    # TODO: replace this with your code
