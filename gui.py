import tkinter as tk
from db import DbDriver


def main():
    db = DbDriver()

    def add_song():
        title = ent_title.get()
        artists = ent_artists.get()
        tags = ent_tags.get()
        yt = ent_yt.get()

        ent_title.delete(0, tk.END)
        ent_artists.delete(0, tk.END)
        ent_tags.delete(0, tk.END)
        ent_yt.delete(0, tk.END)

        print(title, artists, tags, yt)
        db.add_song(title, artists, tags, yt)

    window = tk.Tk()

    fr_add_song = tk.Frame(
        master=window,
    )

    tk.Label(
        master=fr_add_song,
        text="Title"
    ).grid(row=0, column=0)

    ent_title = tk.Entry(
        master=fr_add_song,
    )
    ent_title.grid(row=0, column=1)

    tk.Label(
        master=fr_add_song,
        text="Artist(s)"
    ).grid(row=1, column=0)

    ent_artists = tk.Entry(
        master=fr_add_song,
    )
    ent_artists.grid(row=1, column=1)

    tk.Label(
        master=fr_add_song,
        text="Tag(s)"
    ).grid(row=2, column=0)

    ent_tags = tk.Entry(
        master=fr_add_song,
    )
    ent_tags.grid(row=2, column=1)

    tk.Label(
        master=fr_add_song,
        text="Youtube Link"
    ).grid(row=3, column=0)

    ent_yt = tk.Entry(
        master=fr_add_song,
    )
    ent_yt.grid(row=3, column=1)

    tk.Button(
        master=fr_add_song,
        text="Add Song",
        command=add_song
    ).grid(row=0, column=2)

    fr_add_song.pack()
    window.mainloop()


if __name__ == "__main__":
    main()
