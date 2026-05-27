from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    message = None
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        if name:
            message = f"Hello, {name}!"
        else:
            message = "Please enter a name."
    return render_template("index.html", message=message)

if __name__ == "__main__":
    # In Codespaces, host='0.0.0.0' lets the preview port work.
    app.run(host="0.0.0.0", port=5000, debug=True)
