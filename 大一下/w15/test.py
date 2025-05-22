from PIL import Image
import sys
from glob import glob

def jpeg2png(oldImage , newImage):
    try:
        image = Image.open(f'../imgs/{oldImage}')
        image.save(f'../results/{newImage}')
    except FileNotFoundError as e:
        print('Error opening as: {e}')
    
def png2jpeg(oldImage , newImage):
    try:
        image = Image.open(f'../imgs/{oldImage}')
        image.save(f'../results/{newImage}')
    except FileNotFoundError as e:
        print('Error opening as: {e}')

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == '-png2jpeg':
            png2jpeg('Fig01.png' , 'Fig01_result.jpeg')
        elif sys.argv[1] == '-jpeg2png':
            jpeg2png('Fig01.jpeg' , 'Fig01_result.png')