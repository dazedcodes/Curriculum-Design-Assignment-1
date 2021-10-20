HOMEWORK 1 HIGH-LEVEL OVERVIEW

    Whenever you say "ouch my toe hurts!", what you are really saying medically

is "ouch, my phalanges hurt!" In this homework assignment, you will contribute
to some starter code that will take in as input a colloquial body part and
return all of the medical bone terms associated with that colloquial body part.

RUNNING CODE EXAMPLE

Below is an example of how the program should work at a high-level:
You would type in the following command into the terminal:

      python3 bones-starter.py

Which would then ask the user:

     What part of your body hurts?:

Let's say that the user says that their 'forearm' hurts.

     What part of your body hurts?: forearm

Then the expected output would be as follows:

    Oh, I'm so sorry that your forearm hurts!

    Tell your doctor that you need a look at your:

    radius
    ulna

    Feel better soon!

PARAMETERS FOR INPUT AND EXPECTED OUTPUT

    Input: Program should be able to handle all input properly.
      (i.e, forearm, FOREARM, and Forearm should return "radius and ulna.")

    Expected Output: Handles inputs that are not in the dictionary properly.
      (i.e, if a user inputs a term that's not in the dictionary or spelled
      properly the program should instead print "Hmm, I don't recognize that
      body part. Try again.")

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

THE DATASET & DATA STRUCTURE

In order to actually implement this program, we'll need a dataset, which
will contain all of the colloquial terms and their associated medical terms.

Luckily, we've provided a dataset called 'dataset.txt' where each line of the
file is as follows:

    [medical_term], [colloquial_term]

So following from the sample input illustrated above where the user enters
'forearm' as the colloquial body part that hurts, this would mean that the
'dataset.txt' file would have two lines in the file as:

    radius, forearm
    ulna, forearm

From this dataset, you'll need to create what we'd call a dictionary which is
a set of key-value pairs. For this assignment, each key-value pair should be
as follows:

    {
      colloquial_term: [medical_term_2],
      colloquial_term: [medical_term_1, medical_term_2],
      ...
    }

You will then use this dictionary as the data structure for implementing
this program. Below are the following functions that you are tasked with
implementing.

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

Bonus for print_message():
In addition the message that this function prints if the user enters a
body part that the program doesn't recognize, print all of the
colloquial body parts that a user can choose from.

In the bones-starter.py file, the main has the following commands commented
out.

    # Dict = create_dictionary("dataset.txt")
    # colloquial_term = input("What part of your body hurts?: ")
    # medical_terms = colloquial_to_medical(Dict,colloquial_term)
    # print_message(colloquial_term, medical_terms)

What you'll want to do is begin implementing create_dictionary() first and
uncomment # Dict = create_dictionary("dataset.txt") to test out your function.

As you implement the functions that you are tasked with above, uncomment
the lines of code in main that's associated with that function to test out
your code.

It is advised to implement the functions in the order in which they are listed
in the bones-starter.py file.

Hints: Look up the following built-in Python functions as they may be of help
when writing your create_dictionary and insert_key_value_pair functions:

    readlines()
    split()
    setdefault()
