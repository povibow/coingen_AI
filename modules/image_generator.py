from PIL import Image, ImageDraw, ImageFont
import numpy as np

def generate_logo(coin_name):
    """
    Generate a simple logo for a coin using PIL.
    The function generates an image with the coin name at its center.
    """
    # Create an empty image with white background
    img_size = (400, 400)
    background_color = (255, 255, 255)
    img = Image.new("RGB", img_size, background_color)
    
    # Create drawing context
    draw = ImageDraw.Draw(img)
    
    # Draw a simple circle
    circle_color = (0, 102, 204)  # Example blue color
    circle_center = (img_size[0] // 2, img_size[1] // 2)
    circle_radius = 150
    draw.ellipse((circle_center[0] - circle_radius, circle_center[1] - circle_radius,
                  circle_center[0] + circle_radius, circle_center[1] + circle_radius),
                 fill=circle_color)

    # Add coin name text
    font = ImageFont.load_default()
    text_color = (255, 255, 255)
    text_size = draw.textsize(coin_name, font=font)
    draw.text((circle_center[0] - text_size[0] // 2, circle_center[1] - text_size[1] // 2),
              coin_name, fill=text_color, font=font)

    return img
