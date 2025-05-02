from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/stok_ekle")
def stok_ekle():
    return render_template("stok_ekle.html")

@app.route("/stok_duzenle")
def stok_duzenle():
    return render_template("stok_duzenle.html")

@app.route("/stok_listesi")
def stok_listesi():
    return render_template("stok_listesi.html")

@app.route("/urun_ayrintilari")
def urun_ayrintilari():
    return render_template("urun_ayrintilari.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
    # app.run(debug=True)
