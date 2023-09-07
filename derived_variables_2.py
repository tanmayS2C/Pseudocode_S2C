import uuid

"""
fc = first_condition
sc = second_condition
oc = all_condition
lo = left_operand
ro =right_operand
o = operator
ao = andor
cc = combined_condition
"""

fc = [
    {"lo": "'5e'", "ro": "'8e'", "o": "=="},
    {"ao": "and"},
    {"lo": "'7'", "ro": "'7'", "o": "=="},
    {"ao": "and"},
    {"lo": "'7'", "ro": "'7'", "o": "=="},
    {"Lname": "First Condition"},
]

sc = [
    {"lo": "5", "ro": "5", "o": "=="},
    {"ao": "and"},
    {"lo": "7", "ro": "7", "o": "=="},
    {"Lname": "Second Condition"},
]

uuid1 = str(uuid.uuid4())
uuid2 = uuid1

tc = [{"lo": f"'{uuid1}'", "ro": f"'{uuid2}'", "o": "=="}, {"Lname": "Third Condition"}]

oc = [fc,sc,tc]
result = "Default Else condition"

for cond in oc:
    cc = cond[0]["lo"] + " " + cond[0]["o"] + " " + cond[0]["ro"] + " "

    for i in range(1, len(cond) - 2, 2):
        cc += (
            cond[i]["ao"]
            + " "
            + cond[i + 1]["lo"]
            + " "
            + cond[i + 1]["o"]
            + " "
            + cond[i + 1]["ro"]
            + " "
        )

    print(cc, eval(cc))

    if eval(cc):
        result = cond[-1]
        break

print(result)



"""
>>> uuid.uuid4()
UUID('8b69144c-8d7d-4f63-a550-427cd72221ab')
>>> str(uuid.uuid4()).isdigit()
False
>>> str("1223").isdigit()
True
ss    
"""