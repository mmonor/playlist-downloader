import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter.messagebox as messagebox
bg_color = "#48248f"
class PlaylistDownloaderGUI:
    def __init__(self, root, download_callback=None):
        self.root = root
        self.root.title("Playlist Downloader")
        self.root.minsize(500, 300)
        self.root.configure(bg="#48248f")

        self.download_callback = download_callback

        # YouTube logo
        image = Image.open("youtube.png")
        resized_image = image.resize((150, 150))
        self.new_image = ImageTk.PhotoImage(resized_image)

        main_frame = tk.Frame(root, bg="#48248f")
        main_frame.pack(expand=True, fill='both')

        # This scales the elements based of the window resolution
        for i in range(5):
            main_frame.grid_rowconfigure(i, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)

        tk.Label(
            main_frame,
            text="Welcome to Playlist Downloader",
            font=("Helvetica", 18, "bold"),
            pady=20,
            padx=20,
            bg="#48248f"
        ).grid(row=0, column=0, sticky="n", pady=10)

        tk.Label(main_frame, image=self.new_image, bg="#48248f").grid(row=1, column=0, pady=10)

        tk.Label(
            main_frame,
            text="Please insert the link to the YouTube playlist you want to download",
            font=("Helvetica", 14),
            bg="#48248f"
        ).grid(row=2, column=0, sticky="n", padx=10, pady=10)

        self.entry = tk.Entry(main_frame, width=40, font=("Helvetica", 14))
        self.entry.grid(row=3, column=0, pady=10)
        self.format_var = tk.StringVar(value="audio")

        format_frame = tk.Frame(main_frame, bg=bg_color)
        format_frame.grid(row=4, column=0, pady=10)





        # Download button
        tk.Button(
            main_frame,
            text="Download",
            fg="white",
            bg="green",
            font=("Helvetica", 12),
            padx=15,
            pady=15,
            command=self.handle_download
        ).grid(row=4, column=0, pady=10)

        # Progress bar
        self.progress_bar = ttk.Progressbar(
            main_frame,
            orient="horizontal",
            length=300,
            mode="determinate",
            maximum=100,
        )
        self.progress_bar.grid(row=5, column=0, pady=20)

    def handle_download(self):
        url = self.entry.get()
        if not url:
            messagebox.showerror("Error", "Please fill in this field")
            return

        if "youtube.com" not in url:
            messagebox.showerror("Error", "This is not a valid URL")
            return


        if self.download_callback:
            self.download_callback(url, self.update_progress)

    def update_progress(self, progress):

        self.progress_bar["value"] = progress
        self.root.update_idletasks()
