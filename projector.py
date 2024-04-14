import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
plt.rcParams['figure.dpi']=100

def operation(img, A, beta):
    
    xy_plane = []
    result = np.ones(img.shape)*255

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            
            xy_plane.append(A@((np.array([i,j]).reshape(-1,1))+ beta*img.shape[0]))
            result[int(xy_plane[-1][1]),int(xy_plane[-1][0])] = img[j,i]
    
    return result
           
    
def serpinski(img,iterations):
    A = np.array([.5,0,0,.5]).reshape(2,2)
    b1 = np.array([0,1]).reshape(-1,1)
    b2 = np.array([1,1]).reshape(-1,1)
    b3 = np.array([.5,0]).reshape(-1,1)
    result = [img]
    for i in range(iterations):
        img1 = operation(img,A,b1)
        img2 = operation(img,A,b2)
        img3 = operation(img,A,b3)
        img = (img1+img2+img3)/3
        result.append(img)
    return result

def subplot(images):
    n = len(images)
    
    fig,ax = plt.subplots(1,n)

    for i in range(n):
        ax[i].imshow(images[i],cmap = "gray")
        ax[i].axis("off")
# axe[0].imshow(triangle,cmap = "gray")
# axe[1].imshow(operation(triangle,np.array([[.5,0],[0,.5]]),np.array([0.5,0]).reshape(-1,1)),cmap="gray")

if __name__ == "__main__":
    #Input image should be square (preferred 256 x 256), image with white background is preffered
    img = "monkey.gif"
    try:
        triangle = np.mean(np.array(Image.open(img)),axis = 2)
    except:
        triangle = np.array(Image.open(img))
    
    triangle = np.random.randint(0,255,(256,256))
    images = serpinski(triangle,5)
    subplot(images)
    plt.show()