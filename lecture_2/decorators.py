def announce(f):
    def wrapper():
        print("About to run function...")
        f()
        print("Done with funtion!")
    return wrapper

@announce
def hello():
    print("Welcome to our Store!")

hello()