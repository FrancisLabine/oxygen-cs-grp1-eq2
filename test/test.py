"""Imports"""
import unittest
import os
from unittest import mock
from unittest.mock import  MagicMock, patch
from src.main import Main

class Tests(unittest.TestCase) :
    """Docstring"""

    def setUp(self):
        """Docstring"""
        self.main = Main()

    #Test variable d'environnement
    @mock.patch.dict(os.environ, {"TOKEN": "fHtJqgMACx"})
    @mock.patch.dict(os.environ, {"HOST": "HTTP://34.95.34.5"})
    @mock.patch.dict(os.environ, {"TICKETS": "3"})
    @mock.patch.dict(os.environ, {"T_MAX": "28"})
    @mock.patch.dict(os.environ, {"T_MIN": "19"})
    @mock.patch.dict(os.environ, {"DATABASE": "OxygenDB"})
    def test_variable_environnement(self):
        """Docstring"""
        #Les variables sont déjà pré-définis (variable d'environnement)
        self.main.set_env_vars()
        self.assertEqual(self.main.TOKEN, "fHtJqgMACx")
        self.assertEqual(self.main.HOST,"HTTP://34.95.34.5")
        self.assertEqual(self.main.TICKETS,"3")
        self.assertEqual(self.main.T_MAX,"28")
        self.assertEqual(self.main.T_MIN,"19")
        self.assertEqual(self.main.DATABASE,"OxygenDB")

    @mock.patch.dict(os.environ, {"TOKEN": "fHtJqgMACx"})
    def test_variable_environnement_default(self):
        """Docstring"""
        #Les variables ne sont pas pré-définis, une valeur par défault leurs est attribuée
        self.main.set_env_vars()

        self.assertEqual(self.main.TOKEN,"fHtJqgMACx")
        self.assertEqual(self.main.HOST,"http://34.95.34.5")    # .env value --> "HTTP://34.95.34.5"
        self.assertEqual(self.main.TICKETS,"6")                 # .env value --> "3"
        self.assertEqual(self.main.T_MAX,"35")                  # .env value --> "28"
        self.assertEqual(self.main.T_MIN,"15")                  # .env value --> "19"
        self.assertEqual(self.main.DATABASE,"oxygendb")         # .env value --> "oxygendb"

    def test_variable_token_invalide(self):
        """Docstring"""
        #retourne un message d'erreur lorsque le token n'est pas définit
        with self.assertRaises(ValueError):
            self.main.set_env_vars()


    #Test fonction main
    def test_set_sensor_hub(self):
        """Docstring"""
        self.main.set_sensor_hub()
        self.assertIsNotNone(self.main.get_hub_connection())

    @mock.patch.dict(os.environ, {"TOKEN": "fHtJqgMACx"})
    def test_analyze_datapoint_turn_on_ac(self):
        """Docstring"""
        self.main.set_env_vars()
        self.main.send_action_to_hvac = MagicMock()
        self.main.analyze_datapoint("2023-06-01", 50)
        self.main.send_action_to_hvac.assert_called_with("2023-06-01", "TurnOnAc",50, \
                                                         int(self.main.TICKETS))

    @mock.patch.dict(os.environ, {"TOKEN": "fHtJqgMACx"})
    def test_analyze_datapoint_turn_on_heater(self):
        """Docstring"""
        self.main.set_env_vars()
        self.main.send_action_to_hvac = MagicMock()
        self.main.analyze_datapoint("2023-06-01", 8)
        self.main.send_action_to_hvac.assert_called_with("2023-06-01", "TurnOnHeater", 8, \
                                                         int(self.main.TICKETS))

    @mock.patch.dict(os.environ, {"TOKEN": "fHtJqgMACx"})
    def test_analyze_datapoint_no_action(self):
        """Docstring"""
        self.main.set_env_vars()
        self.main.send_action_to_hvac = MagicMock()
        self.main.analyze_datapoint("2023-06-01", 20)
        self.assertFalse(self.main.send_action_to_hvac.called)

    @mock.patch.dict(os.environ, {"TOKEN": "fHtJqgMACx"})
    def test_send_event_to_database(self):
        """Docstring"""
        self.main.set_env_vars()
        self.main.send_event_to_database = MagicMock()
        self.main.TOKEN = 'fHtJqgMACx'
        self.main.HOST = "HTTP://34.95.34.5"
        self.main.send_action_to_hvac("2023-06-01", "TurnOnHeater", 8, \
                                                        int(self.main.TICKETS))
        self.main.send_event_to_database.assert_called_with("2023-06-01", "TurnOnHeater", 8)

    @mock.patch.dict(os.environ, {"TOKEN": "fHtJqgMACx"})
    def test_send_temperature_to_fastapi(self):
        """Docstring"""
        self.main.set_env_vars()
        with patch("builtins.print") as mock_print:
            self.main.send_temperature_to_fastapi("2023-06-01", 25.5)
            mock_print.assert_called_with("2023-06-01", 25.5)

if __name__ == '__main__':
    unittest.main()
