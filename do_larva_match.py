from PIL import Image
import imagehash
import os
import numpy as np


hash_size = 8

LARVA_DIR = "larvas"
PUNK_DIR = "punks"

def scale_image(image):
    # TODO ensure image is 256x256
    return



def find_similar(source_image_dir=LARVA_DIR,target_image_dir=PUNK_DIR,similarity=75):
    threshold = 1 - similarity/100
    diff_limit = int(threshold*(hash_size**2))

    source_image_fnames = os.listdir(source_image_dir)
    
    for source_image_fname in source_image_fnames:
        similar = 0;
        with Image.open(os.path.join(source_image_dir,source_image_fname)) as source_image:
            source_image_hash = imagehash.average_hash(source_image, hash_size).hash

            target_image_fnames = os.listdir(target_image_dir)

            print("Finding {} that are similar to {}".format(target_image_dir, source_image_fname))
            for target_image_fname in target_image_fnames:
                with Image.open(os.path.join(target_image_dir,target_image_fname)) as target_image:
                    target_image_hash = imagehash.average_hash(target_image, hash_size).hash
                    
                    if np.count_nonzero(source_image_hash != target_image_hash) <= diff_limit:
                        print("{} is similar to {}".format(target_image_fname,source_image_fname))
                        similar+=1
            print("Found {} similar {}".format(similar, target_image_dir))

def findmypunks():
    find_similar(source_image_dir=LARVA_DIR, target_image_dir=PUNK_DIR, similarity=77)

def findmylarvas():
    find_similar(source_image_dir=PUNK_DIR, target_image_dir=LARVA_DIR)


findmypunks()