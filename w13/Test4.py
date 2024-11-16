def white_to_black(image , row , col):
    if row < 0 or row >= len(image) or col < 0 or col >= len(image[0]) or image[row][col] != 0:
        return 
    image[row][col] = 2
    white_to_black(image , row + 1, col)
    white_to_black(image , row - 1, col)
    white_to_black(image , row , col + 1)
    white_to_black(image , row , col - 1)
    return image
image = [[0,0,1,0],
         [1,0,1,0],
         [0,0,0,1],
         [0,1,1,0]]

kernel = [1,1]

white_to_black(image , kernel[0] , kernel[1])
for i in image:
    print(i)