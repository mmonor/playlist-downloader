import tkinter as tk
from PIL import Image, ImageTk

class PlaylistDownloaderGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Playlist Downloader")
        self.root.minsize(500, 300)
        self.root.configure(bg="#f0f0f0")  # TODO: change background color

        bg_color = "#48248f"

        # TODO: add a YouTube logo next to the text ##FIXED
        image = Image.open("youtube.png")
        resized_image = image.resize((150, 150))
        self.new_image = ImageTk.PhotoImage(resized_image)

        main_frame = tk.Frame(root, bg=bg_color)
        main_frame.pack(expand=True, fill='both')

        # TODO: scale it whenever the user maximizes the window ##FIXED
        for i in range(5):
            main_frame.grid_rowconfigure(i, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)

        tk.Label(
            main_frame,
            text="Welcome to Playlist Downloader",
            font=("Helvetica", 18, "bold"),
            pady=20,
            padx=20,
            bg=bg_color
        ).grid(row=0, column=0, sticky="n", pady=10)

        tk.Label(main_frame, image=self.new_image, bg=bg_color).grid(row=1, column=0, pady=10)

        tk.Label(
            main_frame,
            text="Please insert the link to the YouTube playlist you want to download",
            font=("Helvetica", 14),
            bg=bg_color
        ).grid(row=2, column=0, sticky="n", padx=10, pady=10)

        self.entry = tk.Entry(main_frame, width=40, font=("Helvetica", 14))
        self.entry.grid(row=3, column=0, pady=10)

        # TODO: make it prettier ig idk
        tk.Button(
            main_frame,
            text="Download",
            fg="white",
            bg="green",
            font=("Helvetica", 12),
            padx=15,
            pady=15
        ).grid(row=4, column=0, pady=10)
