from plyer import notification
import time

from pyexpat.errors import messages

if __name__ == '__main__':
        while True:
            notification.notify(
                title = " ******Take Rest ******* ",
                message = " Rest is very important for you. Take rest for  4-5 minutes and come back again to  complete your task or work. If you take rest you fell fresh and you done your work in right way. You are healthy, if you take rest.",
                # app_icon = "copy1.png",
                timeout = 5
            )
            time.sleep(60*60*60)



# To run any phython file in background, we need to write code in cmd : "pythonw *filename*"