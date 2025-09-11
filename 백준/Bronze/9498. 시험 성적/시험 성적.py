score = int(input())


match score:
    case score if score > 89:
        grade = 'A'
    case score if score > 79:
        grade = 'B'
    case score if score > 69:
        grade = 'C'
    case score if score > 59:
        grade = 'D'
    case _:
        grade = 'F'

print(grade)