

#!/usr/bin/python
# -*- coding: utf-8 -*-
 
import random 
import YanAPI
import sys
import os
ip_addr = "10.12.6.50"
YanAPI.yan_api_init(ip_addr)
isCanGaitControl = False
is_need_reset_gait_control = False
is_on_stop = False


quiz_data = {

    "animals": [
        {"question": "What is the largest land animal?", "answer": "elephant"},
        {"question": "What do pandas primarily eat?", "answer": "bamboo"}
    ],
    "countries": [
        {"question": "What is the capital of France?", "answer": "paris"},
        {"question": "Which country is known as the Land of the Rising Sun?", "answer": "japan"}
    ],
    "math": [
        {"question": "What is 5 + 7?", "answer": "12"},
        {"question": "What is the square root of 16?", "answer": "4"}
    ],
    "general knowledge": [
        {"question": "Who wrote 'Hamlet'?", "answer": "shakespeare"},
        {"question": "What is the chemical symbol for water?", "answer": "h2o"}
    ]
}


def greet_user():
    YanAPI.sync_do_tts("Hello! I see you. Let's play a quiz game!", True)

"""def ask_category():

    YanAPI.sync_do_tts("Please choose a category: animals, countries, math, or general knowledge.", True)
    
    category = YanAPI.sync_do_voice_iat_value()
    if category in quiz_data:
        return category
    else:
         YanAPI.sync_do_tts("I didn't understand that. Please choose one of the given categories.", True)
         return ask_category()"""
         
def ask_category():
    YanAPI.sync_do_tts("Please choose a category: animals, countries, math, or general knowledge.", True)
    
    #category = YanAPI.sync_do_voice_iat_value().lower()
    # Normalize input to lowercase
    category = input("Enter Category : \n")
    print(f"Received category: {category}")  # Debugging line

    if category in quiz_data:
        return category

    else:
        YanAPI.sync_do_tts("I didn't understand that. Please choose one of the given categories.", True)
        return ask_category()

def reset_robot():
    global is_on_stop
    is_on_stop = True
    YanAPI.stop_voice_iat()
    YanAPI.stop_voice_tts()
    


 
def ask_question(category):
    question_set = random.choice(quiz_data[category])
    YanAPI.sync_do_tts(question_set["question"], True)
    return question_set



def check_answer(correct_answer):
    #user_answer = YanAPI.sync_do_voice_iat_value()
    user_answer = input("Enter Answer \n") 
    print(user_answer)
    if user_answer == correct_answer:
        YanAPI.sync_do_tts("Correct! Well done!", True)
        return True
    else:
        YanAPI.sync_do_tts(f"Sorry, the correct answer was {correct_answer}. Game over.", True)
        return False


# Main function to start the quiz
def start_quiz():
    score = 0
    while True:
        category = ask_category()
        question_set = ask_question(category)
        if check_answer(question_set["answer"]):
            score += 1
            
            YanAPI.sync_do_tts(f"Your score is now {score}. Let's continue!", True)
        else: 
            YanAPI.sync_do_tts("Let's start again.", True)
            score = 0
            
            
#Function to detect the user and start the game
"""def detect_user_and_start():
    while True:
        
        if YanAPI.sync_do_face_recognition('recognition') == 1:  # Assuming `detect_face()` returns True when a face is detected
            greet_user()
            start_quiz()"""


# Start the game

#YanAPI.sync_do_tts("I am ready to start the quiz game. Please come in front of the camera.", True)
#detect_user_and_start()
#start_quiz()
#reset_robot()

 
 
def __highlight_block(block_id=None):
    if block_id:
        sys.stdout.write("\r")
        sys.stdout.write(block_id)
        sys.stdout.flush()
 
 
def __validation_response(res=None):
    if res:
        if res['code'] == 7 or res['code'] == 20001:
            sys.stdout.write("\r")
            sys.stdout.write("message:CAMERA_BUSY")
            sys.stdout.flush()
            os._exit(0)
 
 
def compare_face_by_name(name, block_id=None):
    __highlight_block(block_id)
    result = False
    try:
        res = YanAPI.sync_do_face_recognition('recognition')
        __validation_response(res)
        if res is not None:
            recognition = res['data']['recognition']
            if recognition:
                result_name = recognition["name"]
                if result_name and result_name != 'none':
                    if result_name and result_name == name:
                        return True
    except:
        print('bad program')
 
    return result
 
def tts(content, block_id=None):
    __highlight_block(block_id)
    try:
        YanAPI.sync_do_tts(content, True)
    except:
        print('bad program')
 
def reset_robot():
    global is_on_stop
    is_on_stop = True
    YanAPI.stop_voice_iat()
    YanAPI.stop_voice_tts()
    # Since Reset and exit motion are pretty much the same, so if
    # have gait we only need exit, if not, use hts reset
    if is_need_reset_gait_control:
        YanAPI.exit_motion_gait()
    else:
        YanAPI.start_play_motion(name = "Reset", repeat = 1)
    YanAPI.set_robot_led("button", "white", "reset")
 
if __name__ == '__main__':
    # block program start here
     #--------------------------
 
    YanAPI.sync_do_tts("I am ready to start the quiz game. Please come in front of the camera.", True)
    if (compare_face_by_name('islam magdy', block_id="1725355654379")):
 
        #show_tts.
        tts("hi islam magdy", block_id="1725355588442")
        start_quiz()
    else:
        YanAPI.sync_do_tts("you are not allowed to do the quiz", True)
 
    if (compare_face_by_name('ahmed amin', block_id="1725355704986")):
 
        #show_tts.
        tts("hi ahmed amin", block_id="1725355714894")
        start_quiz()
    else:
        YanAPI.sync_do_tts("you are not allowed to do the quiz", True)
 
 
 
    if (compare_face_by_name('ahmed hagag', block_id="1725355941372")):
 
        #show_tts.
        tts("hi ahmd hagag", block_id="1725355775759")
        start_quiz()
    else:
        YanAPI.sync_do_tts("you are not allowed to do the quiz", True)
 
 
    #--------------------------
     # block program end
 
 
    # Reset robot
    reset_robot()

