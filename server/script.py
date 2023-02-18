import datetime
import pyautogui as pg
import asyncio
import os

async def check_time(input_hour):
    while True:
        hour = datetime.datetime.now().time().hour
        minute = datetime.datetime.now().time().minute

        if int(hour) == input_hour and int(minute) >= 1:
            left = 60 - int(minute)
            message = 'Через ' + str(left) + ' минут пк будет выключен'

            pg.alert(text=message, title='Предупреждение', button='OK')

            shutdown = "shutdown -s -t " + str(60 * left)
            os.system(shutdown)

        elif int(hour) > input_hour:
            os.system("shutdown -s -t 60")

        print("Бесконечный цикл")
        await asyncio.sleep(15)

if __name__ == '__main__':
    input_hour = int(input("Когда спать? - "))

    loop = asyncio.get_event_loop()
    asyncio.ensure_future(check_time(input_hour))
    loop.run_forever()