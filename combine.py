import os
import json

filenames = os.listdir('2563')
total_courses = []
for filename in filenames:
  with open(f'2563/{filename}', mode='r', encoding='utf8') as jsonFile:
    courses = json.load(jsonFile)
    total_courses.extend(courses)

with open('courses.json', mode='w', encoding='utf8') as courseFile:
  json.dump(total_courses, courseFile, ensure_ascii=False)