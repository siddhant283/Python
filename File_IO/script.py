
import os
from translate import Translator

script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "/test.txt"
new_path = "/tanslated.txt"
abs_file_path = script_dir + rel_path
abs_file_path2 = script_dir + new_path


translator = Translator(to_lang="pt")
try:
  with open(abs_file_path, mode='r') as my_file:
    text = my_file.read()
    translation = translator.translate(text)
    print(translation)
    with open(abs_file_path2, mode="w") as my_file2:
        my_file2.write(translation )
except FileNotFoundError as err:
    print('Check your file path')


