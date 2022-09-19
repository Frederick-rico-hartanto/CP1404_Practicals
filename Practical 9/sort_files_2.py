import os
import shutil

extension_to_category = {}

def main():
    os.chdir('FileToSortOut')
    for directory_name, subdirectories, filenames in os.walk('.'):
        sort_files_to_categories(filenames)

def sort_files_to_categories(filenames):
    for filename in filenames:
        data = filename.split(".")
        extension = data[1]
        if extension not in extension_to_category:
            category = input("What category would you like to sort {} files into? ".format(extension))
            extension_to_category[extension] = category
        try:
            os.mkdir(category)
        except FileExistsError:
            pass
        shutil.move(filename, category + '/' + filename)
main()




if __name__ == '__main__':
    main()