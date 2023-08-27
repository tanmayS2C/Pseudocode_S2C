"""
fc = first_condition
lo = left_operand
ro =right_operand
o = operator
ao = andor
cc = combined_condition
"""

fc = [
    {"lo": "5", "ro": "5", "o": "=="},
    {"ao": "and"},
    {"lo": "7", "ro": "8", "o": "=="},
    {"ao": "and"},
    {"lo": "7", "ro": "7", "o": "=="},
    {"Lname": "Tanmay"},
]

cc = fc[0]["lo"] + " " + fc[0]["o"] + " " + fc[0]["ro"] + " "

for i in range(1, len(fc) - 2, 2):
    cc += (
        fc[i]["ao"]
        + " "
        + fc[i + 1]["lo"]
        + " "
        + fc[i + 1]["o"]
        + " "
        + fc[i + 1]["ro"]
        + " "
    )

print(cc)
print(eval(cc))

if eval(cc):
    print(fc[-1])
