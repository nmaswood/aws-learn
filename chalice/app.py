from chalice import Chalice
import aws_learn as A

app = Chalice(app_name="chalice")


@app.route("/")
def index():
    return A.hello_world()
