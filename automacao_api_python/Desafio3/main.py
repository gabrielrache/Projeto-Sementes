from behave.__main__ import main

debug = False

if __name__ == "__main__":
    if debug:
        main("features --no-capture --no-capture-stderr")
    else:
        main("features")