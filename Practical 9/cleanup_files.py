import shutil
import os

def main():

    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        # print("Directory:", directory_name)
        # print("\tcontains subdirectories:", subdirectories)
        # print("\tand files:", filenames)
        # print("(Current working directory is: {})".format(os.getcwd()))

        for filename in filenames:
            new_name = get_fixed_filename(filename)
            print("Renaming {} to {} ".format(filename, new_name))

            # old_name = os.path.join(directory_name, filename)
            # new_name = os.path.join(directory_name, get_fixed_filename(filename))
            # os.rename(old_name, new_name)

def get_fixed_filename(filename):

    data = filename.split(".")
    filename_without_extension = data[0]
    length_of_name = len(filename_without_extension)
    index = 1
    while index < length_of_name:
        current_character = filename_without_extension[index]
        previous_character = filename_without_extension[index - 1]
        if current_character.isupper() and previous_character.isalpha():
            filename_without_extension = filename_without_extension[:index] + " " + filename[index:]
            length_of_name = len(filename_without_extension)
            index += 1
        index += 1
    if len(data) == 2:
        filename_without_extension = filename_without_extension.strip().title() + "." + data[1].lower()
    return filename_without_extension.replace(" ", "_")

    # new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    # return new_name


main()