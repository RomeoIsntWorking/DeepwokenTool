import keyboard
import pyautogui
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from PIL import Image
from fuzzywuzzy import fuzz
import time

phrases = ("Me-wow, is that the latest Felinor fashion?",
           "So, what's keeping you busy these days?",
           "Hey hivekin, can I bug you for a moment?",
           "So, how's work?",
           "Wow, this breeze is great, right?",
           "Sometimes I have really deep thoughts about life and stuff.",
           "Some weather we're having, huh?",
           "You ever been to a Canor restaurant? The food's pretty howlright.")



# Gets the required prompt
def GetPromptText():
    newPrompt = pyautogui.locateOnScreen("charisma.png", confidence=0.38)
    if newPrompt:
        # This takes the picture of the prompt
        left, top, width, height = map(int, (newPrompt.left, newPrompt.top, newPrompt.width, newPrompt.height))
        pyautogui.screenshot("Temp_Prompt.png", region=(left, top, width, height))
        time.sleep(0.25)

        promptText = tess.image_to_string(Image.open("Temp_Prompt.png"))
        print(promptText)
    return promptText


def CompareText(text):
    highestSimilarity = 0
    mostSimilar = ""

    for phrase in phrases:
        similarity = fuzz.ratio(text.lower(), phrase.lower())
        if similarity > highestSimilarity:
            highestSimilarity = similarity
            mostSimilar = phrase
    return mostSimilar


def EnterPrompt(newPrompt):
    pyautogui.write(newPrompt)
    keyboard.press_and_release('enter')
    print("Task Complete")


exit_key = 'esc'
while not keyboard.is_pressed(exit_key):
    if keyboard.is_pressed("alt"):
        prompt = CompareText(GetPromptText())
        EnterPrompt(prompt)


print("Exiting gracefully...")
# Add any cleanup code here if needed
