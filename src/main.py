"""Imports"""
import json
import logging
import time
import os
from signalrcore.hub_connection_builder import HubConnectionBuilder
import mysql.connector
import requests

class Main:
    """Docstring"""
    def __init__(self):
        self._hub_connection = None
        self.HOST = None              # api host
        self.TOKEN = None             # token
        self.TICKETS = None           # nb of tickets
        self.T_MAX = None             # max temperature
        self.T_MIN = None             # min temperature
        self.DATABASE = None          # database name

    def __del__(self):
        if self._hub_connection is not None:
            self._hub_connection.stop()

    def get_hub_connection(self):
        """Docstring"""
        return self._hub_connection

    def setup(self):
        """Docstring"""
        self.set_env_vars()
        self.set_db()
        self.set_sensor_hub()

    def start(self):
        """Docstring"""
        self.setup()
        self._hub_connection.start()

        print("Press CTRL+C to exit.")
        while True:
            time.sleep(2)

    def set_sensor_hub(self):
        """Docstring"""
        self._hub_connection = (
            HubConnectionBuilder()
            .with_url(f"{self.HOST}/SensorHub?token={self.TOKEN}")
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

        self._hub_connection.on("ReceiveSensorData", self.on_sensor_data_received)
        self._hub_connection.on_open(lambda: print("||| Connection opened."))
        self._hub_connection.on_close(lambda: print("||| Connection closed."))
        self._hub_connection.on_error(lambda data: print(f"||| \
                               An exception was thrown closed: {data.error}"))

    def on_sensor_data_received(self, data):
        """Docstring"""
        try:
            date = data[0]["date"]
            d_p = float(data[0]["data"])
            self.send_temperature_to_fastapi(date, d_p)
            self.analyze_datapoint(date, d_p)
        except ValueError as err:
            print(err)

    def analyze_datapoint(self, date, data):
        """Docstring"""
        if float(data) >= float(self.T_MAX):
            self.send_action_to_hvac(date, "TurnOnAc", data, int(self.TICKETS))
        elif float(data) <= float(self.T_MIN):
            self.send_action_to_hvac(date, "TurnOnHeater", data, int(self.TICKETS))

    def send_action_to_hvac(self, date, action, data, nb_tick):
        """Docstring"""
        request = requests.get(f"{self.HOST}/api/hvac/{self.TOKEN}/{action}/{nb_tick}", timeout=10)
        details = json.loads(request.text)
        print(details)
        self.send_event_to_database(date, action, data)

    def send_event_to_database(self, timestamp, event, data):
        """Docstring"""
        print(timestamp, event, data)
        try:
            conn = mysql.connector.connect(
            host="localhost",  # Replace with your MySQL server host
            user="root",  # Replace with your MySQL username
            password="1234"  # Replace with your MySQL password
            )
            cursor = conn.cursor()
            # Switch to the newly created database
            cursor.execute(f"USE {self.DATABASE} ")

            # insert into table
            TABLE_NAME = "ac_event"  # Replace with your desired table name
            insert_query = f"""
                INSERT INTO {TABLE_NAME} (timestamp, event, temp) 
                VALUES ('{timestamp}', '{event}', '{data}' )
            """
            cursor.execute(insert_query)
            conn.commit()

            # Close connection
            cursor.close()
            conn.close()
        except requests.exceptions.RequestException as exception:
            # To implement
            print(exception)

    def send_temperature_to_fastapi(self, date, d_p):
        """Docstring"""
        print(date, d_p)

    def set_db(self):
        """Docstring"""
        # Establish a connection to the MySQL server
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234"
        )

        # Create a new database
        cursor = conn.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.DATABASE}")

        # Switch to the newly created database
        cursor.execute(f"USE {self.DATABASE}")

        # Create a table
        TABLE_NAME = "ac_event"
        cursor = conn.cursor()
        create_table_query = f"""
            CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
                id INT AUTO_INCREMENT PRIMARY KEY,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                event VARCHAR(64) NOT NULL,
                temp DECIMAL(6,2) NOT NULL         
            )
        """
        cursor.execute(create_table_query)

        # Close the cursor
        cursor.close()
        conn.close()

    def set_env_vars(self):
        """Docstring"""

        self.HOST = os.environ.get("HOST")          # api host
        self.TOKEN = os.environ.get("TOKEN")        # token
        self.TICKETS = os.environ.get("TICKETS")    # nb of tickets
        self.T_MAX = os.environ.get("T_MAX")        # max temperature
        self.T_MIN = os.environ.get("T_MIN")        # min temperature
        self.DATABASE = os.environ.get("DATABASE")  # database name

        #Met les variables d'environnement par défaut s'ils n'existent pas.
        if not self.TOKEN or self.TOKEN == '' :
            raise ValueError("TOKEN INEXISTANT")

        if not self.HOST or self.HOST == '':
            self.HOST = "http://34.95.34.5"

        if not self.TICKETS or self.TICKETS == '':
            self.TICKETS = '6'

        if not self.T_MAX or self.T_MAX == '':
            self.T_MAX = '35'

        if not self.T_MIN or self.T_MIN == '':
            self.T_MIN = '15'

        if not self.DATABASE or self.DATABASE == '':
            self.DATABASE = "oxygendb"

if __name__ == "__main__":
    main = Main()
    main.start()
