def number_guesser(left, right):
    while left <= right:
        target = (left + right) //2
        user_response = input(f"Is it {target} (yes or no): ").lower()
        if user_response == "yes":
            print("I got it! Awesome! Thanks for playing!")
            return
        elif user_response == "no":
            high_or_low = input("Was that too high or too low (too high or too low): ").lower()
            if high_or_low == "too high":
                right = target - 1
            elif high_or_low == "too low":
                left = target + 1
            else:
                print("INVALID")


def main():

    print("""
    Welcome to the number guesser!
    Pick a number in your mind and I'll try to guess it!
    """)
    print()

    start_game = input("Are you ready (yes or no): ").lower()
    if start_game == "yes":
        print("Great")
        number_guesser(1, 100)
    else:
        print("Please play the game!")
        return

if __name__ == "__main__":
    main()
