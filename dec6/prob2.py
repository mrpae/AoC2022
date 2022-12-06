with open('input1.txt') as f:
    message=''.join(line.rstrip() for line in f)    # the input is stored here

# 1) split four letter substring into a list of characters
# 2) put those elements into a set
# 3) if the number of elements in that set is =3, then there were repeating characters
# in the original four letter substring
# 4) create a while loop until the condition is satisfied

answer = 14

while answer <= len(message):
    if len(set([*message[answer-14:answer]])) != 14:
        answer += 1
    else:
        break

print(answer)
