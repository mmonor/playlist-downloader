import tkinter as tk


window = tk.Tk()
window.title("Playlist Downloader")
window.minsize(500, 300)

main_frame = tk.Frame(window)
main_frame.pack(expand=True, fill='both')

welcome_label = tk.Label(
    main_frame,
    text = "Welcome to Playlist Downloader",
    font=("Helvetica",18,"bold"),
    pady=20,
    padx=20

)
welcome_label.grid(row=0, column=0,columnspan=2)

prompt_label = tk.Label(
    main_frame,
    text = "Please insert the link to the youtube playlist you want to download",
    font=("Helvetica",14),


)
prompt_label.grid(row=1, column=0,sticky="e",padx=10,pady=10)
entry = tk.Entry(main_frame,
                 width=40,
                 font=("Helvetica",14))

entry.grid(row=2, column=0,pady=10)

download_button = tk.Button(
    main_frame,
    text="Download",
    fg="white",
    bg="green",
    font=("Helvetica",12),
    padx=10,
    pady=5,
)
download_button.grid(row=3, column=0)
window.mainloop()

#TODO add a youtube logo next to the text
#TODO scale it whenever the user maximizes the window
#TODO change background color
#TODO make it prettier ig idk