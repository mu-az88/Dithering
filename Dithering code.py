import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def load_image(image_path):
    image = Image.open(image_path).convert("L")   
    return np.array(image)


def random_dithering(image):
    noise = np.random.randint(-128, 128, image.shape)
    noisy_image = np.clip(image + noise, 0, 255)
    return noisy_image.astype(np.uint8)


def error_diffusion_dithering(image):
    height, width = image.shape
    processed_image = image.astype(float)

    for y in range(height):
        for x in range(width):
            old_pixel = processed_image[y, x]
            new_pixel = 255 if old_pixel > 127 else 0  
            processed_image[y, x] = new_pixel

            quant_error = old_pixel - new_pixel

            
            if x + 1 < width:
                processed_image[y, x + 1] += quant_error * (7 / 16)
            if y + 1 < height:
                if x - 1 >= 0:
                    processed_image[y + 1, x - 1] += quant_error * (3 / 16)
                processed_image[y + 1, x] += quant_error * (5 / 16)
                if x + 1 < width:
                    processed_image[y + 1, x + 1] += quant_error * (1 / 16)

    return np.clip(processed_image, 0, 255).astype(np.uint8)



def uniform_dithering(image):
    bayer_matrix = np.array([
        [0,   128],
        [192,  64]
    ]) / 256

    tile_size = bayer_matrix.shape[0]

  
    tiled_bayer = np.tile(
        bayer_matrix,
        (image.shape[0] // tile_size + 1, image.shape[1] // tile_size + 1)
    )

   
    tiled_bayer = tiled_bayer[:image.shape[0], :image.shape[1]]

   
    return (image > tiled_bayer * 255).astype(np.uint8) * 255



def display_images(original, random_dithered, error_dithered, uniform_dithered):

    fig, axes = plt.subplots(1, 4, figsize=(18, 5))
    titles = ["Original", "Random Dithering", "Error Diffusion", "Uniform Dithering"]
    images = [original, random_dithered, error_dithered, uniform_dithered]

    for ax, img, title in zip(axes, images, titles):
        ax.imshow(img, cmap="gray")
        ax.set_title(title)
        ax.axis("off")

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    image_path = "\images\Kitten.jpg"

    original_image = load_image(image_path)

    random_dithered = random_dithering(original_image)
    error_dithered = error_diffusion_dithering(original_image)
    uniform_dithered = uniform_dithering(original_image)

    display_images(original_image, random_dithered, error_dithered, uniform_dithered)
