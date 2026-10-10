bureliai = {
    "krepsinis": {
        "pavadinimas": "Krepsinis",
        "vadovas": "Jonas",
        "max_skaicius": 5,
        "dab_skaicius": 2
    },
    "futbolas": {
        "pavadinimas": "Futbolas",
        "vadovas": "Petras",
        "max_skaicius": 10,
        "dab_skaicius": 4
    },
    "tenisas": {
        "pavadinimas": "Tenisas",
        "vadovas": "Antanas",
        "max_skaicius": 3,
        "dab_skaicius": 1
    },
    "sachmatai": {
        "pavadinimas": "Sachmatai",
        "vadovas": "Zigmas",
        "max_skaicius": 2,
        "dab_skaicius": 0
    },
    "fotografija": {
        "pavadinimas": "Fotografija",
        "vadovas": "Rimas",
        "max_skaicius": 4,
        "dab_skaicius": 2
    }
}


def prideti_prie_burelio(vardas, burelis):
    if bureliai[burelis]["dab_skaicius"] < bureliai[burelis]["max_skaicius"]:
        bureliai[burelis]["dab_skaicius"] += 1
        print(f"Sveikiname {vardas}, jūs sėkmingai prisijungėte prie {bureliai[burelis]['pavadinimas']}!")
    else:
        print(f"Deja, {bureliai[burelis]['pavadinimas']} yra pilnas. Jūs negalite prisijungti.")


def pasalinti_is_burelio(vardas, burelis):
    if bureliai[burelis]["dab_skaicius"] > 0:
        bureliai[burelis]["dab_skaicius"] -= 1
        print(f"{vardas}, jūs sėkmingai atsijungėte nuo {bureliai[burelis]['pavadinimas']}!")
    else:
        print("Įvyko klaida. Būrelis neturi narių.")


print("Galimi būreliai:")
print("1. Krepšinis")
print("2. Futbolas")
print("3. Tenisas")
print("4. Šachmatai")
print("5. Fotografija")

burelis = int(input("Pasirinkite būrelį: "))
vardas = input("Įveskite savo vardą: ")

if burelis == 1:
    pasirinkimas = "krepsinis"
elif burelis == 2:
    pasirinkimas = "futbolas"
elif burelis == 3:
    pasirinkimas = "tenisas"
elif burelis == 4:
    pasirinkimas = "sachmatai"
elif burelis == 5:
    pasirinkimas = "fotografija"
else:
    pasirinkimas = None

if pasirinkimas is not None:
    prideti_prie_burelio(vardas, pasirinkimas)
    print(bureliai[pasirinkimas])
else:
    print("Tokio būrelio nėra.")