careers = ["doctor", "lawyer", "chef", "librarian"]
print(careers.index("chef"))
print("lawyer" in careers)
careers.append("competitive eater")
careers.insert(0, "teacher")
for job in careers:
    print(job)