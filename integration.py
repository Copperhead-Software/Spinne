import os

with open("setup.cfg", "r") as f:
    data = f.read()
    data = data.splitlines()
    data[2] = "version = " + input("version: ")
    data = "\n".join(data)
with open("setup.cfg", "w") as f:
    f.write(data)
    f.close()