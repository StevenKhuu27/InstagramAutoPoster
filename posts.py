from PIL import Image, ImageDraw, ImageFont
import textwrap
import datetime
import os
def create_image(quote):
    # Create an image
    out = Image.new("RGB", (1080, 1080), (255, 245, 238))
    # Grabs font from the fonts dir
    font = ImageFont.truetype('./fonts/Junge-Regular.ttf', 60)
    font_auth = ImageFont.truetype('./fonts/Quicksand-VariableFont_wght.ttf', 60)
    text_colour = (40, 77, 35)

    # Get a drawing context for the text and author name
    d = ImageDraw.Draw(out)
    d_auth = ImageDraw.Draw(out)
    # Text to be drawn
    max_width = 27  # Maximum number of characters per line
    # We wrap the text for multi line quotes, without this it will flow off the iamge.
    wrapped_text = textwrap.fill(quote['quote'], width=max_width)
    wrapped_author = textwrap.fill(quote['author'], width=max_width)
    # Calculate coordinates for centered text
    bbox = d.textbbox((0, 0), wrapped_text, font_size=60, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    # x and y coordinates for the text boxes
    x = (out.width - text_width) / 2
    y = (out.height - text_height) / 2
    # y2 is for the author text box to sit right under neath the quote
    y2 = (out.height + text_height + 100) / 2
    # Draw multiline text
    d.multiline_text((x, y), wrapped_text, fill=text_colour, font_size=60, font=font)
    d_auth.multiline_text((x, y2), wrapped_author, fill=text_colour, font_size=60, font=font_auth)

    # Display the image
    out.show()
    date_str = datetime.date.today().strftime('%Y-%m-%d')
    # Using this for Github Actions
    path = 'posts'
    # file_path = os.path.join('/app/posts', f'{date_str}.jpeg')
    # Using this for Local Run
    # path = 'C:/Users/Steven/Documents/All things Code/Insta Poster/posts'
    # Using this for DockerFile
    # path = '/app/posts'
    image_path = os.path.join(path, f'{date_str}.jpeg')

    out.save(image_path)
#     