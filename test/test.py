
import os
import unittest
from unittest.mock import  MagicMock, patch
from src.main import Main


class Tests(unittest.TestCase) :

    #retourne un message d'erreur lorsque le token n'est pas définit
    def test_variable_token_invalide(self):
        with self.assertRaises(Exception):
             exec(open(os.getcwd() + "/script/set_Env_Variables.py").read())
       
    #Test fonction main       
    """Docstring"""
    def setUp(self):
        self.main = Main()

    def tearDown(self):
        pass

    def test_set_sensor_hub(self):
        """Docstring"""
        self.main.set_sensor_hub()
        self.assertIsNotNone(self.main._hub_connection)

    def test_analyze_datapoint_turn_on_ac(self):
        """Docstring"""
        self.main.T_MIN = 18
        self.main.T_MAX = 30
        self.main.TICKETS = 3
        self.main.send_action_to_hvac = MagicMock()
        self.main.analyze_datapoint("2023-06-01", 34)
        self.main.send_action_to_hvac.assert_called_with("2023-06-01", "TurnOnAc",34, \
                                                         self.main.TICKETS)

    def test_analyze_datapoint_turn_on_heater(self):
        """Docstring"""
        self.main.T_MIN = 18
        self.main.T_MAX = 30
        self.main.TICKETS = 3
        self.main.send_action_to_hvac = MagicMock()
        self.main.analyze_datapoint("2023-06-01", 16)
        self.main.send_action_to_hvac.assert_called_with("2023-06-01", "TurnOnHeater", 16, \
                                                         self.main.TICKETS)

    def test_analyze_datapoint_no_action(self):
        """Docstring"""
        self.main.T_MIN = 18
        self.main.T_MAX = 30
        self.main.send_action_to_hvac = MagicMock()
        self.main.analyze_datapoint("2023-06-01", 20)
        self.assertFalse(self.main.send_action_to_hvac.called)

    def test_send_event_to_database(self):
        """Docstring"""
        with patch("builtins.print") as mock_print:
            self.main.DATABASE = 'OxygenDB'
            self.main.send_event_to_database("2023-06-01", "TurnOnAc", 30)
            mock_print.assert_called_with("2023-06-01", "TurnOnAc", 30)

    def test_send_temperature_to_fastapi(self):
        """Docstring"""
        with patch("builtins.print") as mock_print:
            self.main.send_temperature_to_fastapi("2023-06-01", 25.5)
            mock_print.assert_called_with("2023-06-01", 25.5)

if __name__ == '__main__':
    unittest.main()
