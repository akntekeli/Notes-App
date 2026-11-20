import os
import sqlite3
from datetime import datetime

from flask import Flask, abort, g, redirect, render_template, request, url_for


def now():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def create_app(test_config=None):
    app = Flask(__name__)
    app.config["DATABASE"] = os.path.join(app.instance_path, "notes.db")
    if test_config:
        app.config.update(test_config)
    os.makedirs(os.path.dirname(app.config["DATABASE"]), exist_ok=True)

    def get_db():
        if "db" not in g:
            g.db = sqlite3.connect(app.config["DATABASE"])
            g.db.row_factory = sqlite3.Row
        return g.db

    @app.teardown_appcontext
    def close_db(exception=None):
        db = g.pop("db", None)
        if db is not None:
            db.close()

    with sqlite3.connect(app.config["DATABASE"]) as conn:
        conn.execute(
            """CREATE TABLE IF NOT EXISTS notes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                content TEXT,
                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL
            )"""
        )
    conn.close()

    # --- Not listeleme ---
    @app.route("/")
    def index():
        notes = get_db().execute(
            "SELECT * FROM notes ORDER BY updated_at DESC, id DESC"
        ).fetchall()
        return render_template("index.html", notes=notes)

    # --- Not ekleme ---
    @app.route("/notes/new", methods=["GET", "POST"])
    def new_note():
        if request.method == "POST":
            title = request.form.get("title", "").strip()
            content = request.form.get("content", "").strip()
            if not title:
                return render_template(
                    "note_form.html",
                    heading="Yeni Not",
                    note={"title": title, "content": content},
                    error="Başlık boş bırakılamaz.",
                )
            db = get_db()
            db.execute(
                "INSERT INTO notes (title, content, created_at, updated_at) VALUES (?, ?, ?, ?)",
                (title, content, now(), now()),
            )
            db.commit()
            return redirect(url_for("index"))
        return render_template(
            "note_form.html", heading="Yeni Not", note={"title": "", "content": ""}
        )

    # --- Not düzenleme ---
    @app.route("/notes/<int:note_id>/edit", methods=["GET", "POST"])
    def edit_note(note_id):
        db = get_db()
        note = db.execute("SELECT * FROM notes WHERE id = ?", (note_id,)).fetchone()
        if note is None:
            abort(404)
        if request.method == "POST":
            title = request.form.get("title", "").strip()
            content = request.form.get("content", "").strip()
            if not title:
                return render_template(
                    "note_form.html",
                    heading="Notu Düzenle",
                    note={"title": title, "content": content},
                    error="Başlık boş bırakılamaz.",
                )
            db.execute(
                "UPDATE notes SET title = ?, content = ?, updated_at = ? WHERE id = ?",
                (title, content, now(), note_id),
            )
            db.commit()
            return redirect(url_for("index"))
        return render_template("note_form.html", heading="Notu Düzenle", note=note)
    
    # --- Not silme ---
    @app.route("/notes/<int:note_id>/delete", methods=["POST"])
    def delete_note(note_id):
        db = get_db()
        cur = db.execute("DELETE FROM notes WHERE id = ?", (note_id,))
        db.commit()
        if cur.rowcount == 0:
            abort(404)
        return redirect(url_for("index"))
    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
