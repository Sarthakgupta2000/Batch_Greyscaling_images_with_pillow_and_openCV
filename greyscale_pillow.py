"""
This is a script for converting multiple random colored images to greyscale using the Pillow library 

run command - $python greyscale.py <inputFolderName> <outputFolderName>

checkpoints are added manually according to need

code for automatic checkpoints is also added but commented - uncomment to use it

"""

import argparse
import os.path
import sys
import glob
from PIL import Image
import time
import matplotlib.pyplot as plt


def rgb2grey(in_path, out_path):
    """
    function that converts given image file to greyscale using Pillow's inbuilt convert function 

    When translating a color image to greyscale (mode “L”), the library uses the ITU-R 601-2 luma transform:

    L = R * 299/1000 + G * 587/1000 + B * 114/1000

    """
    image = Image.open(in_path)
    grey = image.convert('L')
    grey.save(out_path)


def main(source_dir, target_dir):

    # check if source_dir exists otherwise give error
    if not os.path.isdir(source_dir):
        print("Error: '%s' must be a directory" % source_dir, file=sys.stderr)
        return

    x = []  # number of files
    y = []  # time taken to process number if files in x
    i = 0  # file counter
    start_time = time.time()
    x.append(i)  # marking origin
    end_time = time.time()
    y.append(end_time - start_time)  # marking origin time for better graph view

    # iterate through each file of the source_dir
    for in_file in glob.glob(source_dir + '/*'):
        filename = os.path.basename(in_file)  # filename.extension
        _, ext = os.path.splitext(filename)  # splits into file name & extension( e.g ".jpeg") - don't forget the dot

        # check file extension for appropriate file formats
        if not os.path.isfile(in_file) or ext[1:] not in ['jpg', 'jpeg', 'gif', 'png']:
            print('Skipping', filename)
            continue
        # else:
            # print('Processing', filename)
        # make path with the same file name in target directory
        out_file = target_dir + '/' + filename

        rgb2grey(in_file, out_file)

        """
        if i in range(1, len(glob.glob(source_dir + '/*'))):
            x.append(i)
            end_time = time.time()
            y.append(end_time - start_time)
        i += 1

        """
        if i in [999, 1999, 2999, 3999, 4999, 5999, 6999, 7999, 8999, 9999, 10239]:
            x.append(i)
            end_time = time.time()
            y.append(end_time - start_time)
        i += 1
    plt.plot(x, y, 'ko-')
    plt.xlabel('Number of files(approx 10-15kb each) -> ')
    plt.ylabel('Time taken (s) ->')
    plt.title(label="Using Pillow", fontsize=15, color="red")
    plt.show()


if __name__ == '__main__':
    # parses the positional arguments for exactly two values
    parser = argparse.ArgumentParser(description='get directory paths ')
    parser.add_argument("source_dir")
    parser.add_argument("target_dir")
    args = parser.parse_args()
    main(args.source_dir, args.target_dir)
