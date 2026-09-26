import streamlit as st
import math
from PIL import Image, ImageOps, ImageDraw

def get_star_icon(image_path):
    img = Image.open(image_path).convert("RGBA")
    size = min(img.size)
    img = ImageOps.fit(img, (size, size))
    
    cx, cy = size / 2, size / 2
    r_outer = size / 2
    r_inner = r_outer * 0.7
    num_points = 8
    
    star_coordinates = []
    for i in range(2 * num_points):
        r = r_outer if i % 2 == 0 else r_inner
        angle = i * math.pi / num_points - math.pi / 2
        x = cx + r * math.cos(angle)
        y = cy + r * math.sin(angle)
        star_coordinates.append((x, y))
        
    mask = Image.new("L", (size, size), 0)
    draw = ImageDraw.Draw(mask)
    draw.polygon(star_coordinates, fill=255)
    

    star_img = Image.new("RGBA", (size, size))
    star_img.paste(img, (0, 0), mask=mask)
    return star_img
    
star_icon = get_star_icon("Crossy_Road_icon.jpeg")


st.set_page_config(
    page_title="Crossy Road",
    page_icon=star_icon
)

st.title("Crossy Road Hacker")
st.write("By *ghostpes*  \n:grey[Uses Gemini by Google]")
