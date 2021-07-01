import os
import json

dayOfWeeks = set()
genEdTypes = dict()
studyPrograms = set()
classTypes = set()

courseNull = 0
dayOfWeekNull = 0
typeNull = 0
genEdTypeNull = 0
departmentNull = 0
creditNull = 0

DayARPeriodNotAR = 0

with open('courses.json', mode='r', encoding='utf8') as courseFile:
  courses = json.load(courseFile)
  print(len(courses))
  # print(courses)
  for course in courses:
    if course is None:
      print("COURSE NULL")
      courseNull += 1
      continue
    if "genEdType" in course:
      if course["genEdType"] not in genEdTypes:
        genEdTypes[course["genEdType"]] = 0
      genEdTypes[course["genEdType"]] += 1
    else:
      print("genEdType null", course["courseNo"], course["semester"], course["studyProgram"], course["academicYear"])
      genEdTypeNull += 1
    if "department" not in course:
      departmentNull += 1
    if "credit" not in course or course["credit"] == None:
      # print("CREDIT NULL")
      creditNull += 1
    studyPrograms.add(course["studyProgram"])
    hasDayOfWeek = 0
    for section in course["sections"]:
      for classObject in section["classes"]:
        if "dayOfWeek" in classObject:
          dayOfWeeks.add(classObject["dayOfWeek"])
          if classObject["dayOfWeek"] == "AR":
            if "period" in classObject and classObject["period"]["start"] != "AR":
              DayARPeriodNotAR += 1
          #     print("dayOfWeeks", classObject["dayOfWeek"],"period", classObject["period"], course["courseNo"], course["studyProgram"], course["academicYear"])
          #   elif "period" not in classObject:
          #     print("period missing!")
          # elif "period" in classObject and classObject["period"]["start"] == "AR":
          #   print("dayOfWeeks", classObject["dayOfWeek"],"period", classObject["period"], course["courseNo"], course["studyProgram"], course["academicYear"])
        else:
          # print("dayOfWeek null", course["courseNo"], course["semester"], course["studyProgram"], course["academicYear"])
          hasDayOfWeek = 1
        if "type" in classObject:
          classTypes.add(classObject["type"])
        else:
          typeNull += 1
    dayOfWeekNull += hasDayOfWeek

print("courseNull", courseNull)
print("dayOfWeekNull", dayOfWeekNull)
print("typeNull", typeNull)
print("genEdTypeNull", genEdTypeNull)
print("departmentNull", departmentNull)
print("creditNull", creditNull)
print("DayARPeriodNotAR", DayARPeriodNotAR)
print('totalCourses', len(courses))

print(dayOfWeeks)
print(genEdTypes)
print(studyPrograms)
print(classTypes)
