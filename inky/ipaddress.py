#!/usr/bin/env python3

import socket
import requests
from inky.auto import auto
from PIL import Image, ImageDraw, ImageFont

def get_local_ip():
    """Get the local IP address of the machine"""
    try:
        # Create a socket connection to determine the local IP
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # Doesn't need to be a real connection
        s.connect(('8.8.8.8', 1))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except Exception as e:
        return f"Error: {str(e)}"

def get_external_ip():
    """Get the external IP address of the machine"""
    try:
        # Use a public API to fetch the external IP
        response = requests.get('https://api.ipify.org')
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    # Get IP addresses
    local_ip = get_local_ip()
    external_ip = get_external_ip()
    
    # Initialize the Inky display using auto detection
    inky_display = auto()
    inky_display.set_border(inky_display.WHITE)
    
    # Create a blank canvas
    img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT), inky_display.WHITE)
    draw = ImageDraw.Draw(img)
    
    body_size = 14
    small_size = 12

    # Load a font
    try:
        # Try to use a nice font if available
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", body_size)
        small_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", small_size)
    except:
        # Fall back to default font if necessary
        font = ImageFont.load_default()
        small_font = ImageFont.load_default()
       
    # Draw IP addresses with tighter spacing for small display
    draw.text((5, 5), f"Local IP:", inky_display.BLACK, font=small_font)
    draw.text((5, 20), f"{local_ip}", inky_display.BLACK, font=font)
    
    draw.text((5, 40), f"External IP:", inky_display.BLACK, font=small_font)
    draw.text((5, 55), f"{external_ip}", inky_display.BLACK, font=font)
    
    # Update the display with the image
    inky_display.set_image(img)
    inky_display.show()

if __name__ == "__main__":
    main()
