""" This program will return all of the medically associated bones for
    a colloquial body part that a user inputs.

    Input: face
    Output: rib 3, rib4, rib5, rib6, rib7, rib8

"""
## HANDLING INVALID INPUTS ##
    # capital versus lower case
    # doesn't insert a term that's not in the dictionary

## THOUGHTS ABOUT ASSIGNMENTS
def create_dictionary(filename):
    """
    Takes in a file and returns a dictionary of key, value pairs. Keys are
    (Strings) that refer to the colloquial name and values are (Lists) that
    refer to the associated medical terms

    """
    Dict = {}
    f = open(filename)
    list = f.readlines()
    for line in list:
        currentline = line.split(",")
        print currentline
        key = currentline[0]
        value = currentline[1]


    # TO DO
    dict = "You need to implement this function!"
    return dict

def colloquial_to_medical(dictionary,colloquial_name):
    """
    Takes in a colloquial term  and dictionary and returns a list of medical
    terms associated with the colloquial term.
    The colloquial term is a (String), the dictionary is a (2D Array)
    and the terms associated are a (List) of the associated medical terms.

    """
    # TO DO
    list = "You need to implement this function!"
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

    dict = create_dictionary("dataset.txt")

    colloquial_term = raw_input("What part of your body hurts?: ")
    print "Oh, I'm so sorry that your", colloquial_term, "hurts!"

    medical_terms = colloquial_to_medical(dict,colloquial_term)

    print ""
    print "Let me see..."
    print ""
    reccomendations = print_message(medical_terms)

    print reccomendations


if __name__ == '__main__':
    main()
