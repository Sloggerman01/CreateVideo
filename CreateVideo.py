import os
import cv2


path = "Images"

images = []


for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

               
        images.append(file_name)
        
img  = cv2.imread(images[0])
h,w,c = img.shape
print(h,w,c)
out  = cv2.VideoWriter("Friends.mp4", cv2.VideoWriter_fourcc(*"DIVX"), 30,(1280,720))


for i in range(0, len(images)):
    img  = cv2.imread(images[i])
    out.write(img)
out.release()
cv2.waitKey(0)



