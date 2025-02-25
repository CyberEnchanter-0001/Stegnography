# Stegnography
# Image Steganography in Python

## Overview
This project implements a simple image steganography tool that hides a secret message inside an image by modifying pixel values. The encrypted image is saved, and the message can be retrieved using the correct passcode.

## Requirements
- Python 3
- OpenCV (`cv2`)

## Installation
1. Install Python if not already installed.
2. Install the required dependencies using pip:
   ```sh
   pip install opencv-python
   ```

## Usage

### Encryption
1. Place the image file (`mypic.jpg`) in the same directory as the script.
2. Run the script:
   ```sh
   python steg.py
   ```
3. Enter the secret message when prompted.
4. Enter a passcode for encryption.
5. The modified image will be saved as `encryptedImage.jpg`.

### Decryption
1. Run the script again.
2. Enter the passcode when prompted.
3. If the passcode is correct, the original message will be displayed.

## Code Explanation
- Reads an image (`mypic.jpg`) and modifies pixel values to encode the message.
- Saves the modified image as `encryptedImage.jpg`.
- Asks for a passcode to decrypt the hidden message.
- If the passcode matches, extracts and displays the secret message.

## Notes
- The image used must be large enough to store the entire message.
- The script currently modifies only one pixel per character in a basic encoding scheme.

## License
This project is open-source and free to use for educational purposes.

