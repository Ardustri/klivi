import readline
import os

print(f"Welcome to klivi manager")

version = "1.0.0"

command = input(">> ")

git = [
    "sh script/git.sh"
]

release = [
    f"zip -r archive/klivi-v{version}.zip ./*"
]

scripts = {
    "git": git,
    "release": release
}

for script in scripts:
    if command != script:
        continue  # ignore the rest of the loop

    for i in range(len(scripts[script])):
        os.system(scripts[script][i])
