#Two.py

import One

print ("TOP LEVEL IN TWO.PY")

One.func()

if __name__ == "__main__":
    print("Two.py is being run directly!")
else:
    print("One.py is being run directly")