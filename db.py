import sqlite3


class DbDriver:
    def __init__(self):
        self.conn = sqlite3.connect('temp.db')
        self.cursor = self.conn.cursor()

        if self._table_exists('songs'):
            pass
        else:
            self._create_song_table()

    def __del__(self):
        self.conn.close()

    def _table_exists(self, table_name):
        results = self.cursor.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name= ?;",
            (table_name,),
        ).fetchall()

        if not results:
            return False
        else:
            return True

    def _create_song_table(self):
        self.cursor.execute("CREATE TABLE songs (title TEXT, artists TEXT, tags TEXT, ytLink TEXT)")

    def add_song(self,
                 title,
                 artists,
                 tags,
                 yt):
        self.cursor.execute(
            "INSERT INTO songs VALUES (?, ?, ?, ?)",
            (title, artists, tags, yt),
        )
        self.conn.commit()

    def view_all_songs(self):
        rows = self.cursor.execute("SELECT title, artists, tags, ytLink FROM songs").fetchall()
        return rows

    def test_add_sample_entries(self):
        self.add_song('Purple Gusher', 'Rezz', 'new-edm,liked', 'https://youtube.com/fjklasdfjklasdfj')

    def test_view_sample_entries(self):
        return self.view_all_songs()


def main():
    db = DbDriver()
    db.test_add_sample_entries()
    print(db.test_view_sample_entries())


if __name__ == "__main__":
    main()
