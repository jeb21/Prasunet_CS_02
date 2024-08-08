from PIL import Image

def encrypt_image(input_image_path, output_image_path):
    # Open the image
    with Image.open(input_image_path) as img:
        # Convert the image to RGB mode
        img = img.convert("RGB")
        # Get the size of the image
        width, height = img.size

        # Load the pixel data
        pixels = img.load()

        # Swap the red and blue pixels
        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x, y]
                pixels[x, y] = (b, g, r)

        # Save the encrypted image
        img.save(output_image_path)

def decrypt_image(input_image_path, output_image_path):
    # Open the image
    with Image.open(input_image_path) as img:
        # Convert the image to RGB mode
        img = img.convert("RGB")
        # Get the size of the image
        width, height = img.size

        # Load the pixel data
        pixels = img.load()

        # Swap the red and blue pixels back
        for x in range(width):
            for y in range(height):
                b, g, r = pixels[x, y]
                pixels[x, y] = (r, g, b)

        # Save the decrypted image
        img.save(output_image_path)

# Example usage:
encrypt_image('demo.jpg', 'encrypted_image.jpg')
decrypt_image('encrypted_image.jpg', 'decrypted_image.jpg')