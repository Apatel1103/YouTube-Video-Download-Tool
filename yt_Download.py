# from pytube import YouTube
# import sys
# import time
# import logging

# # Configure logging
# logging.basicConfig(filename='download_log.txt', level=logging.INFO)

# def download_video(link):
#     yt = YouTube(link)

#     print("Title: ", yt.title)
#     print("Views: ", yt.views)

#     # Measure download time
#     start_time = time.time()
#     try:
#         yd = yt.streams.get_highest_resolution()
#         yd.download('C:\\Users\\19046\\Desktop\\YT download')
#         end_time = time.time()
#         download_time = end_time - start_time
#         logging.info(f"Downloaded: {yt.title}, Time: {download_time:.2f} seconds, Views: {yt.views}")
#         print(f"Download completed in {download_time:.2f} seconds")
#         return True, download_time
#     except Exception as e:
#         logging.error(f"Failed to download: {yt.title}, Error: {e}")
#         print(f"Failed to download video: {e}")
#         print(f"Exception details: {str(e)}")  # Added to print detailed error message
#         return False, None

# if __name__ == "__main__":
#     if len(sys.argv) > 1:
#         link = sys.argv[1]
#     else:
#         print("Error: No video link provided.")
#         sys.exit(1)

#     success, time_taken = download_video(link)

from pytube import YouTube

try:
    # Ask the user to input the YouTube URL
    url = input("Enter the YouTube URL: ")
    
    yt = YouTube(url)
    
    print("Title:", yt.title)
    print("Views:", yt.views)

    # Get the highest resolution stream
    yd = yt.streams.get_highest_resolution()
    
    # Download the video to the current directory
    yd.download()
    
    print("Download complete.")
except Exception as e:
    print("An error occurred:", str(e))
