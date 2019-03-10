from PIL import Image
import random

def open_image(path):
    newImage = Image.open(path)
    return newImage

def save_image(image, path):
    image.save(path, 'png')

def create_image(i, j):
    image = Image.new("RGB", (i, j), "white")
    return image

def get_pixel(image, i, j):
    width, height = image.size
    if i > width or j > height:
        return None
    pixel = image.getpixel((i, j))
    return pixel

def randShapesInPic(image,        # image to change
                    pat_length,   # consecutive pixels in a row that will be modified 
                    pat_depth,    # pixels below (how thick) the length will be
                    ran_space_btw,# the max amount away one bar is away from another horizontally
                    rsh, gsh, bsh,# pass in the amount you want to vary each pixel color/shade by: the difference of this val
                                  # and the image pixel is the new pixel color/shade
                    ranCol_flag): # 0, 1 or 2, 1: all r,g,b are set to the same random constant between 1 and whatever
                                  # number you feed in to the rsh param. The original img pixel is subtracted from this
                                  # rand value (actually I take the abs value so really the difference) and this difference
                                  # becomes the new pixel color for that r or g or b rgb value. If 2 is the param, it
                                  # randomizes this for all three of the rsh, gsh, bsh params so now instead of them being
                                  # all the same rand difference from the original pixel, they are/could be all different
                                  # numbers so different differences creating more color randomness in the img at that pixel.
                                  # if you just want to give it three values and not have any randomizer set param to 0 or anything
                                  # that isn't a 1 or 2. Those three values are your normal rsh, gsh, bsh params to begin with.
    r = rsh
    g = gsh
    b = bsh
    if (ranCol_flag == 1):
        r = random.randint(1, rsh)  # all same const
        g = r
        b = r
    elif (ranCol_flag == 2):  # all diff colors
        r = random.randint(1, rsh)
        g = random.randint(1, gsh)
        b = random.randint(1, bsh)
    w, h = image.size
    new = create_image(w, h)
    pixels = new.load()
    rowSum = random.randint(0, ran_space_btw)
    deep = 1
    saveAr = []
    for i in range(h):
        leng = pat_length
        if (i == int(h*.25) ) :
            print("... 25%")
        elif (i == int(h*.5) ) :
            print("... 50%")
        elif (i == int(h*.75) ) :
            print("... 75%")
        if (deep == 1):
            saveAr = []
            rowSum = random.randint(0, ran_space_btw)
            saveAr.append(rowSum)
            deep = pat_depth
        else:
            deep -= 1
        counter = 0
        for j in range(w):
            pixel = image.getpixel((j, i))
            red = pixel[0]
            green = pixel[1]
            blue = pixel[2]
            if deep == pat_depth:
                if (j == rowSum and leng > 1):
                    rowSum += 1
                    saveAr.append(rowSum)
                    leng -= 1
                    if (ranCol_flag == 1):
                        r = random.randint(1, rsh) #all same const
                        g = r
                        b = r
                    elif (ranCol_flag == 2): #all diff colors
                        r = random.randint(1, rsh)
                        g = random.randint(1, gsh)
                        b = random.randint(1, bsh)
                    pixels[j, i] = (abs(r - red), abs(g - green), abs(b - blue))
                elif (j == rowSum and leng == 1):
                    rowSum += random.randint(1, ran_space_btw)
                    saveAr.append(rowSum)
                    leng = pat_length
                    if (ranCol_flag == 1):
                        r = random.randint(1, rsh) #all same const
                        g = r
                        b = r
                    elif (ranCol_flag == 2): #all diff colors
                        r = random.randint(1, rsh)
                        g = random.randint(1, gsh)
                        b = random.randint(1, bsh)
                    pixels[j, i] = (abs(r - red), abs(g - green), abs(b - blue))
                else:
                    pixels[j, i] = (red, green, blue)
            else:
                if (saveAr[counter] == j):
                    pixels[j, i] = (abs(r - red), abs(g - green), abs(b - blue))
                    counter += 1
                else:
                    pixels[j, i] = (red, green, blue)
    print("... 100%")
    return new


#example method for changing images pixels
def makeART(im0):
    im1 = randShapesInPic(im0, 20, 20, 500, 5, 5, 5, 0)
    im2 = randShapesInPic(im1, 10, 5, 100, 255, 255, 255, 2)
    im3 = randShapesInPic(im2, 5,  35, 300, 15, 15, 15, 1) #1=rand col in range (all same diff), 2=rand and all diff

    # create a random name for the img so does not potentially overwrite an existing one
    name = ""
    for i in range(15):
        name = name + str(random.randint(1, 9))

    im3.save("made_pics/" + name + '.png')
    im3.show()

# example list of images
pics = ["plane1.jpeg", "car.jpg", "sky.jpeg", "person.jpg", ]


def doBunch(lst):
    a = lst[:]
    print(a) #list of images to change
    while a:
        x = random.randint(0, len(a)-1)
        print(a[x])
        makeART( Image.open(a[x]) )
        a.pop(x)
        print(a)


def randShapesInPicTester(pat_length, pat_depth, rand_space_betw):
    w = 15
    h = 15
    deep = 1
    for i in range(w):
        leng = pat_length
        if (deep <= 1):
            saveAr = []
            rowSum = random.randint(0, rand_space_betw)
            saveAr.append(rowSum)
            deep = pat_depth
        else:
            deep = deep - 1
        counter = 0
        for j in range(h):
            if deep == pat_depth:
                if (j == rowSum and leng > 1):
                    rowSum = rowSum + 1
                    saveAr.append(rowSum)
                    leng = leng - 1
                    print(" O", end="")
                elif (j == rowSum and leng == 1):
                    rowSum = rowSum + random.randint(0, rand_space_betw)
                    saveAr.append(rowSum)
                    leng = pat_length
                    print(" O", end="")
                else:
                    print(" .", end="")
            else:
                if (saveAr[counter] == j):
                    print(" O", end="")
                    counter = counter + 1
                else:
                    print(" .", end="")
        print("")
