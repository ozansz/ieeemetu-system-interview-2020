from restructure import restructure_malformed_data

tests = [
    {
        "case": "oZan    SAzaK  ozan. sazA K@  gma il. Com",
        "answer": {
            "name": "Ozan",
            "surname": "Sazak",
            "email": "ozan.sazak@gmail.com"
        }
    },
    {
        "case": "   joHN doE  j D@  iEeE.met u.edu.      tr",
        "answer": {
            "name": "John",
            "surname": "Doe",
            "email": "jd@ieee.metu.edu.tr"
        }
    },
    {
        "case": "     gOkSU KAVaL  gok suka val@ohyeah      . co m",
        "answer": {
            "name": "Goksu",
            "surname": "Kaval",
            "email": "goksukaval@ohyeah.com"
        }
    },
    {
        "case": "Thisisaveryverylongname andsurname whoami@example.com                                ",
        "answer": {
            "name": "Thisisaveryverylongname",
            "surname": "Andsurname",
            "email": "whoami@example.com"
        }
    }
]

if __name__ == "__main__":
    corrects = 0
    wrongs = 0
    
    for test_index, case in enumerate(tests):
        try:
            res = restructure_malformed_data(case["case"])
        except Exception as e:
            print(f"[!] Exception in test #{test_index}: {str(e)}")
            wrongs += 1
            continue

        if type(res) != dict:
            print(f"[!] In test #{test_index}: response is not dict")
            wrongs += 1
            continue

        if ("name" not in res) or (res["name"] != case["answer"]["name"]):
            print(f"[!] In test #{test_index}: name is wrong")
            wrongs += 1
            continue

        if ("surname" not in res) or (res["surname"] != case["answer"]["surname"]):
            print(f"[!] In test #{test_index}: surname is wrong")
            wrongs += 1
            continue

        if ("email" not in res) or (res["email"] != case["answer"]["email"]):
            print(f"[!] In test #{test_index}: email is wrong")
            wrongs += 1
            continue

        corrects += 1

    print("\n[+] Corrects: {corrects}, wrongs: {wrongs}")