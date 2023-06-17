import mac_model
import datetime

def read_file(file_name):
    """Reads a file and returns a list of lines."""
    with open(file_name, 'r') as file:
        lines = file.readlines()
        # remove empty lines
        lines = [line for line in lines if line != '\n']
        # split file on header lines
        for i in range(len(lines)):
            if lines[i].startswith('Station MAC'):
                for j in range(i + 1, len(lines)):
                    return lines[j:]
                

def check_oui_db(mac):
    """Checks if MAC is in OUI database."""
    with open('data/oui.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            """Check hex representation of MAC address."""
            mac_address = mac.upper().replace(":", "").replace("-", "")
            # print(mac_address)
            oui = mac_address[:6]
            if oui in line:
                return True
    

def parse_line(line):
    """Parses a line and returns a MacModel object."""
    time_format = '%Y-%m-%d %H:%M:%S'
    line = line.split(',')
    mac = mac_model.MacModel()
    mac.station_mac = line[0]
    mac.first_time_seen = datetime.datetime.strptime(line[1].lstrip(), time_format)
    mac.last_time_seen = datetime.datetime.strptime(line[2].lstrip(), time_format)
    mac.power = int(line[3])
    mac.packets = int(line[4])
    mac.bssid = line[5]
    mac.probed_essids = line[6]
    return mac

def is_local_mac(mac):
    """checks if MAC is LAA or UAA"""
    return mac[1] in ['2', '6', 'A', 'E'] or mac[2] in ['2', '6', 'A', 'E']

