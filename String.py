id = int(input('Enter Your ID (1-100): '))
name = str(input('Enter Your name (3-12): '))
gender = str(input('Enter Your gender (M, F): '))
while not(gender == 'M' or gender == 'F'):
    gender = str(input('Please Enter Your gender again! (M, F): '))
group = str(input('Enter Your group: '))

student = []
student.append(
    {
        'id': id,
        'name': name,
        'gender': gender,
        'group': group,
    },
)

for item in student:
    print(f"Id: {item['id']} - Name: {item['name']}")
