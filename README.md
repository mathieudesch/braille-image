# ASCII Art Generator

This project is a web-based ASCII Art Generator that converts uploaded images into ASCII art using braille characters. It provides a simple interface for users to adjust various parameters and generate ASCII representations of their images.

## Features

- Convert images to ASCII art using braille characters
- Adjustable threshold for black and white conversion
- Option to invert the image
- Customizable width for the output ASCII art
- Real-time character count display
- Copy ASCII art to clipboard functionality

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/ascii-art-generator.git
   cd ascii-art-generator
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install flask pillow numpy
   ```

## Usage

1. Start the Flask server:
   ```
   python app.py
   ```

2. Open a web browser and navigate to `http://localhost:5000`

3. Use the interface to:
   - Upload an image
   - Adjust the threshold slider
   - Toggle image inversion
   - Set the desired width (optional)
   - Generate ASCII art
   - Copy the generated ASCII art

## How It Works

The application uses the following process to generate ASCII art:

1. The uploaded image is converted to grayscale and enhanced for better contrast.
2. Each 2x4 pixel block is converted to a braille character based on its intensity.
3. The resulting ASCII art is displayed and can be copied to the clipboard.

## Project Structure

- `app.py`: Contains the Flask server code and image processing logic.
- `index.html`: The HTML template for the web interface (located in the `templates` folder).

## Contributing

Contributions to improve the ASCII Art Generator are welcome! Please feel free to submit pull requests or open issues to suggest improvements or report bugs.

## License

This project is open-source and available under the MIT License.
