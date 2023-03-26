while True:
    position = input("Enter the position of the chess piece (e.g. a1): ")
    if len(position) == 1:
        print("Invalid input. Please enter both a letter between a-h and a number between 1-8.")
        continue

    file = position[0]  # letter
    rank = position[1]  # number

    # Check if the values are within the allowed limits
    if file not in "abcdefgh" or rank not in "12345678":
        print("Invalid input. Please enter a letter between a-h and a number between 1-8.")
    else:
        # Determine the color of the square based on the position of the piece
        if (ord(file) + int(rank)) % 2 == 0:
            color = "black"
        else:
            color = "white"
        print(f"The square at {position} is {color}.")
        break
