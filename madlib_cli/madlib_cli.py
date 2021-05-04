""" somthing """
import re
import random
import sys

print("Welcome to Madlib game, please input the blanks")
def start_game():
    print("""
    Konnichiwa😎!
    Welcome to Madlib game ....
    in this game you should fill the blanks
    after you finish I will surprise you 😄!
    Are you ready ?
    lets get started 🔥....
    """)

start_game()

def read_template(file_path):
    try:
      with open(file_path, "r") as f_path:
       return f_path.read().strip("\n")
    except FileNotFoundError:
      raise FileNotFoundError('A very specific bad thing happened.')
    except:
       print("Other error")


    


def parse_template(text):
    parts = []
    parts = re.findall(r"\{.*?\}", text)
    for i in range(len(parts)):
        parts[i] = parts[i].replace("{", "")
        parts[i] = parts[i].replace("}", "")
        # parts[i] = parts[i].replace(r"\{", "")

    for i in range(text.count("{")):
        text = text.replace(parts[i], "")
    parts_t = ()
    for i in parts:
        parts_t = parts_t + (i,)
    print(text)
    print(parts_t)
    return text, parts_t


def merge(text, parts):
    return text.format(*parts)


def create_file(result):
    n = random.random()
    with open("assets/f{}.txt".format(str(n)), "w") as f:
        f.write(result)



print(merge("It was a {} and {} {}.", ("dark", "stormy", "night")))
def receive_data():
    text = read_template("assetsr/make_me_a_video_game_template.txt")
    stripped_text, parts_tuple = parse_template(text)
    user_answers = []

    for i in range(len(parts_tuple)):
        x = input('enter a {} >'.format(parts_tuple[i]))
        user_answers.append(x)
    result = stripped_text.format(*user_answers)
    print(result)
    create_file(result)







