import pyautogui
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from PIL import Image
import time
import keyboard


# Gets math question string and turns it into an actual Question
def GetQuestionString():
    time.sleep(0.4)
    newQuestion = pyautogui.locateOnScreen("question.png", confidence=0.88)
    if newQuestion:
        left, top, width, height = map(int, (newQuestion.left, newQuestion.top, newQuestion.width, newQuestion.height))
        pyautogui.screenshot("Temp_Question.png", region=(left, top, width, height))

        time.sleep(0.25)

        # Perform OCR on the temporary image
        questionText = tess.image_to_string(Image.open("Temp_Question.png"))
        time.sleep(0.3)
        print("The raw text is: " + questionText)
    return (questionText)


# refines the string into something Python can solve and solves it!
def AnswerQuestionString(questionString):
    # Takes the string, lower-cases it
    newStr = questionString

    # Gets rid of any fluff
    newStr = newStr.replace("?", "")
    newStr = newStr.replace("‘", "")
    newStr = newStr.replace(",", ".")
    newStr = newStr.replace(" ", "")

    # Takes all possible operators and turns them into proper ones
    newStr = newStr.replace("plus", "+")
    newStr = newStr.replace("minus", "-")
    newStr = newStr.replace("times", "*")
    newStr = newStr.replace("divided", "/")
    newStr = newStr.replace("by", "")

    print(newStr)

    # Gets rid of lang text
    for char in newStr:
        if char.isalpha():
            newStr = newStr.replace(char, "")
        else:
            break

    print(newStr)
    answer = eval(newStr)
    answer = round(answer, 2)
    print("The answer is: " + str(answer))


# Change the exit_key variable to the key you want to use for exiting
exit_key = 'esc'

while not keyboard.is_pressed(exit_key):
    if keyboard.is_pressed("alt"):
        AnswerQuestionString(GetQuestionString())



print("Exiting gracefully...")
# Add any cleanup code here if needed



