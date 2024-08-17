# Mad Libs Generator

def mad_libs():
    # User inputs
    adjective1 = input("Enter an adjective: ")
    noun1 = input("Enter a noun: ")
    verb1 = input("Enter a verb: ")
    adjective2 = input("Enter another adjective: ")
    noun2 = input("Enter another noun: ")
    verb2 = input("Enter another verb: ")
    place = input("Enter a place: ")
    adverb = input("Enter an adverb: ")
    
    # Story template
    story = f"Once upon a time, there was a {adjective1} {noun1} who loved to {verb1}. " \
            f"One day, the {noun1} met a {adjective2} {noun2} while {verb2} in the {place}. " \
            f"They decided to {verb1} together and lived {adverb} ever after."

    # Display the generated story
    print("\nHere's your story:")
    print(story)

# Run the Mad Libs generator
mad_libs()
