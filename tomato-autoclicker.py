from pynput.mouse import Button, Controller
import time
import keyboard
mouse = Controller()
print("by DomatesGames from Github")
baslamatusu = input("Otomatik tıklama hangi tuşa basıldığında başlasın? ")
durmatusu = input("Hangi tuşa basıldığında dursun? (Başlama tuşuyla aynı olmasın.) ")
print("Başladı, lütfen başlatmak için " + baslamatusu + " tuşuna basın. Durdurmak için de " + durmatusu + " tuşuna basın.")
while(True):
    if keyboard.is_pressed(baslamatusu):
        while(True):
            mouse.press(Button.left)
            mouse.release(Button.left)
            time.sleep(0.01)
            if keyboard.is_pressed(durmatusu):
                break
