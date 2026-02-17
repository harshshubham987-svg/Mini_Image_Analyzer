image = [
    [12, 45, 200],
    [34, 255, 90],
    [123, 67, 89]
]

row = len(image)
col = len(image[0])

print("Image Dimensions: ",row," x ",col)
print("Total Pixels:- ",row*col)

# == Total Sum + Average 

total = 0
for row in range(len(image)):
    for col in range(len(image[0])):
        total += image[row][col]

ave = total/(row*col)

print("Total Intensity :- ",total)
print("Average Intensity :- ",ave)

# -- Brightest & Darkest Pixel

bright = image[0][0]
dark = image[0][0]

for row in range(len(image)):
    for col in range(len(image[0])):
        if image[row][col] > bright:
            bright = image[row][col]
        if image[row][col] < dark:
            dark = image[row][col]
print("Brightness Pixel :- ",bright)
print("Drakest Pixel :- ",dark)

#-- Row-wise Brightness

for i in range(len(image)):
    row_sum = 0
    for j in range(len(image[0])):
        row_sum += image[i][j]
    print("Row ",i," Brightness :- ",row_sum)

#-- Diagonal Intensity
dig_sum = 0
for i in range (len(image)):
    dig_sum += image[i][i]

print("Diagonal Intensity :- ",dig_sum)

# -- Inverted Image
new_image = []
for i in range(len(image)):
    new_pixel = []
    for j in range(len(image[0])):
        new_pixel.append(255 - image[i][j])
    new_image.append(new_pixel)

print("Inverted Image")
for row in new_image:
    print (row)
