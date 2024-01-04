import os

import pytube


# download single video with optional quality setting
def on_progress_callback(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage = (bytes_downloaded / total_size) * 100
    print(f"\rDownloading: {percentage:.2f}% complete", end='', flush=True)


def download_single_video(video_url, output_path='./download', quality='highest'):
    # Check if the download directory exists, create it if not
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    try:
        yt = pytube.YouTube(video_url, on_progress_callback=on_progress_callback)

        if quality.lower() == 'highest':
            stream = yt.streams.get_highest_resolution()
        elif quality.lower() == 'lowest':
            stream = yt.streams.get_lowest_resolution()
        else:
            stream = yt.streams.filter(res=quality).first()

        print(f"Downloading: {yt.title} in {stream.resolution} resolution")
        stream.download(output_path=output_path)
        print(f"\nDownloaded: {yt.title}")
    except Exception as e:
        print(f"Error: {str(e)}")


# Example usage with quality setting
video_url = "https://www.youtube.com/watch?v=QdBZY2fkU-0"
download_single_video(video_url, quality='1080p')
