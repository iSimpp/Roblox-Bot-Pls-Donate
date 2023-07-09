import pyautogui
import requests
import pyscreeze

url = 'https://api.quotable.io/random'
image_to_detect = r"" # Between the "" put your file containing an image of you getting a 5 robux donation.
confidence_threshold = 0.7  # Set the minimum confidence level for image matching

while True:
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        phrase = data["content"]

        matches = pyscreeze.locateAll(image_to_detect, confidence=confidence_threshold)

        if len(list(matches)) > 0:
            pyautogui.press('/')
            pyautogui.typewrite(phrase)
        else:
            print("Image not found.")
    else:
        print("Request failed with status code:", response.status_code)
