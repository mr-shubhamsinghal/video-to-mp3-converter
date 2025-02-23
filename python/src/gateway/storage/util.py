import pika, json
import logging


# Configure logging at the top of your file
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def upload(f, fs, channel, access):
    try:
        fid = fs.put(f)
    except Exception as err:
        logging.error(f"Error uploading file: {err}")
        return "internalfdsfd server error", 500
    message = {
        "video_fid": str(fid),
        "mp3_fid": None,
        "username": access["username"],
    }
    try:
        channel.basic_publish(
            exchange="",
            routing_key="video",
            body=json.dumps(message),
            properties=pika.BasicProperties(
                delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
            ),
        )
    except Exception as err:
        print(err)
        fs.delete(fid)
        return "internal server error", 500