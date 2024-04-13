import os
import django
import json

# Configure Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hacknu24.settings")
django.setup()
from reading_module.models import Reading_module

with open("data.json", "r") as f:
    data = json.load(f)

    for item in data:
        text_content = item["text"]
        question_text = item["question"]
        correct_answers = next(
            answer["text"] for answer in item["answers"] if answer["correct"]
        )

        options = []
        for i in item["answers"]:
            options.append(i["text"])
        # Create ReadingModule object
        reading_module = Reading_module.objects.create(
            text=text_content,
            questions=question_text,
            options=options,
            answer=correct_answers,
            level=item["level"],
        )
