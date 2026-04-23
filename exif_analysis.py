# import the necessary modules
import helper
import exif
from exif import Image

# let the program know what file we are working with
with open('assets/exif_analysis/sunset.jpg', 'rb') as image_file:
    my_image = Image(image_file)
    
# printing the exif data
if my_image.has_exif:
    for property in my_image.list_all():
        print(f"{property} :  {my_image.get(property)}")

# What additional information do we have now that we've checked the EXIF?
