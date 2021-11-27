# Install and import the required packages
# pip install pillow
from PIL import Image 
from pathlib import Path

# Function to create a mosaic from square images
# Based on the script created by the Python Brasil community
# https://rgth.co/pt-br/blog/criando-a-foto-oficial-da-python-brasil-2020/

def generate_image_mosaic(path,side=200,columns=16,rows=9,output_file="mosaic.jpg"):
    # path = Path to the folder containing the images
    # side = Side of the square images. Default is 200.
    # columns = Number of columns. Default is 16.
    # rows = Number of rows. Default is 9.
    # output_file = Output file name. Default is "mosaic.jpg".
    
    # Resize the images to the desired size
    resized_photos = [
        Image.open(photo).resize((side, side), Image.LANCZOS)
        for photo in Path(path).iterdir()
    ]

    # Create an empty image with the desired size
    mosaic = Image.new("RGB", (columns * side, rows * side))
    
    # Iterate over the files and paste them in the mosaic
    for x_item in range(columns):
        for y_item in range(rows):
            index = (columns * y_item + x_item) % len(resized_photos)
            mosaic.paste(
                resized_photos[index],
                (x_item * side, y_item * side)
            )

    # Save the mosaic
    mosaic.save(output_file)

    # Print the output filename and the total number of files used
    print(f"Mosaic created with {len(resized_photos)} files: {output_file}")


## Customized usage example:
# generate_image_mosaic("pictures_folder",side=100,columns=4,rows=3,output_file="my_mosaic.jpg")

## To use the default values (side=200,columns=16,rows=9,output_file="mosaic.jpg"), just call the function mentioning only the input folder:
generate_image_mosaic("pictures_folder")
