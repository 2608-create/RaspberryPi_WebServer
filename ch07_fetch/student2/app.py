import requests                                              # 추가
from flask import Flask, render_template, request, jsonify   # request, jsonify 추가
import config

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("gallery.html")

@app.route("/api/photos")                                    # 추가
def api_photos():
    page = request.args.get("page", 1)
    photo = requests.get(f"https://jsonplaceholder.typicode.com/photos?_page={page}&_limit=3").json()
    photos = [];
    for p in photo: 
        photos.append({"title": p["title"], "img": p["url"]})
    return jsonify(photos)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=config.PORT)
