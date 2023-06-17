import threading
import mac_filter
import time
from rich.console import Console

def run():
    while True:
        lines = mac_filter.read_file('data/airodump-ng-01.csv')
        macs = [mac_filter.parse_line(line) for line in lines]
        macs = [mac for mac in macs if not mac_filter.is_local_mac(mac.station_mac)]
        macs = [mac for mac in macs if mac_filter.check_oui_db(mac.station_mac)]
        print("--------------------")
        for mac in macs:
            print(mac.station_mac, mac.first_time_seen, mac.last_time_seen, mac.power, mac.packets, mac.bssid, mac.probed_essids)
        time.sleep(2)


def main():
    threading.Thread(target=run).start()


if __name__ == '__main__':
    main()