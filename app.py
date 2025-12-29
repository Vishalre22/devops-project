from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "🚀 DevOps CI/CD Project Running on Kubernetes (KIND) Made by Vishal!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

