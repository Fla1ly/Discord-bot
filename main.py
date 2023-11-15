from time import sleep

meme_dict = {
        "CRINGE": "Coś wyjątkowo dziwnego lub zawstydzającego",
        "LOL": "Częsta reakcja na coś zabawnego",
        "BRB": "Be Right Back - Wrócę zaraz",
        "IRL": "In Real Life - W rzeczywistości",
        "SMH": "Shaking My Head - Kręcę głową ze zdziwienia",
        "YOLO": "You Only Live Once - Żyjesz tylko raz",
        "FOMO": "Fear Of Missing Out - Strach przed przegapianiem",
        "TFW": "That Feeling When - To uczucie, gdy",
        "ICYMI": "In Case You Missed It - W razie, gdy tego nie zauważyłeś",
        "BTW": "By The Way - Przy okazji",
        "OOTD": "Outfit Of The Day - Strój dnia",
        "NSFW": "Not Safe For Work - Niebezpieczne dla pracy (zawiera treści dla dorosłych)",
}

print("Witam do aplikacji slownika dla slow wspolczesnych")
sleep(5)

start = input("Czy chcesz użyć aplikacji? Wpisz 'tak', aby uruchomić program, albo 'nie', aby wyjść: ")

if start == "tak":
    word = input("Wpisz słowo, którego nie rozumiesz (używaj wielkich liter!): ")
elif start == "nie":
    print("See you next time!")
    sleep(2)
    exit()  
else:
    print("?")

if word in meme_dict.keys():
    print(meme_dict[word])
    sleep(5)
    print("Czy chesz zakonczyc program, czy nauczyc sie wieciej slow?")
    sleep(5)
    cont = input("Wpisz 'nauczyc', zeby nauczyc sie wieciej slow, albo 'zakoncz', zeby zakonczyc program.")
else:
    print("Nie znaleziono slowa")
    
if cont == "nauczyc":
        word = input("Wpisz słowo, którego nie rozumiesz (używaj wielkich liter!): ")
elif cont == "zakoncz":
        print("See you next time!")
        sleep(2)
        exit()
else:
    print("?")
    
    #Kod nie dziala tak jak bym chcial, ale jakos jest ok.
        
