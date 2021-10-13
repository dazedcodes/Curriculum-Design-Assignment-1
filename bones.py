"""
    Author: Maya Murphy, 22'
    Carleton College, Layla Oesper (Advisor)

    This program will return all of the medically associated bones for
    a colloquial body part that a user inputs.
"""

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

def print_message(term, list):
    """
    Takes a list of medical terms associated with the colloquial term and
    returns a recommended message of bones that the user should check out.
    The associated medical terms (List) and the message (String).

    """
    if not list:
        print("Hmm, I don't recognize that body part. Try again. ")
        print(" ")
    else:
        print("")
        print("Oh, I'm so sorry that your", term, "hurts!")
        print("")
        message = "Tell your doctor that you need a look at your: "
        print(message)
        print("")
        for term in list:
            print(term, "")
        print("")
        print("Feel better soon!")
        print("")

def main():
    import sys
    Dict = create_dictionary("dataset.txt")
    colloquial_term = input("What part of your body hurts?: ").lower()
    medical_terms = colloquial_to_medical(Dict,colloquial_term)
    print_message(colloquial_term, medical_terms)
if __name__ == '__main__':
    main()
