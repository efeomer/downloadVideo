import pytube

def download_highest_resolution_video(url, save_path):
    try:
        video = pytube.YouTube(url)
        stream = video.streams.get_highest_resolution()
        stream.download(output_path=save_path)
        print("Video downloaded successfully!")
    except Exception as e:
        print("An error occurred:", e)

url = input("Enter video URL: ")
save_path = ""

download_highest_resolution_video(url, save_path)
