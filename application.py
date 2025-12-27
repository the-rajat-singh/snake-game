from flask import Flask, render_template, jsonify
import os
import socket

# IMPORTANT: variable name must be `application` for Elastic Beanstalk
application = Flask(__name__)

APP_VERSION = os.getenv("APP_VERSION", "v1.0.0")
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")


@application.route("/")
def index():
    return render_template(
        "index.html",
        hostname=socket.gethostname(),
        environment=ENVIRONMENT,
        version=APP_VERSION
    )


@application.route("/health")
def health():
    return jsonify({"status": "UP"}), 200


@application.route("/info")
def info():
    return jsonify({
        "hostname": socket.gethostname(),
        "environment": ENVIRONMENT,
        "version": APP_VERSION
    })


@application.route("/users")
def users():
    return jsonify(["Rajat", "Aman", "DevOps-User"])


if __name__ == "__main__":
    application.run()
