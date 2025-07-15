def temp_conv():
    while True:
        try:
            raw_num = float(input('Enter the number you want to convert: '))
        except ValueError:
            print('Please enter a valid number.')
            continue  # restart loop on invalid input

        conv_to = input('Do you want to convert to (F)ahrenheit or (C)elsius?: ').lower()
        if conv_to == 'f':
            conv_num = (raw_num * 9 / 5) + 32
            print(f'{raw_num}°C in Fahrenheit is {conv_num}°F!\n')
        elif conv_to == 'c':
            conv_num = (raw_num - 32) * 5 / 9
            print(f'{raw_num}°F in Celsius is {conv_num}°C!\n')
        else:
            print('Please enter F or C.')
            continue  # go back to top of loop

        # Ask if user wants to convert another
        again = input('Would you like to convert another temperature? (y/n): ').lower()
        if again != 'y':
            print("Goodbye!")
            break

if __name__ == '__main__':
    temp_conv()