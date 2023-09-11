import inflect

def bid_adieu(names):
    p = inflect.engine()
    length = len(names)
    text = "Adieu, adieu"
    if length == 1:
        return f" {text} to {names[0]}"
    else:
        rhymes = f" {text} to {', '.join(names[:-1])}"
        if length == 2:
            return f"{rhymes} and {names[-1]}"
        else:
            return f"{rhymes}, and {names[-1]}"

names = []
print("Names: ")
try:
    while True:
        name = input()
        names.append(name)
except EOFError:
    pass

print(bid_adieu(names))
