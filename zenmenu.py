import zenpoems
from zenpoems import generate_line

def input_user():
    while True:
        print("Welcome to ZenPoems!")
        print("Choose one of the options below!")
        print("1. Generate a Haiku")
        print("2. Exit")
        index = input("Input which option you desire: ")
        
        if index == '1':
            #   Function for generating a Haiku
            def generate_haiku():
                line1 = generate_line(5)
                line2 = generate_line(7)
                line3 = generate_line(5)
                
                haiku = f"{line1}\n{line2}\n{line3}"
                return haiku

            #   Haiku generated
            print(generate_haiku())
            print("-----------------------------------------------------------")
            continue
        elif index == '2':
            print("Exiting program...")
            break
        
        else:
            print("Incorrect input, please type a correct option")
            continue

def main():
    input_user()

if __name__ == "__main__":
    main()