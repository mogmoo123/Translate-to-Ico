import easygui as eg
import cv2
from PIL import Image

input_path = eg.fileopenbox(
    title= "open file",
    filetypes= ["*.png", "*.jpg", "*.gif"]
)
output_path = eg.filesavebox(
    title= "output path",
    filetypes= ["*.ico"]
)
try:
    img = cv2.imread(input_path)
    img = cv2.resize(img,(300,300))
    cv2.imshow(winname="image",mat=img)
    file_new = Image.open(fp=input_path)
    file_new.save(fp=output_path+'.ico',format='ico')
except:
    print("파일을 선택해주세요.")
cv2.waitKey(0)
cv2.destroyAllWindows()
