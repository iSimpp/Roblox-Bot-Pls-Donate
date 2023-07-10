from discord_webhook import DiscordWebhook, DiscordEmbed
import pyautogui
import requests
import pyscreeze
import time
import asyncio

def Send_Message(Title, Description, Color, Url):
    # create embed object for webhook
    embed = DiscordEmbed(title=Title, description=Description, color=Color)
    webhook = DiscordWebhook(url=Url)

    # add embed object to webhook
    webhook.add_embed(embed)

    response = webhook.execute()


url = 'https://api.quotable.io/random'
image_to_detect = r"<PATH_TO_IMAGE>"
confidence_threshold = 0.7  # Set the minimum confidence level for image matching

def Bot():
    while True:
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            phrase = data["content"]

            screenshot = pyscreeze.screenshot()
            matches = pyscreeze.locateAll(needleImage=image_to_detect, haystackImage=screenshot, confidence=confidence_threshold)

            if len(list(matches)) > 0:
                pyautogui.press('/')
                pyautogui.typewrite(phrase, interval=0.1)
                pyautogui.press('enter')
                time.sleep(0.1)
                pyautogui.press('/')

                pyautogui.write('/clear')
                pyautogui.press('enter')
                Send_Message('Someone donated 5 Robux!', 'Okay, so you now have 5 robux more :sunglasses:', ' 8cff00', '<DISCORD_WEBHOOK_URL>')
                time.sleep(5)  # Delay for 5 seconds before the next iteration
            else:
                print("Image not found.")
        else:
            print("Request failed with status code:", response.status_code)

# Call the Bot function to start the bot
Bot()
