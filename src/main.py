"""Imports"""
import json
import logging
import time
import os
import requests

from signalrcore.hub_connection_builder import HubConnectionBuilder


class Main:
    """Docstring"""
    def __init__(self):
        self._hub_connection = None
        self.HOST = "https://34.95.34.5"  # Setup your host here
        self.TOKEN = None  # Setup your token here
        self.TICKETS = None  # Setup your tickets here
        self.T_MAX = 23  # Setup your max temperature here
        self.T_MIN = 18  # Setup your min temperature here
        self.DATABASE = "OxygenDB"  # Setup your database here
        #self.dbConnection = None

    def __del__(self):
        if self.hub_connection is not None:
            self.hub_connection.stop()
        # if self.dbConnection != None:
        #     self.dbConnection.close()

    def setup(self):
        # exec(open(os.getcwd() + "/script/mySqlSetup.py").read())
        exec(open(os.getcwd() + "/script/setEnvVariables.py").read())
        self.TOKEN = "fHtJqgMACx" #os.environ.get("TOKEN")
        """Docstring"""
        self.set_sensor_hub()

    def start(self):
        """Docstring"""
        self.setup()
        self.hub_connection.start()

        print("Press CTRL+C to exit.")
        while True:
            time.sleep(2)

    def set_sensor_hub(self):
        """Docstring"""
        self.hub_connection = (
            HubConnectionBuilder()
            .with_url(f"{self.host}/SensorHub?token={self.token}")
            .configure_logging(logging.INFO)
            .with_automatic_reconnect(
                {
                    "type": "raw",
                    "keep_alive_interval": 10,
                    "reconnect_interval": 5,
                    "max_attempts": 999,
                }
            )
            .build()
        )

        self.hub_connection.on("ReceiveSensorData", self.on_sensor_data_received)
        self.hub_connection.on_open(lambda: print("||| Connection opened."))
        self.hub_connection.on_close(lambda: print("||| Connection closed."))
        self.hub_connection.on_error(lambda data: print(f"||| \
                               An exception was thrown closed: {data.error}"))

    def on_sensor_data_received(self, data):
        """Docstring"""
        try:
            print(data[0]["date"] + " --> " + data[0]["data"])
            date = data[0]["date"]
            d_p = float(data[0]["data"])
            self.send_temperature_to_fastapi(date, d_p)
            self.analyze_datapoint(date, d_p)
        except ValueError as err:
            print(err)

    def analyze_datapoint(self, date, data):
        """Docstring"""
        if float(data) >= float(self.t_max):
            self.send_action_to_hvac(date, "TurnOnAc", self.tickets)
        elif float(data) <= float(self.t_min):
            self.send_action_to_hvac(date, "TurnOnHeater", self.tickets)

    def send_action_to_hvac(self, date, action, nb_tick):
        """Docstring"""
        response = requests.get(f"{self.host}/api/hvac/{self.token}/{action}/{nb_tick}", timeout=10)
        details = json.loads(response.text)
        print(details, date)

    def send_event_to_database(self, timestamp, event):
        """3 events possible, Turn on AC, Turn on Heat or Set to normal"""
        print(timestamp, event)
        try:
            # To implement
            # voir create_connection.py
            pass
        except requests.exceptions.RequestException as exception:
            # To implement
            print(exception)

    def send_temperature_to_fastapi(self, date, d_p):
        """Docstring"""
        print(date, d_p)

if __name__ == "__main__":
    main = Main()
    main.start()
