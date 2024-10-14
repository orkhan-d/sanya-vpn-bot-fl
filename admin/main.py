import os
import sys
sys.path.append(os.getcwd())
from admin import app

import uvicorn

if __name__ == '__main__':
    uvicorn.run('app:app',
                host='0.0.0.0',
                port=8080,
                # ssl_keyfile='mykey.key',
                # ssl_certfile='mycert.crt',
                reload=True)
