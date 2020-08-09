from chalice import Chalice
import aws_learn as A

app = Chalice(app_name="chalice")


@app.route("/")
def index():
    A.kafka.produce()
    return {"something": "is on the queue"}
