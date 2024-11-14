import pandas as pd
from PIL import Image, ImageDraw
import os

def create_card(front_text, back_text, front_color, back_color, card_name, output_dir):
    card_size = (400, 600)  # Width x Height

    # Create front of card
    front_img = Image.new("RGB", card_size, front_color)
    draw = ImageDraw.Draw(front_img)

    # Center front text
    w, h = draw.textsize(front_text)
    draw.text(((card_size[0] - w) / 2, (card_size[1] - h) / 2), front_text, fill="black")

    # Save front image
    front_img.save(os.path.join(output_dir, f"{card_name}_front.jpg"))

    # Create back of card
    back_img = Image.new("RGB", card_size, back_color)
    draw = ImageDraw.Draw(back_img)

    # Center back text
    w, h = draw.textsize(back_text)
    draw.text(((card_size[0] - w) / 2, (card_size[1] - h) / 2), back_text, fill="black")

    # Save back image
    back_img.save(os.path.join(output_dir, f"{card_name}_back.jpg"))

def main():
    # Load CSV
    csv_path = "cards.csv"  # Path to your CSV file
    output_dir = "cards_output"
    os.makedirs(output_dir, exist_ok=True)

    df = pd.read_csv(csv_path)

    # Loop through each row and create card images
    for idx, row in df.iterrows():
        front_text = row['Effect']
        back_text = row['Cards']
        front_color = row['Front Color']
        back_color = row['Back Color']
        card_name = f"card_{idx}"

        create_card(front_text, back_text, front_color, back_color, card_name, output_dir)

if __name__ == "__main__":
    main()