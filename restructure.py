#Rector of METU, The Great V, suddenly decided to open all departments for
#physical education and allowed us to proceed the traditional 'Topluluk
#Tanitimlari'. After this we, IEEE METU, have decided to use an OCR system to
#read the name, surname and email info of new participants of our
#community after this 'Topluluk Tanitimlari'.

#However, our OCR system failed and malformed some of those data. Now we need
#you to re-structure this malformed data and output in JSON format.

#Example 1:
# Malformed data: "oZan    SAzaK  ozan. sazA K@  gma il. Com"
# Re-structured : "Ozan Sazak ozan.sazak@gmail.com"
# JSON format   : {"name": "Ozan", "surname": "Sazak", "email": "ozan.sazak@gmail.com"}

#Example 2:
# Malformed data: "   joHN doE  j D@  iEeE.met u.edu.      tr"
# Re-structured : "John Doe jd@ieee.metu.edu.tr"
# JSON format   : {"name": "John", "surname": "Doe", "email": "jd@ieee.metu.edu.tr"}

# Specifications
# - The true data format is: "NAME SURNAME EMAIL" with one space between each other
# - Names and surnames are all first-letter uppercase and all other letters lowecase
# - Emails are always lowercase
# There may be extra spaces between names, surname and email
# - The function takes a strng which is malformed data, and returns the a dict including "name", "surname" and "email" keys

# There are some little tests for you to test your code in test.py
# Run it via bash: python3 test.py
def restructure_malformed_data(mdata: str) -> dict:
    # Code here.
    pass