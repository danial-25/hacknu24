import json
import random
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hacknu24.settings")
django.setup()
from grammmar.models import Grammar_find_word
from grammmar.models import Grammar_choose_correct

with open("grammar_endings.json", "r", encoding="utf-8") as file:
    data = json.load(file)
for i in data:
    Grammar_choose_correct.objects.create(
        question=i["question"],
        answer=i["correct_answer"],
        word_to_replace=i["word_to_replace"],
        options=i["options"],
    )
# Grammar_choose_correct.objects.create(question=data['question']
# with open("sentences.json", "r", encoding="utf-8") as file:
#     data = json.load(file)

# # Extract the lists from the loaded data
# kaz = data["kaz"]
# rus = data["rus"]

# find_missing = kaz[: len(kaz) // 2]
# words_options = [word for string in kaz for word in string.split()]

# for i in find_missing:
#     words = i.split()

#     random_word = random.choice(words)

#     output_string = i.replace(random_word, "*")
#     random_words = random.sample(words_options, 3)
#     random_words.append(random_word)
#     Grammar_find_word.objects.create(
#         text=output_string, answer=random_word, options=random_words
#     )
# print("Output string:", output_string, random_word,random_words)
