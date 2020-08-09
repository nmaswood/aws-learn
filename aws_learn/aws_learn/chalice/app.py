from chalice import Chalice

app = Chalice(app_name="aws_learn/chalice")


@app.route("/")
def index():
    return {"hello": "world"}
