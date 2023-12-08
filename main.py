# main.py

from puppy import Puppy
from puppy_store import PuppyStore

def main():
    store = PuppyStore()

    # Adding some puppies to the store
    store.add_puppy(Puppy("Buddy", "Golden Retriever", 1))
    store.add_puppy(Puppy("Max", "Labrador", 2))
    store.add_puppy(Puppy("Bella", "Beagle", 3))

    # Interactive console
    while True:
        print("\nWelcome to FindPuppyAHome!")
        print("1. List available puppies")
        print("2. Adopt a puppy")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            for puppy in store.list_puppies():
                print(puppy)
        elif choice == "2":
            name = input("Enter the name of the puppy you want to adopt: ")
            print(store.adopt_puppy(name))
        elif choice == "3":
            print("Thank you for using FindPuppyAHome. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
