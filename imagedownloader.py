import requests
import argparse
import os


def download_image(url, filename, chunk_size=1024):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status() # http hata kontrolu
        if os.path.exists(filename):
            print(f"uyarı, {filename} zaten var, üzerine yazılıyor.")

        with open(filename,"wb") as f:
            for chunk in response.iter_content(chunk_size):
                if chunk:
                    f.write(chunk)
        print(f"{filename} başarıyla oluşturuldu")
    except requests.exceptions.RequestException as e:
        print(f"HTTP hatası{e}")
    except Exception as e:
        print(f"genel bir hata oluştu {e}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u","--url",required=True,help="İndirilecek görselin URL'si")
    parser.add_argument("-f","--file",required=True,help="Sistem üzerine kaydedilecek dosya adı")
    parser.add_argument("-c","--chunk",type=int,default=1024,help="Chunk boyutu (varsayılan: 1024 bayt)")
    args = parser.parse_args()

    download_image(args.url, args.file, args.chunk)

if __name__ == "__main__":
    main()









