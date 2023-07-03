
import os
import unittest
from unittest.mock import MagicMock, patch
from src.main import Main

class Tests(unittest.TestCase) :
    def main(self):
        self.Test_Scripts()

##Test scripts
    def test_Script_sql(self):
        try :
            exec(open(os.getcwd() + "/script/my_Sql_Setup.py").read())
        except Exception :
            self.fail("script sql retourne une exception.")
        
    def test_Script_EnvVar(self):
        try :
           exec(open(os.getcwd() + "/script/set_Env_Variables.py").read())
        except Exception :
            self.fail("script de variable d'environnement retourne une exception.")

        self.assertEqual(os.environ.get("TOKEN"),"fHtJqgMACx")

##Test fonction main       
    """Docstring"""
    def setUp(self):
        self.main = Main()

    def tearDown(self):
        pass

    def test_set_sensor_hub(self):
        """Docstring"""
        self.main.set_sensor_hub()
        self.assertIsNotNone(self.main.hub_connection)

    def test_analyze_datapoint_turn_on_ac(self):
        """Docstring"""
        self.main.t_max = 23
        self.main.send_action_to_hvac = MagicMock()
        self.main.analyze_datapoint("2023-06-01", 24)
        self.main.send_action_to_hvac.assert_called_with("2023-06-01", "TurnOnAc", \
                                                         self.main.tickets)

    def test_analyze_datapoint_turn_on_heater(self):
        """Docstring"""
        self.main.t_min = 18
        self.main.send_action_to_hvac = MagicMock()
        self.main.analyze_datapoint("2023-06-01", 16)
        self.main.send_action_to_hvac.assert_called_with("2023-06-01", "TurnOnHeater", \
                                                         self.main.tickets)

    def test_analyze_datapoint_no_action(self):
        """Docstring"""
        self.main.send_action_to_hvac = MagicMock()
        self.main.analyze_datapoint("2023-06-01", 20)
        self.assertFalse(self.main.send_action_to_hvac.called)



    def test_send_event_to_database(self):
        """Docstring"""
        with patch("builtins.print") as mock_print:
            self.main.send_event_to_database("2023-06-01", "TurnOnAc")
            mock_print.assert_called_with("2023-06-01", "TurnOnAc")

    def test_send_temperature_to_fastapi(self):
        """Docstring"""
        with patch("builtins.print") as mock_print:
            self.main.send_temperature_to_fastapi("2023-06-01", 25.5)
            mock_print.assert_called_with("2023-06-01", 25.5)

if __name__ == '__main__':
    unittest.main()
