import os
import json

years = ['2563', '2564']
total_courses = []

for year in years:
  filenames = os.listdir(year)
  for filename in filenames:
    with open(f'{year}/{filename}', mode='r', encoding='utf8') as jsonFile:
      courses = json.load(jsonFile)
      total_courses.extend(courses)
      print(f'Appended {year}/{filename}: {len(courses)} courses, total: {len(total_courses)}')

print(f'Total courses: {len(total_courses)} courses')
with open('courses.json', mode='w', encoding='utf8') as courseFile:
  json.dump(total_courses, courseFile, ensure_ascii=False)