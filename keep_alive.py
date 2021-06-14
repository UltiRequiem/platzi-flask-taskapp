from threading import Thread
import random
from app import create_app

app = create_app()


def keep_alive():
    t = Thread(target=app.run(host="0.0.0.0", port=random.randint(2000, 9000)))
    t.start()

