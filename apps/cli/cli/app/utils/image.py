from pathlib import Path

from colorama import Fore, Style
from PIL import Image


def render_image(image_path: Path) -> None:
    img = Image.open(image_path)
    width, height = img.size

    terminal_width = 80
    aspect_ratio = height / width
    new_width = terminal_width
    new_height = int(terminal_width * aspect_ratio)
    img = img.resize((new_width, new_height))

    img = img.convert("L")
    ascii_chars = "@#*. "

    pixels = img.getdata()
    ascii_str = [ascii_chars[pixel // (256 // len(ascii_chars))] for pixel in pixels]
    ascii_str = "".join(ascii_str)

    for i in range(0, len(ascii_str), terminal_width):
        row = ascii_str[i : i + terminal_width]
        colored_row = [f"{Fore.GREEN}{char}{Style.RESET_ALL}" for char in row]
        print("".join(colored_row))
