"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"

def main():
    subjects = load_subjects()
    print(display_subjects(subjects))
    print(subjects)


def load_subjects():
    """Read data from file formatted like: subject,lecturer,number of students."""
    subjects = []  # a list of subject list
    input_file = open(FILENAME)
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        subjects.append(parts)  # put in the subjects into a list of subjects
    input_file.close()
    return subjects

def display_subjects(subjects):
    # Display subject code, lecturer and number of students
    for subject in subjects:
        print(f"{subject[0]} is taught by {subject[1]:12} and has {subject[2]:4} students")

main()