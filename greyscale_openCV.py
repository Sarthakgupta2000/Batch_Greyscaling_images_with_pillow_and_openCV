"""Batch convert images to greyscale .
Install dependencies:
  pip install pillow docopt
Note: If you do not provide an output path, the generated files will be saved
in a folder named "Converted"
Usage:
  greyscale.py <in_path> [<out_path>]
  greyscale.py -h | --help
  greyscale.py --version
Arguments:
  <in_path>   Input directory
  <out_path>  Output directory [default: ./Converted]
Options:
  -h, --help  Show this help screen.
  --version     Show version.
"""
import docopt
from PIL import Image
import glob
import os
import sys
import cv2
import time
import matplotlib.pyplot as plt


def process_image(in_path, out_path):
    image = cv2.imread(in_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    cv2.imwrite(out_path, gray_image)


def main(in_path, out_path):
    if not os.path.isdir(in_path):
        print('Error: <in_path> must be a directory', file=sys.stderr)
        return

    if out_path is None:
        dirname = os.path.dirname(in_path)
        out_path = dirname + 'Converted'

    if not os.path.exists(out_path):
        print('Creating directory', out_path)
        os.mkdir(out_path)

    x = []  # number of files
    y = []  # time taken to process number if files in x
    i = 0  # file counter
    start_time = time.time()
    x.append(i)  # marking origin
    end_time = time.time()
    y.append(end_time - start_time)  # marking origin time for better graph view

    for in_file in glob.glob(in_path + '/*'):
        filename = os.path.basename(in_file)
        _, ext = os.path.splitext(filename)

        if (not os.path.isfile(in_file) or
                ext[1:] not in ['jpg', 'jpeg', 'gif', 'png']):
            print('Skipping', filename)
            continue
        # else:
            # print('Processing', filename)

        out_file = out_path + '/' + filename
        process_image(in_file, out_file)
        if i in [999, 1999, 2999, 3999, 4999, 5999, 6999, 7999, 8999, 9999, 10239]:
            x.append(i)
            end_time = time.time()
            y.append(end_time - start_time)
        i += 1
    plt.plot(x, y, 'ko-')
    plt.xlabel('Number of files(approx 10-15kb each) -> ')
    plt.ylabel('Time taken (s) ->')
    plt.title(label="using openCV", fontsize=15, color="red")
    plt.show()


if __name__ == '__main__':
    args = docopt.docopt(__doc__, version='Greyscale converter v2.0')
    main(args['<in_path>'], args['<out_path>'])
