import os


class BaseConfig(object):
    @property
    def events_table(self):
        return os.environ.get("events_table")

    @property
    def bookings_table(self):
        return os.environ.get("bookings_table")

    @property
    def reservation_queue_url(self):
        return os.environ.get("reservation_queue_url")


config = BaseConfig()
