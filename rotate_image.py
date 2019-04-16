"""
    You are given an n x n 2D matrix that represents an image.
    Rotate the image by 90 degrees (clockwise).

    === Example ===
        for:

        a = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]


        the output should be:

        rotateImage(a) = [[7, 4, 1],
                          [8, 5, 2],
                          [9, 6, 3]]
"""

def rotate_image(image):
    if len(image) > 1:
        image = list(zip(*image))
        image = [list(i[::-1]) for i in image]
    return image


if __name__ == '__main__':
    a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    b = [1]
    c = [[10, 9, 6, 3, 7], [6, 10, 2, 9, 7], [7, 6, 3, 8, 2],
         [8, 9, 7, 9, 9],  [6, 8, 6, 8, 2]]

    # tests     
    print(rotate_image(a))
    print(rotate_image(b))
    print(rotate_image(c))
