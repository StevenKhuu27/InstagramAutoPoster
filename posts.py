from PIL import Image, ImageDraw, ImageFont
import textwrap
import datetime
import os
def create_image(quote):
    # Create an image
    out = Image.new("RGB", (1080, 1080), (255, 245, 238))
    font = ImageFont.truetype('./fonts/Junge-Regular.ttf', 60)
    font_auth = ImageFont.truetype('./fonts/Quicksand-VariableFont_wght.ttf', 60)
    text_colour = (40, 77, 35)

    # Get a drawing context
    d = ImageDraw.Draw(out)
    d_auth = ImageDraw.Draw(out)

    # Text to be drawn
    # text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris at tortor commodo, congue erat ac, mattis ex. Aenean tempus nibh dolor, sit amet rhoncus tellus convallis et. Sed hendrerit vitae purus quis accumsan. Vestibulum luctus, felis commodo condimentum posuere, lacus nisi tincidunt justo, eu posuere felis neque eu eros. Donec interdum erat sed nibh rhoncus bibendum. Nunc fringilla ante neque, at posuere odio interdum vel. Integer eget tellus posuere, gravida eros eu, mattis magna."
    # text =  data[0]['q']
    # author = data[0]['a']
    max_width = 27  # Maximum number of characters per line
    wrapped_text = textwrap.fill(quote['quote'], width=max_width)
    wrapped_author = textwrap.fill(quote['author'], width=max_width)
    # Calculate coordinates for centered text
    bbox = d.textbbox((0, 0), wrapped_text, font_size=60, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    x = (out.width - text_width) / 2
    y = (out.height - text_height) / 2
    y2 = (out.height + text_height + 100) / 2
    # Draw multiline text
    d.multiline_text((x, y), wrapped_text, fill=text_colour, font_size=60, font=font)
    d_auth.multiline_text((x, y2), wrapped_author, fill=text_colour, font_size=60, font=font_auth)

    # Display the image
    out.show()
    date_str = datetime.date.today().strftime('%Y-%m-%d')
    local_path = 'C:/Users/Steven/Documents/All things Code/Insta Poster/posts'
    file_path = os.path.join(local_path, f'{date_str}.jpeg')
    # file_path = os.path.join('/app/posts', f'{date_str}.jpeg')

    out.save(file_path)
#     docker run -d -p 80:80 -v "C:\Users\Steven\Documents\All things Code\Insta Poster\posts:/app/posts" my-python-app