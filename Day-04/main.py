 
students = [
    ("rahul", 45),
    ("ram",34),
    ("Keshav",67),
    ("rohit",87)
]

for name,marks in students:
    print(f"name:{name},marks:{marks}")

marks_list = []

for name,marks in students:
    marks_list.append(marks)


print("\nTotal Students:", len(students))

print("Highest Marks:", max(marks_list))

print("Lowest Marks:", min(marks_list))

print("Average Marks:", sum(marks_list) / len(marks_list))

print("\nSorted Marks:", sorted(marks_list))



languages = ["java","c++","js","Go","Python"]


print(languages[0],languages[-1],languages[2])




Num = [1,2,3,4,5,6,7,8,9,10]


Num.extend([11,12])

del Num[2]

Num[4] = 33

print(Num)



print(max(Num))
print(min(Num))
avarage = sum(Num) / len(Num)
print(avarage)


Numd = [1,2,3,1,1,1,1,2,2,3,3]

Numdd =[]

for N in Numd:
    if N not in Numdd:
      Numdd.append(N)

print(Numdd)



student = ("Kunal", 21, 8.7)

name, age, cgpa = student

print(name)
print(age)
print(cgpa)

