import sys
from PIL import Image, ImageOps
from os.path import splitext


def main():
    # Check if the user has specified exactly two command-line arguments
    check_len_argv()

    # If the input’s and output’s names do not end in .jpg, .jpeg, or .png, case-insensitively
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    input_ext = splitext(input_file)[
        1
    ].lower()  # Extract extension and convert to lowercase
    output_ext = splitext(output_file)[1].lower()

    # Check if both input and output have valid image extensions
    valid_extensions = [".jpg", ".jpeg", ".png"]
    if input_ext not in valid_extensions or output_ext not in valid_extensions:
        print("Invalid input or output file extension")
        sys.exit(1)

    # Ensure input and output have the same extension
    if input_ext != output_ext:
        print("Input and output have different extensions")
        sys.exit(1)

    # Try to open the input file
    try:
        shirt = Image.open("shirt.png")
        photo = Image.open(input_file)
        size = shirt.size
        photo = ImageOps.fit(photo, size)  # Fit the photo to the size of the shirt
        # Paste the shirt onto the resized photo (overlays the shirt image)
        photo.paste(shirt, shirt)
        # Save the final result to the output file
        photo.save(output_file)

    except FileNotFoundError:
        print(f"Input does not exist")
        sys.exit(1)


def check_len_argv():
    # Ensure exactly 2 arguments (script name + 2 file paths) are provided
    if len(sys.argv) != 3:
        if len(sys.argv) < 3:
            print("Too few command-line arguments")
        else:
            print("Too many command-line arguments")
        sys.exit(1)


if __name__ == "__main__":
    main()
