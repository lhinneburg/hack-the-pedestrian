import datetime

class MacModel:
    station_mac = str
    first_time_seen = datetime.datetime
    last_time_seen = datetime.datetime
    power = int
    packets = int
    bssid = str
    probed_essids = str