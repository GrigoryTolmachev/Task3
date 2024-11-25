import numpy as np
for q in range(3):
    from PIL import Image
    img = Image.open("lunar0"+str(q+1)+"_raw.jpg")
    data = np.array(img)
    k=data.max()-data.min()
    k=255/k
    data2=np.ones(data.shape)
    data2*=data.min()
    data2=data-data2
    data3=np.array(data2*k,dtype=np.uint8)
    res_img = Image.fromarray(data3)
    res_img.save("lunar0"+str(q+1)+".jpg")

