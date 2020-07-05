import json
from .services import scan_table, create_booking, send_message_to_queue
from .config import config


def get_all_events(event, context):
    try:
        events = scan_table(config.events_table)

        return {"statusCode": 200, "body": json.dumps(events)}
    except Exception as e:
        print(e)
        return {"statusCode": 500, "body": "Internal server Error"}


def book_place(event, context):
    try:
        booking_id = create_booking(json.loads(event["body"]))

        return {"statusCode": 200, "body": json.dumps({"booking_id": booking_id})}
    except Exception as e:
        print(e)
        return {"statusCode": 500, "body": "Internal server Error"}


def booking_trigger(event, context):
    message = event["Records"][0]["dynamodb"]["NewImage"]

    return send_message_to_queue(config.reservation_queue_url, message)["MessageID"]
