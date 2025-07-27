import random  # Required to simulate rolling dice


class DiceRoller:
    def __init__(self, sides):
        """
        Initialize the DiceRoller with a specific number of sides.
        Validates that 'sides' is an integer between 2 and 100.
        """
        if isinstance(sides, int):
            if 2 <= sides <= 100:
                self.sides = sides  # Valid sides, store it
            else:
                print(f'{sides} is not between 2 and 100')
                self.sides = None  # Mark as invalid
        else:
            print('Invalid input: sides must be an integer')
            self.sides = None  # Mark as invalid

    def roll(self):
        """
        Rolls a single die with the configured number of sides.
        Returns an integer result if sides are valid; otherwise, returns None.
        """
        if self.sides:  # Only roll if sides are valid
            return random.randint(1, self.sides)
        else:
            print('Invalid number of sides')
            return None

    def roll_multiple(self, numdie):
        """
        Rolls multiple dice and returns a list of the results.
        Expects 'numdie' to be an integer (number of dice).
        """
        results = []  # List to store roll results

        if isinstance(numdie, int):
            for _ in range(numdie):  # Repeat for each die
                result = self.roll()  # Call the single die roller
                results.append(result)
            return results  # Return list of results
        else:
            print("Number of dice must be an integer.")
            return None


# This block runs only when the script is run directly (not imported)
if __name__ == '__main__':
    # Prompt the user for number of sides
    sides_input = input('Enter number of sides (2–100): ')

    if sides_input.isdigit():
        sides = int(sides_input)  # Convert to integer
        roller = DiceRoller(sides)  # Create a DiceRoller instance

        if roller.sides:  # Proceed only if the roller was set up correctly
            # Prompt the user for number of dice
            dice_count = input('Enter the number of dice you\'re rolling: ')

            if dice_count.isdigit():
                num_dice = int(dice_count)
                results = roller.roll_multiple(num_dice)  # Roll the dice
                print(f'Your rolls: {results}')
                print(f'Total: {sum(results)}')  # Optional: sum of all rolls
            else:
                print('Number of dice must be a whole number.')
        else:
            print('Invalid number of sides provided.')
    else:
        print('Number of sides must be a whole number.')
