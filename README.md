# Code Functionality

This Python code demonstrates a basic functionality to create a bot that performs the following tasks:

1. Makes a GET request to the "quotable.io" API to fetch a random quote.
2. Detects a specified image on the screen using image recognition.
3. If the image is found with a confidence level of at least 70%, it presses the '/' key and types the fetched quote.

## Prerequisites

Before running this code, make sure you have the following:

- Python installed on your system.
- Required modules installed: `pyautogui`, `requests`, `pyscreeze`, and `discord_webhook`. You can install them using `pip` with the command: `pip install pyautogui requests pyscreeze discord_webhook`.

## Usage

1. Import the required modules: `sys`, `pyautogui`, `requests`, `pyscreeze`, and `discord_webhook`.
2. Set the `url` variable to the API endpoint, which in this case is 'https://api.quotable.io/random'.
3. Set the `image_to_detect` variable to the file path of the image you want to detect on the screen.
4. Set the `confidence_threshold` variable to the minimum confidence level (between 0 and 1) required for image matching.
5. Run an infinite loop using `while True` to continuously perform the following tasks:
   - Send a GET request to the API using `requests.get(url)`.
   - If the response status code is 200 (indicating a successful request), extract the quote content from the response JSON.
   - Use `pyscreeze.locateAll` to detect the specified image on the screen with the defined confidence threshold.
   - If the image is found, press the '/' key using `pyautogui.press('/')` and type the quote using `pyautogui.typewrite(phrase)`.
   - If the image is not found, print a message indicating that the image was not found.
   - If the API request fails, print an error message along with the response status code.

Please note that this code assumes the availability of the required modules and a working internet connection to access the API.

Feel free to customize the code according to your specific requirements.

**Disclaimer:** This code is provided as a basic demonstration and may require additional error handling and edge case considerations depending on your specific use case.

## Bug Reporting

If you encounter any bugs or issues, please report them on our Discord server: [https://discord.gg/ymmcwwAYjB](https://discord.gg/ymmcwwAYjB).
