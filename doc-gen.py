import re
import glob

config = {
    "author": "Steve Richardson",
    "project_path": "./src/"
}

all_content = []

for filename in glob.iglob(config["project_path"] + "**/*.py", recursive=True):
    f = open(filename, "r")
    file_contents = f.read()
    expression = r'"""(.|\n)+?"""'
    for match in re.finditer(expression, file_contents, re.DOTALL):
        print(match.group())

    print("______________________________________________________________________________")
    f.close()