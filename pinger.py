import json
import pingparsing
from datetime import datetime

print("Hello from JSON Pinger Python!")

ping_parser = pingparsing.PingParsing()
transmitter = pingparsing.PingTransmitter()
transmitter.destination = "google.com"
transmitter.ping_option = "-i 10"
transmitter.count = 6

while True:
    print(f"Attempting Ping at {datetime.now().isoformat()}")
    result = transmitter.ping()
    with open("logs/ping_log.txt", "a+") as log:
        data = ping_parser.parse(result).as_dict()
        data.update({'dttm': datetime.now().isoformat()})
        log.writelines(json.dumps(data, indent=4))
        log.write("\n,")
