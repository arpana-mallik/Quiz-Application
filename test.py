import tomli

with open("questions.toml", mode="rb") as toml_file:
   questions = tomli.load(toml_file)

questions
{"When does __name__ == '__main__' equal True in a Python file":
    ['When the file is run as a script',
     'When the file is imported as a module',
     'When the file has a valid name',
     'When the file only has one function'],
 'Which version of Python is the first with TOML support built-in':
    ['3.11', '3.9', '3.10', '3.12']}