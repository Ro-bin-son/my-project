import time
from plyer import notification

if __name__ == '__main__':
    while True:

        time.sleep(5)
        notification.notify(
            title="ALERT!!",
            message="Wake Up",
            timeout= 5
        )

        time.sleep(10)
