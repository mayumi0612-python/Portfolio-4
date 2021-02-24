from tkinter import *
from tkinter import scrolledtext
import json

############################################################
################## Constant Variable ########################
############################################################

FONT = font = ("Courier", 10)
BASE_COLOR = "#9ad3bc"
ORANGE = "#ec524b"

###############################################################
########## Dogs' Data ##########################################
################################################################
with open("rating.json") as file:
    data = json.load(file)
    dog_data = data["dog_breeds"]

    dog_name_list = []

    for dog in dog_data:
        dog_name_list.append(dog)


#################################################################
############## Function #########################################
##################################################################

def selected():
    global select_dog
    selected_dog = select_dog.get()
    canvas_4.itemconfig(user_choice_dog, text=f"{selected_dog}\n\nのことを知りたい")

    selected_dog_data = dog_data[selected_dog]

    size = selected_dog_data['Size']
    general_health = selected_dog_data['General Health']
    hot_weather = selected_dog_data['Tolerates Hot Weather']
    cold_weather = selected_dog_data['Tolerates Cold Weather']
    tolerance_being_alone = selected_dog_data['Tolerates Being Alone']
    intelligence = selected_dog_data['Intelligence']
    exercise = selected_dog_data['Exercise Needs']
    tendency_weight_gain = selected_dog_data['Potential For Weight Gain']

    output_box.insert(END, f"{selected_dog}の特徴を下記に表示するよ。\nそれぞれの項目を1～5のレベルに分類したよ\n\n")

    output_box.insert(END, f"サイズレベルは{size}\n")
    output_box.insert(END, f"一般的な健康レベルは{general_health}\n")
    output_box.insert(END, f"寒さに対する耐性のレベルは{cold_weather}\n")
    output_box.insert(END, f"暑さに対する耐性のレベルは{hot_weather}\n")
    output_box.insert(END, f"一匹でお留守番できるかのレベルは{tolerance_being_alone}\n")
    output_box.insert(END, f"知性レベルは{intelligence}\n")
    output_box.insert(END, f"運動の必要量は{exercise}\n")
    output_box.insert(END, f"太りやすさは{tendency_weight_gain}\n\n")
    output_box.insert(END, f"です。")


def clear():
    output_box.delete("1.0", END)


##################################################################
######### User Interface ########################################
#################################################################

root = Tk()
root.title("Dog Lovers!")
root.config(padx=50, pady=50, bg=BASE_COLOR)

####### Dog Image  ####################

canvas = Canvas(width=128, height=128, bg=BASE_COLOR, highlightthickness=0)
dog_image = PhotoImage(file="images/dog_image.png")
canvas.create_image(66, 70, image=dog_image)
canvas.grid(row=0, column=0, padx=50)

canvas_2 = Canvas(width=362, height=222, bg=BASE_COLOR, highlightthickness=0)
hukidashi = PhotoImage(file="images/hukidashi.png")
canvas_2.create_image(181, 111, image=hukidashi)
dog_talk = canvas_2.create_text(180, 95, text="何犬のことを知りたい？\n\n下のドロップダウンメニューからえらんでね", width=250,
                                fill=ORANGE, font=FONT)
canvas_2.grid(row=0, column=1)

### Dropdown Menu ################

select_dog = StringVar()
select_dog.set(dog_name_list[0])
dropdown_menu = OptionMenu(root, select_dog, *dog_name_list)

dropdown_menu.config(width=25, font=FONT, fg=ORANGE)
dropdown_menu.grid(row=1, column=0, pady=50)

####### Select button ################

select_button = Button(root, text="この犬を知りたい！", command=selected, fg=ORANGE, font=FONT)
select_button.grid(row=1, column=1, ipadx=20)

######## Duck Image ###############

canvas_3 = Canvas(width=140, height=128, bg=BASE_COLOR, highlightthickness=0)
duck_image = PhotoImage(file="images/duck_image.png")
canvas_3.create_image(75, 66, image=duck_image)
canvas_3.grid(row=2, column=1)

canvas_4 = Canvas(width=362, height=222, bg=BASE_COLOR, highlightthickness=0)
canvas_4.create_image(181, 111, image=hukidashi)
user_choice_dog = canvas_4.create_text(150, 90, text="考え中　...", fill=ORANGE, font=FONT)
canvas_4.grid(row=2, column=0)

######### Output box ######################

output_box = scrolledtext.ScrolledText(root, width=50, height=10)
output_box.grid(row=3, column=0, columnspan=2, pady=10)

clear_button = Button(text="ボックスのデータを消す", command=clear, font=FONT, fg=ORANGE)
clear_button.grid(row=4, column=0, columnspan=2, pady=10, ipadx=50)

root.mainloop()
