from PIL import Image
name = input("image name...")
img = Image.open(name) # create the pixel map
out = " sensibility "+name
limiter = int(input("lower sensibility (hight number, higher than 0)..."))
ran = int(input("higher sensibility (lower number, higher than 0)..."))
for limit in range(limiter, ran+1):
    img_data = [(255, 255, 255)]
    first = True
    for j in range(img.size[1]): # for every pixel:
        for i in range(img.size[0]):
            if not first:
                for a in range(3):
                    if list(img.getpixel((i, j)))[a] <= list(old)[a] + limit and list(img.getpixel((i, j)))[a] >= list(old)[a] - limit:
                        img_data.append((255, 255, 255))
                        break
                    elif a == 2:
                        img_data.append((0, 0, 0))
            first = False
            old = img.getpixel((i, j))
    newim = Image.new(img.mode,img.size)
    newim.putdata(img_data)
    newim.save(str(limit)+out)