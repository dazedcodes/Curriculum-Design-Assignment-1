""" This program will return all of the medically associated bones for
    a colloquial body part that a user inputs.

    Input: face
    Output: rib 3, rib4, rib5, rib6, rib7, rib8

"""
## HANDLING INVALID INPUTS ##
    # capital versus lower case
    # doesn't insert a term that's not in the dictionary


## THOUGHTS ABOUT ASSIGNMENTS
    # adding items to a dictionary
    # separation of functions
    # searching for an item in the dictionary
    # adding an item to a dictionary
    # key, value pairs in dictionary

def insert_key_value_pair(dictionary, key, value, length):
    """
    Takes in a dictionary, a key, value, and count and returns a the dictionary
    with the key, value pairs added. Keys are (Strings) that refer to the
    colloquial name and values are (Strings) that refer to the medical terms

    """
    index = length - 1
    dictionary.setdefault(key, [])
    if key in dictionary:
        dictionary[key].append(value)
    else:
        dictionary[key] = {value}
    return dictionary

def create_dictionary(filename):
    """
    Takes in a file and returns a dictionary of key, value pairs. Keys are
    (Strings) that refer to the colloquial name and values are (Lists) that
    refer to the associated medical terms

    """
    dict = {}
    f = open(filename)
    list = f.readlines()
    count = 0
    for line in list:
        currentline = line.split(",")
        count += 1
        key = currentline[0]
        value = currentline[1].strip()
        dict  = insert_key_value_pair(dict, key, value, count)
    return dict

def colloquial_to_medical(dictionary,colloquial_name):
    """
    Takes in a colloquial term  and dictionary and returns a list of medical
    terms associated with the colloquial term.
    The colloquial term is a (String), the dictionary is a (2D Array)
    and the terms associated are a (List) of the associated medical terms.

    """
    list = []
    for key in dictionary:
        if colloquial_name in dictionary[key]:
            list.append(key)
    return list

def print_message(list):
    """
    Takes a list of medical terms associated with the colloquial term and
    returns a recommended message of bones that the user should check out.
    The associated medical terms (List) and the message (String).

    """
    message = 'Tell your doctor that you need a look at your '

    #TO DO
    return message

def main():
    import sys

    Dict = create_dictionary("dataset.txt")

    colloquial_term = raw_input("What part of your body hurts?: ")
    print "Oh, I'm so sorry that your", colloquial_term, "hurts!"

    medical_terms = colloquial_to_medical(Dict,colloquial_term)
    print medical_terms

    print ""
    print "Let me see..."
    print ""
    reccomendations = print_message(medical_terms)

    print reccomendations


if __name__ == '__main__':
    main()
