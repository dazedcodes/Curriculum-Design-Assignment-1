This program will return all of the medically associated bones for
a colloquial body part that a user inputs.

Input: Program should be able to handle all input properly.
(i.e, forearm, FOREARM, and Forearm should return "radius and ulna." )

    What part of your body hurts?: forearm

Expected Output: Handles inputs that are not in the dictionary properly.
(i.e, if a user inputs a term that's not in the dictionary or spelled
properly the program should instead print "Hmm, I don't recognize that
body part. Try again.")

    Oh, I'm so sorry that your forearm hurts!

    Tell your doctor that you need a look at your:

    radius
    ulna

    Feel better soon!

Your task is to implement the following functions:

- create_dictionary(filename):
  This function should read in the dataset and return a populated dictionary.

- insert_key_value_pair(dictionary, key, value, length):
  This function is a helper function to create_dictionary(filename) which
  takes four parameters and inserts a term into the dictionary.

- colloquial_to_medical(dictionary, colloquial_name):
  This function searches the dictionary for the colloquial term and returns
  all of the associated medical terms.

- print_message(term, list):
  This function prints the message to the console specified in the expected
  output example above.

  Bonus for print_message(): In addition the message that this function prints
  if the user enters a body part that the program doesn't recognize, print all
  of the colloquial body parts that a user can choose from.

Hints: Look up the following built-in Python functions as they may be of help
when writing the program:

    readlines()
    split()
    setdefault()

To run the code type:

python3 bones-starter.py

Below are the following colloquial terms that you may input to the program.
nose
eyes
face
cheeks
jaw
head
mouth
ear
torso
shoulder
neck
waist
chest
back
upper back
middle back
lower back
wrist
fingers
shoulder blades
privates
butt
forearm
