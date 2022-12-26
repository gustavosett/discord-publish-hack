from app.app import Application
from app.timer import timer
from datetime import datetime


def driver(discord_login, time):
    main = Application(discord_login)
    try:
        print("\nStarting process..")
        result = main.start()
        if result == True:
            print(f"{str(datetime.now())[:19]} completed successfully! :)")
            timer(time)
        else:
            print(f"{str(datetime.now())[:19]} one error occurred... :(")
            timer(10)
    except:
        print("oops! Something went wrong..")
        timer(10)
        pass
