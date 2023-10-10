def my_name_is():
    print("My name is paritos chandra")


def i_have_enrolled_course(course_name):
    print(f"I have enrolled in a course named {course_name}")


def i_have_learning(backend, frontend):
    return f"Learning {backend}, {frontend}"


course_and_learn=[
    {"course": "Python & Web",
     "backend":"html,css,javascript",
     "frontend":"Python"
    }
]
for item in course_and_learn:
    Course_name=item["course"]
    backend=item["backend"]
    frontend=item["frontend"]

my_name_is()
i_have_enrolled_course("python & web")
result=i_have_learning(backend,frontend)
print(result)
print(type(backend))

