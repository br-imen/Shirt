# Shirt Project

This project overlays a shirt image onto a user-provided photo, ensuring that both images have the same file extension. The program is designed to handle common image formats such as JPEG and PNG.

## Requirements

- Python 3.x
- Pillow library (Python Imaging Library)

You can install Pillow using pip:

```bash
pip install Pillow
```

## Usage
To run the program, use the following command in the terminal:

```bash
python overlay.py input_file output_file
```

* input_file: The path to the input image (must be a JPEG or PNG).
* output_file: The path where the output image will be saved (must have the same extension as the input).

## Example
```bash
python overlay.py my_photo.jpg output_photo.jpg
```

## How It Works
1. The program checks if exactly two command-line arguments are provided.
It verifies that both the input and output files have valid image extensions (.jpg, .jpeg, or .png).
2. It ensures that the input and output files have the same extension.
3. The program attempts to open the input image and overlays a predefined shirt image (shirt.png) onto it, resizing the input image to fit the shirt size.
The final image is saved to the specified output file.

## Error Handling
The program includes error handling for the following scenarios:

* Invalid number of command-line arguments.
* Input or output file extensions are not valid.
* Input file does not exist.