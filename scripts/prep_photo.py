from PIL import Image, ImageEnhance
import cv2
import numpy as np
from rembg import remove
import sys


def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts/prep_photo.py source-photo.jpeg")
        return

    input_path = sys.argv[1]

    print("Loading image...")
    image = Image.open(input_path).convert("RGBA")

    print("Removing background...")
    image = remove(image)

    # White background
    background = Image.new("RGBA", image.size, "white")
    background.alpha_composite(image)

    # Convert to grayscale
    gray = background.convert("L")

    # Convert to OpenCV
    img = np.array(gray)

    # CLAHE for local contrast
    clahe = cv2.createCLAHE(
        clipLimit=2.0,
        tileGridSize=(8, 8)
    )

    enhanced = clahe.apply(img)

    # Slight contrast enhancement
    enhanced = Image.fromarray(enhanced)

    enhancer = ImageEnhance.Contrast(enhanced)
    enhanced = enhancer.enhance(1.4)

    enhanced.save("source-prepped.png")

    print("Created source-prepped.png")


if __name__ == "__main__":
    main()
