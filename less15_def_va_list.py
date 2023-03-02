

def give_medal(medal, *persons):
    """Nagrada"""
    for person in persons:
        print("Tov. " + person.title() + "\t nagrada: " + medal)


#give_medal("Za Otvagu", "ivan", "igor", "motorola", "wargonzo")