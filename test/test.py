
import os
import unittest
class Tests(unittest.TestCase) :
    def main(self):
        self.Test_Scripts()

##Test scripts
    def test_Script_sql(self):
        try :
            exec(open(os.getcwd() + "/script/mySqlSetup.py").read())
        except Exception :
            self.fail("script sql retourne une exception.")
        
    def test_Script_EnvVar(self):
        try :
           exec(open(os.getcwd() + "/script/setEnvVariables.py").read())
        except Exception :
            self.fail("script de variable d'environnement retourne une exception.")

        self.assertEqual(os.environ.get("TOKEN"),"fHtJqgMACx")
        

if __name__ == '__main__':
    unittest.main()