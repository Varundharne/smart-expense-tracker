from flask import Flask, render_template, request, redirect, session
import sqlite3

app = Flask(__name__)
app.secret_key = "secret123"


# Database Connection
def get_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn


# Home Page
@app.route("/")
def home():
    return redirect("/dashboard")


# Dashboard
@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        # Temporary session for testing
        session["user_id"] = 1
        session["name"] = "Varun"

    conn = get_db()

    expenses = conn.execute(
        "SELECT * FROM expenses WHERE user_id=?",
        (session["user_id"],)
    ).fetchall()

    total = conn.execute(
        "SELECT SUM(amount) FROM expenses WHERE user_id=?",
        (session["user_id"],)
    ).fetchone()[0]

    budget = conn.execute(
        "SELECT amount FROM budget WHERE user_id=?",
        (session["user_id"],)
    ).fetchone()

    conn.close()

    if total is None:
        total = 0

    budget_amount = budget["amount"] if budget else 0
    remaining = budget_amount - total

    return render_template(
        "dashboard.html",
        expenses=expenses,
        total=total,
        budget=budget_amount,
        remaining=remaining
    )


# Budget Page
@app.route("/budget", methods=["GET", "POST"])
def budget():
    if "user_id" not in session:
        session["user_id"] = 1
        session["name"] = "Varun"

    conn = get_db()

    if request.method == "POST":
        amount = request.form["amount"]

        conn.execute(
            "DELETE FROM budget WHERE user_id=?",
            (session["user_id"],)
        )

        conn.execute(
            "INSERT INTO budget(user_id, amount) VALUES (?, ?)",
            (session["user_id"], amount)
        )

        conn.commit()

    budget = conn.execute(
        "SELECT * FROM budget WHERE user_id=?",
        (session["user_id"],)
    ).fetchone()

    conn.close()

    return render_template(
        "budget.html",
        budget=budget
    )


# Reports Page
@app.route("/reports")
def reports():
    if "user_id" not in session:
        session["user_id"] = 1
        session["name"] = "Varun"

    conn = get_db()

    expenses = conn.execute(
        """
        SELECT category,
               SUM(amount) AS total
        FROM expenses
        WHERE user_id=?
        GROUP BY category
        """,
        (session["user_id"],)
    ).fetchall()

    conn.close()

    return render_template(
        "reports.html",
        expenses=expenses
    )


if __name__ == "__main__":
    app.run(debug=True)

@app.route("/register")
def register():
    return render_template("register.html")

