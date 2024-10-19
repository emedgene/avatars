import os
import random
from PIL import Image, ImageDraw, ImageFont


def main():
    # Define the colors and text colors
    colors = [
        {'color': '#FEBEBD', 'textColor': 'black'},
        {'color': '#961B65', 'textColor': 'white'},
        {'color': '#440E39', 'textColor': 'white'},
        {'color': '#4669C7', 'textColor': 'white'},
        {'color': '#FCB73A', 'textColor': 'black'},
        {'color': '#F0712D', 'textColor': 'white'},
        {'color': '#194A46', 'textColor': 'white'},
        {'color': '#67B87A', 'textColor': 'black'},
        {'color': '#94D6CA', 'textColor': 'black'},
        {'color': '#1B898F', 'textColor': 'white'},
        {'color': '#F9F2E4', 'textColor': 'black'},
        {'color': '#A594D6', 'textColor': 'black'},
        {'color': '#DDDEF4', 'textColor': 'black'},
        {'color': '#DDF6F0', 'textColor': 'black'},
        {'color': '#119570', 'textColor': 'white'},
        {'color': '#D2E0DF', 'textColor': 'black'},
        {'color': '#904FAB', 'textColor': 'white'},
        {'color': '#FE76A2', 'textColor': 'white'},
        {'color': '#5B6A78', 'textColor': 'white'},
        {'color': '#D1D694', 'textColor': 'black'},
        {'color': '#77A7FC', 'textColor': 'black'},
        {'color': '#AD538A', 'textColor': 'white'},
        {'color': '#FEDCDC', 'textColor': 'black'},
        {'color': '#F2A293', 'textColor': 'black'},
        {'color': '#674CDD', 'textColor': 'white'},
        {'color': '#27BAE3', 'textColor': 'white'},
        {'color': '#365EBF', 'textColor': 'white'},
        {'color': '#9DBEFF', 'textColor': 'white'}
    ]

    # Create a directory to hold all images if it doesn't exist
    output_directory = "avatars"
    os.makedirs(output_directory, exist_ok=True)

    # Generate 40x40 images for each two-letter combination
    for first_letter in range(ord('A'), ord('Z') + 1):
        first_char = chr(first_letter)
        # Create a subdirectory for each starting letter
        subdir = os.path.join(output_directory, first_char)
        os.makedirs(subdir, exist_ok=True)
        
        for second_letter in range(ord('A'), ord('Z') + 1):
            second_char = chr(second_letter)
            text = f"{first_char}{second_char}"

            # Randomly choose a background and text color
            color_choice = random.choice(colors)
            background_color = color_choice['color']
            text_color = color_choice['textColor']

            # Create the image
            img = Image.new('RGB', (40, 40), background_color)
            draw = ImageDraw.Draw(img)
            
            # Set font size (adjusted for size) - you might need to adjust font path
            try:
                font = ImageFont.truetype("inter.woff2", 20)
            except IOError:
                print("issues!")
                # Fallback if the font is not available
                font = ImageFont.load_default()

            # Calculate text position (centered)
            bbox = draw.textbbox((0, 0), text, font=font)
            text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]
            position = ((40 - text_width - 1) // 2, (40 - text_height * 1.5) // 2)

            # Add the text to the image
            draw.text(position, text, fill=text_color, font=font)

            # Save the image to the appropriate directory
            img_path = os.path.join(subdir, f"{text}.png")
            img.save(img_path)

    print("Avatar images created successfully.")


if __name__ == '__main__':
    main()
