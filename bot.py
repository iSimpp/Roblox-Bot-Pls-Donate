import pyautogui
import requests
import pyscreeze

url = 'https://api.quotable.io/random'
image_to_detect = r"image"
confidence_threshold = 0.7  # Set the minimum confidence level for image matching

while True:
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        phrase = data["content"]

        screenshot = pyscreeze.screenshot()
        matches = pyscreeze.locateAll(needleImage=image_to_detect, haystackImage=screenshot, confidence=confidence_threshold)

        if len(list(matches)) > 0:
            pyautogui.press('/')
            pyautogui.typewrite(phrase)
        else:
            print("Image not found.")
    else:
        print("Request failed with status code:", response.status_code)
