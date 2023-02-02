from flask import Flask, request, render_template
import redis
import os

app = Flask(__name__)
redis_conn = redis.Redis(host='redis', port=6379, password=os.environ.get('REDIS_PWD'))

@app.route("/")
def index():
    # Retrieve the current click count from Redis
    count = redis_conn.get("clicks")
    if count is None:
        count = 0
        redis_conn.set("clicks", 0)
    else:
        count = int(count)

    # messages = redis_conn.lrange("messages", 0, -1)

    return render_template('front.html',clicks=count,message="")

@app.route("/click")
def update_count():

    count = redis_conn.get("clicks")
    count = int(count)
    redis_conn.set("clicks", count + 1)

    return str(count + 1)

@app.route("/reset", methods=["POST"])
def reset_clicks():
    redis_conn.set("clicks", 0)
    return str(0)

@app.route("/write",methods=["POST"])
def write():
    message = request.form["message"]
    redis_conn.rpush("messages", message)
    return ""

@app.route("/read")
def read():
    message = redis_conn.lindex("messages", -1).decode("utf-8")
    redis_conn.ltrim("messages",0,-2)
    return message
#messages = redis_conn.lrange("messages", 0, -1)
    #if messages:
    #    message = messages.pop(0).decode("utf-8")
    #    redis_conn.ltrim("messages", 1, -1)
    #    return message
    #else:
    #    return "None"


if __name__ == "__main__":
    app.run()
