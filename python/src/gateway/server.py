import os, gridfs, pika, json
from flask import Flask, request, send_file
from flask_pymongo import PyMongo
from auth import validate
from auth_svc import access
from storage import util
from bson.objectid import ObjectId
import logging


# Configure logging at the top of your file
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

server = Flask(__name__)
# server.config["MONGO_URI"] = "mongodb://host.minikube.internal:27017/videos"

mongo_video = PyMongo(
    server,
    uri="mongodb://host.minikube.internal:27017/videos"
)
mongo_audio = PyMongo(
    server,
    uri="mongodb://host.minikube.internal:27017/mp3s"
)

video_fs = gridfs.GridFS(mongo_video.db)
audio_fs = gridfs.GridFS(mongo_audio.db)

connection = pika.BlockingConnection(pika.ConnectionParameters("rabbitmq"))
channel = connection.channel()

@server.route("/login", methods=["POST"])
def login():
    token, err = access.login(request)
    if not err:
        return token
    else:
        return err

@server.route("/upload", methods=["POST"])
def upload():
    access, err = validate.token(request)
    if err:
        return err
    access = json.loads(access)
    if access["admin"]:
        if len(request.files) > 1 or len(request.files) < 1:
            return "exactly 1 file required", 400
        for _, f in request.files.items():
            # f is a FileStorage object, video_fs is a GridFS object, channel is a pika channel, access is a dictionary
            err = util.upload(f, video_fs, channel, access)
            if err:
                return err
        return "success", 200
    else:
        return "not authorized", 401

@server.route("/download", methods=["GET"])
def download():
    access, err = validate.token(request)
    if err:
        return err
    access = json.loads(access)
    if access["admin"]:
        fid_string = request.args.get("fid")
        if not fid_string:
            return "fid is required", 400
        try:
            out = audio_fs.get(ObjectId(fid_string))
            return send_file(out, download_name=f"{fid_string}.mp3")
        except Exception as e:
            print(e)
            logging.error(f"Error downloading file: {e}")
            return "internal server error", 500

    return "not authorized", 401

if __name__ == "__main__":
    server.run(host="0.0.0.0", port=8080)