brackets = "{[()]}"

stack = []

for bracket in brackets:

    if bracket in "([{":
        stack.append(bracket)

    elif bracket in ")]}":

        if len(stack) == 0:
            print("Not Balanced")
            break

        top = stack.pop()

        if (bracket == ")" and top != "(") or \
           (bracket == "]" and top != "[") or \
           (bracket == "}" and top != "{"):
            print("Not Balanced")
            break

else:
    if len(stack) == 0:
        print("Balanced")
    else:
        print("Not Balanced")
