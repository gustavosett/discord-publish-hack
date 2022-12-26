from app.driver import driver

discord_logins = [
    {
    "email" : "YOUR EMAIL HERE",
    "password" : "PASSWORD HERE"
    },
]

time = int(7200 / len(discord_logins))

while True:
    for user in discord_logins:
        driver(user, time)