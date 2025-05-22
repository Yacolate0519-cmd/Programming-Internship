import sys
from glob import glob
from PIL import Image , ImageFilter , ImageEnhance

def showMenu():
    print('----------------')
    print('1. 等比縮放')
    print('2. 圖片旋轉')
    print('3. 產生縮圖')
    print('4. 套用濾鏡')
    print('0. 結束')

def resize(imgName , rate):
    try:
        image = Image.open(f'../imgs/{imgName}')
        imgW , imgH = image.size
        rate = float(rate)
        newW = int(imgW * rate)
        newH = int(imgH * rate)

        newImage = image.resize((newW, newH), Image.BILINEAR)

        dotIndex = imgName.index('.')
        newImageName = imgName[:dotIndex] + "_resized" + imgName[dotIndex: ]
        newImage.save(f'../results/{newImageName}')

    except FileNotFoundError as e:
        print(f'Error opening on: {e}')

def Vflip(imgName):
    try:
        image = Image.open(f'../imgs/{imgName}')
        newImage = image.transpose(Image.FLIP_TOP_BOTTOM)
        # newImage.show()
        dotIndex = imgName.index('.')
        newImageName = imgName[:dotIndex] + '_VFlip' + imgName[dotIndex: ]
        newImage.save(f'../results/{newImageName}')

    except FileNotFoundError as e:
        print(f'Error opening: {e}')
    
def Hflip(imgName):
    try:
        image = Image.open(f'../imgs/{imgName}')
        newImage = image.transpose(Image.FLIP_LEFT_RIGHT)
        # newImage.show()
        dotIndex = imgName.index('.')
        newImageName = imgName[:dotIndex] + '_HFlip' + imgName[dotIndex: ]
        newImage.save(f'../results/{newImageName}')

    except FileNotFoundError as e:
        print(f'Error opening: {e}')

def Rotate90(imgName):
    try:
        image = Image.open(f'../imgs/{imgName}')
        newImage = image.transpose(Image.ROTATE_90)
        # newImage.show()
        dotIndex = imgName.index('.')
        newImageName = imgName[:dotIndex] + '_HFlip' + imgName[dotIndex: ]
        newImage.save(f'../results/{newImageName}')

    except FileNotFoundError as e:
        print(f'Error opening: {e}')

def Rotate180(imgName):
    try:
        image = Image.open(f'../imgs/{imgName}')
        newImage = image.transpose(Image.ROTATE_180)
        # newImage.show()
        dotIndex = imgName.index('.')
        newImageName = imgName[:dotIndex] + '_HFlip' + imgName[dotIndex: ]
        newImage.save(f'../results/{newImageName}')

    except FileNotFoundError as e:
        print(f'Error opening: {e}')

def Rotate270(imgName):
    try:
        image = Image.open(f'../imgs/{imgName}')
        newImage = image.transpose(Image.ROTATE_270)
        # newImage.show()
        dotIndex = imgName.index('.')
        newImageName = imgName[:dotIndex] + '_HFlip' + imgName[dotIndex: ]
        newImage.save(f'../results/{newImageName}')

    except FileNotFoundError as e:
        print(f'Error opening: {e}')

def thumbnail(imgName , width , height):
    try:
        image = Image.open(f'../imgs/{imgName}')
        image.thumbnail((width , height))
        dotIndex = imgName.index('.')
        newImageName = imgName[:dotIndex] + '_thumbnail' + imgName[dotIndex: ]
        image.save(f'../results/{newImageName}')

    except FileNotFoundError as e:
        print(f'Error opening: {e}')

def Blur(imgName):
    try:
        image = Image.open(f'../imgs/{imgName}')
        image = image.filter(ImageFilter.BLUR)
        dotIndex = imgName.index('.')
        newImageName = imgName[:dotIndex] + '_BLUR' + imgName[dotIndex: ]
        image.save(f'../results/{newImageName}')

    except FileNotFoundError as e:
        print(f'Error opening: {e}')

def Contour(imgName):
    try:
        image = Image.open(f'../imgs/{imgName}')
        image = image.filter(ImageFilter.CONTOUR)
        dotIndex = imgName.index('.')
        imageNewName = imgName[:dotIndex] + '_CONTOUR' + imgName[dotIndex: ]
        image.save(f'../results/{imageNewName}')

    except FileNotFoundError as e:
        print(f'Error opening: {e}')

def Detail(imgName):
    try:
        image = Image.open(f'../imgs/{imgName}')
        image = image.filter(ImageFilter.DETAIL)
        dotIndex = imgName.index('.')
        newImageName = imgName[:dotIndex] + '_DETAIL' + imgName[dotIndex: ]
        image.save(f'../results/{newImageName}')

    except FileNotFoundError as e:
        print(f'Error opening: {e}')

def Edge_Enhance(imgName):
    try:
        image = Image.open(f'../imgs/{imgName}')
        image = image.filter(ImageFilter.EDGE_ENHANCE)
        # image.show()
        dotIndex = imgName.index('.')
        newImageName = imgName[:dotIndex] + '_EDGE_ENHANCE' + imgName[dotIndex: ]
        image.save(f'../results/{newImageName}')

    except FileNotFoundError as e:
        print(f'Error opening: {e}')

def Edge_Enhance_More(imgName):
    try:
        image = Image.open(f'../imgs/{imgName}')
        image = image.filter(ImageFilter.EDGE_ENHANCE_MORE)
        # image.show()
        dotIndex = imgName.index('.')
        newImageName = imgName[:dotIndex] + '_EDGE_ENHANCE_MORE' + imgName[dotIndex: ]
        image.save(f'../results/{newImageName}')

    except FileNotFoundError as e:
        print(f'Error opening: {e}')

def Emboss(imgName):
    try:
        image = Image.open(f'../imgs/{imgName}')
        image = image.filter(ImageFilter.EMBOSS)
        # image.show()
        dotIndex = imgName.index('.')
        newImageName = imgName[:dotIndex] + '_EMBOSS' + imgName[dotIndex: ]
        image.save(f'../results/{newImageName}')

    except FileNotFoundError as e:
        print(f'Error opening: {e}')
    
def Sharpen(imgName):
    try:
        image = Image.open(f'../imgs/{imgName}')
        image = image.filter(ImageFilter.SHARPEN)
        # image.show()
        dotIndex = imgName.index('.')
        newImageName = imgName[:dotIndex] + '_SHARPEN' + imgName[dotIndex: ]
        image.save(f'../results/{newImageName}')

    except FileNotFoundError as e:
        print(f'Error opening: {e}')

def Smooth(imgName):
    try:
        image = Image.open(f'../imgs/{imgName}')
        image = image.filter(ImageFilter.SMOOTH)
        # image.show()
        dotIndex = imgName.index('.')
        newImageName = imgName[:dotIndex] + '_SMOOTH' + imgName[dotIndex: ]
        image.save(f'../results/{newImageName}')

    except FileNotFoundError as e:
        print(f'Error opening: {e}')

def Smooth_More(imgName):
    try:
        image = Image.open(f'../imgs/{imgName}')
        image = image.filter(ImageFilter.SMOOTH_MORE)
        # image.show()
        dotIndex = imgName.index('.')
        newImageName = imgName[:dotIndex] + '_SMOOTH_MORE' + imgName[dotIndex: ]
        image.save(f'../results/{newImageName}')

    except FileNotFoundError as e:
        print(f'Error opening: {e}')

def FIND_EDGES(imgName):
    try:
        image = Image.open(f'../imgs/{imgName}')
        image = image.filter(ImageFilter.FIND_EDGES)
        # image.show()
        dotIndex = imgName.index('.')
        newImageName = imgName[:dotIndex] + '_FIND_EDGES' + imgName[dotIndex: ]
        image.save(f'../results/{newImageName}')

    except FileNotFoundError as e:
        print(f'Error opening: {e}')

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[2] == '-resize':
            resize(sys.argv[1] , sys.argv[3])
        
        if sys.argv[2] == '-VFlip':
            Vflip(sys.argv[1])

        if sys.argv[2] == '-HFlip':
            Hflip(sys.argv[1])

        if sys.argv[2] == '-R90':
            Rotate90(sys.argv[1])

        if sys.argv[2] == '-R180':
            Rotate180(sys.argv[1])

        if sys.argv[2] == '-R270':
            Rotate270(sys.argv[1])

        if sys.argv[2] == '-thumbnail':
            thumbnail(sys.argv[1] , int(sys.argv[3]) , int(sys.argv[4]))

        if sys.argv[2] == '-BLUR':
            Blur(sys.argv[1])

        if sys.argv[2] == '-CONTOUR':
            Contour(sys.argv[1])

        if sys.argv[2] == '-DETAIL':
            Detail(sys.argv[1])

        if sys.argv[2] == '-EDGE_ENHANCE':
            Edge_Enhance(sys.argv[1])

        if sys.argv[2] == '-EDGE_ENHANCE_MORE':
            Edge_Enhance_More(sys.argv[1])

        if sys.argv[2] == '-EMBOSS':
            Emboss(sys.argv[1])

        if sys.argv[2] == '-SHARPEN':
            Sharpen(sys.argv[1])

        if sys.argv[2] == '-SMOOTH':
            Smooth(sys.argv[1])

        if sys.argv[2] == '-SMOOTH_MORE':
            Smooth_More(sys.argv[1])

        if sys.argv[2] == '-FIND_EDGES':
            FIND_EDGES(sys.argv[1])        

    else:
        print("argument error")