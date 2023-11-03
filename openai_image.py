import openai
import base64
from config import openai_key
import matplotlib.pyplot as plt
from PIL import Image
import io

def generate_image (prompt: str) -> bytes:
    openai.api_key = openai_key
    response = openai.Image.create(
        prompt=f"{prompt}",
        n=1,
        size="512x512",
        response_format='b64_json'
    )
    return response['data'][0]['b64_json']

def plot_image (b64_image_data: bytes) -> None:
    image_data = base64.b64decode(b64_image_data)

    image = Image.open(io.BytesIO(image_data))
    image.save("imagem_1.jpg")
    plt.imshow(image)
    plt.axis('off')
    plt.show()

def main () -> None:
    response = generate_image("data analytics pie chart")
    plot_image(response)

if __name__ == "__main__":
    main()