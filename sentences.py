import json
import random
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hacknu24.settings")
django.setup()
from grammmar.models import Grammar_find_word
from grammmar.models import Grammar_choose_correct
from reading_module.models import Reading_puzzle
# with open("grammar_endings.json", "r", encoding="utf-8") as file:
#     data = json.load(file)
# for i in data:
    # Grammar_choose_correct.objects.create(
    #     question=i["question"],
    #     answer=i["correct_answer"],
    #     word_to_replace=i["word_to_replace"],
    #     options=i["options"],
    # )
# Grammar_choose_correct.objects.create(question=data['question']
with open("sentences.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# Extract the lists from the loaded data
kaz = data["kaz"]
rus = data["rus"]

kaz = kaz[(len(kaz) // 2)+1:]
# words_options = [word for string in kaz for word in string.split()]
rus=rus[(len(rus) // 2)+1:]
for i in range(len(kaz)):
    words = kaz[i].split()

    random.shuffle(words)
    shuffled_string = ' '.join(words)
    Reading_puzzle.objects.create(
        rus_word=rus[i], kaz_word=kaz[i], shuffled_kaz_word=shuffled_string
    )

