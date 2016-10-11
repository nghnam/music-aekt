from .. import zing
#import ZingDownloader

url = "http://mp3.zing.vn/bai-hat/Gui-Anh-Xa-Nho-Bich-Phuong/ZW7UFI6I.html"
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'}
z = ZingDownloader(url=url, path='/tmp', headers=headers) 
#print z.metadata
print(z.download_url)
f = z.download_mp3_file()
print(f)
