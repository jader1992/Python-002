### 小文件下载
import requests
image_url = 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1596368924575&di=0b1f52010b213b308b8d917ba7a6b7df&imgtype=0&src=http%3A%2F%2Fimage.tianjimedia.com%2FuploadImages%2F2015%2F295%2F41%2F0E87XZ5MPO7J_3epECXX_600.jpg'
r = requests.get(image_url)
with open("beautiful.png",'wb') as f:
    f.write(r.content)

### 大文件下载
# 如果文件比较大的话，那么下载下来的文件先放在内存中，内存还是比较有压力的。
# 所以为了防止内存不够用的现象出现，我们要想办法把下载的文件分块写到磁盘中。
file_url = "http://python.xxx.yyy.pdf"
r = requests.get(url=file_url, stream=True)
with open("python.pdf", 'wb') as pdf:
    for chunk in r.iter_content(chunk_size=1024):
        if chunk:
            pdf.write(chunk)