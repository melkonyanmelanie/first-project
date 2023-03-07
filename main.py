import random 

def template_first():
   print("Great! First story selected!")
   number = input("Input any number: ")
   measure_of_time = input("Please, input a measure of time: ")
   transport = input("Input type of transportation: ")
   adj1 = input("Input an adjective: ")       
   adj2 = input("Input the second adjective: ")
   noun_first = input("Input a noun related to the later mentioned adjective: ")
   color = input("Input a color: ")
   part_of_body = input("Please, input a part of body: ")
   verb = input("Please, input a verb in bare infinitive form: ")
   number_two = input("Please, enter a number: ")
   noun_second = input("Input any noun: ")
   noun_third = input("Please, input any noun: ")
   part_of_body_two = input("Please, input a part of body: ")
   verb_two = input("Please, input a verb in bare infinitive form: ")
   noun_forth = input("Input any noun: ")
   adj3 = input("Input an adjective: ")
   silly_word = input("Input a funny, crazy word: ")
   noun_fifth = input("Input your last noun: ")

   print(f"""It was about {number} {measure_of_time} ago when I arrived at the hospital in a {transport}. The hospital is a/an {adj1} place, there are a lot of {adj2} {noun_first} here. There are nurses here who have {color} {part_of_body}. If someone wants to come into my room I told them that they have to {verb} first. I’ve decorated my room with {number_two} {noun_second}. Today I talked to a doctor and they were wearing a {noun_third} on their {part_of_body_two}. I heard that all doctors {verb_two} {noun_forth} every day for breakfast. The most {adj3} thing about being in the hospital is the {silly_word} {noun_fifth}!""")

def second_template():
   print("Great! Second story selected!")
   persons_name = input("Input a person's name: ")
   noun_sec_templ = input("Please, input a noun: ")
   feeling = input("Input an adjective related to feelings: ")
   verb_sec_templ = input("Input a verb: ")       
   feeling_two = input("Input an adjective related to feelings: ")
   animal = input("Input a name of animal: ")
   verb_sec_templ_two = input("Input a verb: ")
   color_sec_templ = input("Please, input a color: ")
   verb_ing = input("Please, input a verb in verb+ing form: ")
   adverb_ly = input("Please, input an adverb in form adverb+ly: ")
   num_sec_templ = input("Input any number: ")
   time_sec_templ = input("Please, input a measure of time: ")
   color_animal = input("Please, input a color: ")
   second_animal = input("Please, input the name of second animal: ")
   num_num = input("Input any number: ")
   silly_word_2 = input("Input a silly word: ")
   noun_food = input("Input food item name : ")

   print(f"""This weekend I am going camping with {persons_name}. I packed my lantern, sleeping bag, and {noun_sec_templ}. I am so {feeling} to {verb_sec_templ} in a tent. I am {feeling_two} we might see {animal}, I hear they’re kind of dangerous. While we’re camping, we are going to hike, fish, and {verb_sec_templ_two}. I have heard that the {color_sec_templ} lake is great for {verb_ing}. Then we will {adverb_ly} hike through the forest for {num_sec_templ} {time_sec_templ}. If I see a {color_animal} {second_animal} while hiking, I am going to bring it home as a pet! At night we will tell {num_num} {silly_word_2} stories and roast {noun_food} around the campfire!!""")

def third_template():
   print("Great! Third story selected!")
   persons_name_third = input("Please, input person's name: ")
   adjective_1 = input("Please, input first adjective: ")
   color_3_templ = input("Please, input a color: ")
   animal_templ_3 = input("Please, input a name of animal: ")
   place_templ = input("Please, input a name of place: ")
   adjective_2 = input("Please, input second adjective (preferably of descriptive nature): ")
   magical_creature_plural = input("Please, input a name of a magical creature: ")
   adjective_3 = input("Please, input third adjective (preferably of descriptive nature): ")
   magical_creature_plural_2 = input("Please, input a name of a magical creature: ")
   room_in_house = input("Please, input name of room in house: ")
   plural_noun_third = input("Please, input a noun in plural form: ")
   noun_2_third_temp = input("Please, input a noun : ")
   plural_noun_2_third = input("Please, input a noun in plural form: ")
   adjective_4 = input("Please, input an adjective : ")
   plural_noun_3_third = input("Please, input a noun in plural form: ")
   num_third_templ = input("Please, input any number: ")
   time_templ_3 = input("Please, input a measure of time: ")
   verb_ing_templ_3 = input("Please, input a verb in form verb+ing: ")
   adjective_5 = input("Please, input an adjective : ")
   last_noun = input("Please, input a noun: ")

   print(f'''Dear {persons_name_third}, I am writing to you from {adjective_1} castle in an enchanted forest. I found myself here one day after going for a ride on a {color_3_templ} {animal_templ_3} in {place_templ}. There are {adjective_2} {magical_creature_plural} and {adjective_3} {magical_creature_plural_2} here! In the {room_in_house} there is a pool full of {plural_noun_third}. I fall asleep each night on a {noun_2_third_temp} of {plural_noun_2_third} and dream of {adjective_4} {plural_noun_3_third}  It feels as though I have lived here for {num_third_templ} {time_templ_3}. I hope one day you can visit, although the only way to get here now is {verb_ing_templ_3} on a {adjective_5} {last_noun}!!''')


text_template = input("Hello! Type 1, 2 or 3 to choose one of the templates!: ")
templates = ["1", "2", "3"]
function_names = ["second_template", "template_first", "third_template"]


if text_template == templates[0]:
   template_first()
elif text_template == templates[1]:
   second_template()
elif text_template == templates[2]:
   third_template()
else:
   print("Let us choose the text randomly!")
   selected_function_name = random.choice(function_names)
   result = eval(selected_function_name)()