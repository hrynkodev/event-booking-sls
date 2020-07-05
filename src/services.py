import boto3
import uuid
import json
from dynamodb_json import json_util
from .config import config

dynamo_db = boto3.client("dynamodb")
sqs = boto3.client("sqs")


def scan_table(table):
    items = dynamo_db.scan(TableName=table)["Items"]

    return json_util.loads(items)


def create_booking(payload):
    booking_id = str(uuid.uuid4())
    dynamo_db.put_item(
        TableName=config.bookings_table,
        Item={
            "place_number": {"N": payload["place_number"]},
            "event_id": {"S": payload["event_id"]},
            "booking_id": {"S": booking_id},
        },
    )

    return booking_id


def send_message_to_queue(queue, message):
    return sqs.send_message(QueueUrl=queue, MessageBody=json.dumps(message))
