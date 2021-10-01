from diamond import diamond_greetings
from garache import garache_greetings
from mieres import mieres_greetings
from finlayson import Finlayson_greetings

def say_hello():

    diamond_greetings()
    print()
    garache_greetings()
    print()
    mieres_greetings()
    print()
    Finlayson_greetings()
    print()


def main():
    print("Welcome to our collaborative program.")
    print()
    say_hello()


if __name__ == "__main__":
    main()
