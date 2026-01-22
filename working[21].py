import re

def main():
    global th
    th = {
        "12:am": "00:",
        "1:am": "01:",
        "2:am": "02:",
        "3:am": "03:",
        "4:am": "04:",
        "5:am": "05:",
        "6:am": "06:",
        "7:am": "07:",
        "8:am": "08:",
        "9:am": "09:",
        "10:am": "10:",
        "11:am": "11:",
        "12:pm": "12:",
        "1:pm": "13:",
        "2:pm": "14:",
        "3:pm": "15:",
        "4:pm": "16:",
        "5:pm": "17:",
        "6:pm": "18:",
        "7:pm": "19:",
        "8:pm": "20:",
        "9:pm": "21:",
        "10:pm": "22:",
        "11:pm": "23:",
            }
    print(convert(input("Hours: ")))


def convert(s):
    find = re.search(
        r"^(1[0-2]|[1-9])(:[0-5][0-9]\sPM|:[0-5][0-9]\sAM|\sPM|\sAM)\sto\s(1[0-2]|[0-9])(:[0-5][0-9]\sPM|:[0-5][0-9] AM|\sPM|\sAM)",
        s, re.IGNORECASE)
    try:
        x = find.group(1) + find.group(2)
        y = find.group(3) + find.group(4)
        fromthis = x if "pm" in x or "PM" in x else x if "am" in x or "AM" in x else None
        if fromthis:
            global f
            if "AM" in fromthis or "am" in fromthis:
                fromthis = fromthis.replace("AM", "am")
                if ":" in fromthis:
                    partes = fromthis.split(":")
                    a = f"{partes[0]}:am"
                    b = re.sub(r"[a-zA-Z]", "", partes[1])
                    f = f"{th[a]}{b}"
                else:
                    fromthis = fromthis.replace(" ", ":")
                    f = f"{th[fromthis]}00 "
            elif "PM" in fromthis or "pm" in fromthis:
                fromthis = fromthis.replace("PM", "pm")
                if ":" in fromthis:
                    partes = fromthis.split(":")
                    a = f"{partes[0]}:pm"
                    b = re.sub(r"[a-zA-Z]", "", partes[1])
                    f = f"{th[a]}{b}"
                else:
                    fromthis = fromthis.replace(" ", ":")
                    f = f"{th[fromthis]}00 "


        tothis = y if "pm" in y or "PM" in y else y if "am" in y or "AM" in y else None
        if tothis:
            global t
            if "PM" in tothis or "pm" in tothis:
                tothis = tothis.replace("PM", "pm")
                if ":" in tothis:
                    partes = tothis.split(":")
                    a = f"{partes[0]}:pm"
                    b = re.sub(r"[a-zA-Z]", "", partes[1])
                    t = f"{th[a]}{b}"
                else:
                    tothis = tothis.replace(" ", ":")
                    t = f"{th[tothis]}00 "
            elif "AM" in tothis or "AM" in tothis:
                tothis = tothis.replace("AM", "am")
                if ":" in tothis:
                    partes = tothis.split(":")
                    a = f"{partes[0]}:am"
                    b = re.sub(r"[a-zA-Z]", "", partes[1])
                    t = f"{th[a]}{b}"
                else:
                    tothis = tothis.replace(" ", ":")
                    t = f"{th[tothis]}00 "
        return f"{f}to {t}"
    except:
        raise(ValueError)
if __name__ == "__main__":
    main()
