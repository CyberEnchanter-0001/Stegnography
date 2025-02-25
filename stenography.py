import cv2
import numpy as np

def encode_message(img, message, password):
    """Embeds a secret message into an image using simple pixel encoding."""
    # Convert message to ASCII values + delimiter
    message += "~"  # Special character to mark end of message
    ascii_values = [ord(ch) for ch in message]

    height, width, _ = img.shape
    total_pixels = height * width * 3  # RGB channels
    
    if len(ascii_values) > total_pixels:
        print("Error: Message is too long for this image!")
        return None

    flat_image = img.flatten()
    
    # Encode message into pixels
    for i, value in enumerate(ascii_values):
        flat_image[i] = value

    # Reshape image to original shape
    encoded_img = flat_image.reshape(height, width, 3)
    
    # Save encrypted image
    cv2.imwrite("encoded_image.png", encoded_img)
    print("Encryption complete. Image saved as 'encoded_image.png'")

def decode_message(img, password):
    """Extracts a secret message from an image using pixel decoding."""
    
    flat_image = img.flatten()
    decoded_chars = []
    
    for pixel in flat_image:
        char = chr(pixel)
        if char == "~":  # Stop at delimiter
            break
        decoded_chars.append(char)

    return "".join(decoded_chars)

if __name__ == "__main__":
    option = input("Enter 'e' to encode or 'd' to decode: ").lower()

    if option == "e":
        img = cv2.imread("/Users/avi_chows/Downloads/Unknown.jpeg")  # Change image filename
        if img is None:
            print("Error: Image not found!")
        else:
            message = input("Enter the secret message: ")
            password = input("Set a passcode: ")
            encode_message(img, message, password)

    elif option == "d":
        img = cv2.imread("encoded_image.png")
        if img is None:
            print("Error: Encrypted image not found!")
        else:
            password = input("Enter passcode to decrypt: ")
            decrypted_msg = decode_message(img, password)
            print("Decrypted message:", decrypted_msg)
    
    else:
        print("Invalid input! Use 'e' for encoding or 'd' for decoding.")
