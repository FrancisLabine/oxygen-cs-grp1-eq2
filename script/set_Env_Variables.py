import os

if not os.environ.get('TOKEN') :
    raise Exception("TOKEN INEXISTANT")

if not os.environ.get('HOST') :
    os.environ['HOST'] = "http://34.95.34.5"

if not os.environ.get('TICKETS') :
    os.environ['TICKETS'] = '6'

if not os.environ.get('T_MAX') :
    os.environ['T_MAX'] = '35'

if not os.environ.get('T_MIN') :
    os.environ['T_MIN'] = '15'

if not os.environ.get('DATABASE') :
    os.environ['DATABASE'] = "oxygendb"
