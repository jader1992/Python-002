import requests
import os
from PIL import Image
import pytesseract

#下载图片
# session = requests.Session()
# img_url = 'https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=1320441599,4127074888&fm=26&gp=0.jpg'
# user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
#
# headers = {
#     "User-Agent": user_agent
# }
#
# r = session.get(img_url, headers=headers)
#
# with open('cap.jpg','wb') as f:
#     f.write(r.content)

#打开并显示图片
cap = Image.open('cap.jpg')
cap.show()

#灰度图片
gray = cap.convert('L')
gray.save('c_gray.jpg')
cap.close()

#二值化
threshold = 100
table = []

for i in range(256):
    if i<threshold:
        table.append(0)
    else:
        table.append(1)

out = gray.point(table, '1')
out.save('c_th.jpg')

th = Image.open('c_th.jpg')
print(pytesseract.image_to_string(th, lang='chi_sim+eng'))

# 各种语言识别库 https://github.com/tesseract-ocr/tessdata
# 放到 /usr/local/Cellar/tesseract/版本/share/tessdata