from app.app import Application, ANSI
from app.timer import timer
from datetime import datetime


def driver(discord_login, time):
    main = Application(discord_login)
    try:
        print("\nStarting process..")
        result = main.start()
        if result == True:
            print(f"{str(datetime.now())[:19]} " 
                  + ANSI.color_text(32) + 
                  "completed successfully! :)" 
                  + ANSI.color_text(0))
            timer(time)
        else:
            print(f"{str(datetime.now())[:19]} " 
                  + ANSI.color_text(31) + 
                  "one error occurred, cannot bumped! :(" 
                  + ANSI.color_text(0))
            timer(10)
        main.quit()
    except:
        print(ANSI.color_text(31) + 
              "oops! Something went wrong.." 
              + ANSI.color_text(0))
        timer(10)
        pass
