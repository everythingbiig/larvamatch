from PIL import Image
import imagehash
import os
import numpy as np

hash_size = 8
def find_similar(image1,image_folder,similarity=75):
    fnames = os.listdir(image_folder)
    threshold = 1 - similarity/100
    diff_limit = int(threshold*(hash_size**2))
    
    with Image.open(image1) as img:
        hash1 = imagehash.average_hash(img, hash_size).hash
    
    print("Finding Similar Images to {} Now!\n".format(image1))
    for image in fnames:
        with Image.open(os.path.join(image_folder,image)) as img:
            hash2 = imagehash.average_hash(img, hash_size).hash
            
            if np.count_nonzero(hash1 != hash2) <= diff_limit:
                print("{} image found to be at least {}% similar to {}".format(image,similarity,image1))

find_similar("LarvaLad1966.jpg", "resized_images")