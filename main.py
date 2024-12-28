import tkinter
import customtkinter
from yt_dlp import YoutubeDL

def progress_hook(status):
    if status['status'] == 'downloading':
        downloaded = status.get('downloaded_bytes', 0)
        total = status.get('total_bytes', 1)
        percentage = downloaded / total
        progressBar.set(percentage)
        progressLabel.configure(text=f"{int(percentage * 100)}%")
    elif status['status'] == 'finished':
        finishLabel.configure(text="Downloaded!", text_color="green")

def start_download():
    yt_dlp_link = link.get()
    if not yt_dlp_link.strip():
        finishLabel.configure(text="The URL cannot be empty.", text_color="red")
        return

    try:
        # Configuration for YoutubeDL
        ydl_opts = {
            'format': 'best',
            'outtmpl': '%(title)s.%(ext)s',
            'progress_hooks': [progress_hook]
        }

        finishLabel.configure(text="")

        with YoutubeDL(ydl_opts) as yt_dlp_object:
            yt_dlp_object.download([yt_dlp_link])

    except Exception as e:
        finishLabel.configure(text="Download Error", text_color="red")
        print(f"An error occurred: {e}")

# System settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# Our app Frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

# Adding UI Elements
title = customtkinter.CTkLabel(app, text="Insert a YouTube link")
title.pack(padx=10, pady=10)

# Link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var, placeholder_text="Paste video URL here")
link.pack()

# Finished downloading label
finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

# Progress percentage label
progressLabel = customtkinter.CTkLabel(app, text="0%")  
progressLabel.pack()

# Progress bar
progressBar = customtkinter.CTkProgressBar(app, width=400) 
progressBar.set(0)
progressBar.pack()

# Download button
download = customtkinter.CTkButton(app, text="Download", command=start_download)
download.pack(padx=10, pady=10)

# Run app
app.mainloop()
