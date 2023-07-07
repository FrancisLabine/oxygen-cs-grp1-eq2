"""Imports"""
import unittest
from unittest.mock import  MagicMock, patch
from src.main import Main


class Tests(unittest.TestCase) :
    """Docstring"""

    #Test fonction main

    def setUp(self):
        """Docstring"""
        self.main = Main()
        self.main.T_MIN = '18'
        self.main.T_MAX = '30'
        self.main.TICKETS = '3'

    def test_variable_token_invalide(self):
        """Docstring"""
        #retourne un message d'erreur lorsque le token n'est pas définit
        with self.assertRaises(ValueError):
            self.main.TOKEN = None
            self.main.set_env_vars()

    def test_set_sensor_hub(self):
        """Docstring"""
        self.main.set_sensor_hub()
        self.assertIsNotNone(self.main.get_hub_connection())

    def test_analyze_datapoint_turn_on_ac(self):
        """Docstring"""
        self.main.send_action_to_hvac = MagicMock()
        self.main.analyze_datapoint("2023-06-01", 34)
        self.main.send_action_to_hvac.assert_called_with("2023-06-01", "TurnOnAc",34, \
                                                         int(self.main.TICKETS))

    def test_analyze_datapoint_turn_on_heater(self):
        """Docstring"""
        self.main.send_action_to_hvac = MagicMock()
        self.main.analyze_datapoint("2023-06-01", 16)
        self.main.send_action_to_hvac.assert_called_with("2023-06-01", "TurnOnHeater", 16, \
                                                         int(self.main.TICKETS))

    def test_analyze_datapoint_no_action(self):
        """Docstring"""
        self.main.send_action_to_hvac = MagicMock()
        self.main.analyze_datapoint("2023-06-01", 20)
        self.assertFalse(self.main.send_action_to_hvac.called)

    def test_send_event_to_database(self):
        """Docstring"""
        self.main.send_event_to_database = MagicMock()
        self.main.TOKEN = 'fHtJqgMACx'
        self.main.HOST = "HTTP://34.95.34.5"
        self.main.send_action_to_hvac("2023-06-01", "TurnOnHeater", 16, \
                                                        int(self.main.TICKETS))
        self.main.send_event_to_database.assert_called_with("2023-06-01", "TurnOnHeater", 16)


    def test_send_temperature_to_fastapi(self):
        """Docstring"""
        with patch("builtins.print") as mock_print:
            self.main.send_temperature_to_fastapi("2023-06-01", 25.5)
            mock_print.assert_called_with("2023-06-01", 25.5)

if __name__ == '__main__':
    unittest.main()
