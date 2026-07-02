from json import dump
from sqlite3 import LEGACY_TRANSACTION_CONTROL

from Classes.Challenge import Challenge
from Classes.State import State
from Models.StateModel import StateModel

koebenhavn = State(
    1,
    "København",
    challenge=Challenge(
"Købhavne i København",
"""København kom først til prominens som en købstad, grundet dens strategiske lokation og naturlige havne. Byen er derfor fyldt med havne og brygger.
Besøg mindst X af følgende områder, og tag billed af jer ved siden af havet:
- Nordhavn
- Søndre Frihavn
- Inderhavnen
- Nyhavn
- Christianshavn
- Islandsbrygge
- Havneholmen
- Enghave Brygge
- Sydhavn (vandet lige nord for sluseholmen er ikke med)
Se grænser på billed til højre

X er lige ved 5 +/- forskellen mellem holdenes claimede kommuner (ikke nødvendigvis forbundte) (desto længere bagud i er, desto nemmere). I skal besøge i hvert fald en lokation på hver side af vandet.
X sidder fast efter i tager jeres første billed, ie hvis modstanderholdet klarer en udfordring imens I er i gang med denne, så bliver den ikke nemmere.""",
    ),
)
frederiksberg = State(
    2,
    "Frederiksberg",
    challenge=Challenge(
        "Dyrt at se dyr.",
"""Danmarks største zoologisk have er i Frederiksberg, men det såååå dyrt!
Hvorfor ville man betale for at se dyr, når der er dyr over det hele?
Tag et billede af 10 forskellige dyre arter. (Hvis i har snoozed biologi, så er arter dem som kan lave (fungerende)børn sammen. Så hunde er alle den samme art. due og krave er 2 forskellige arter)
Ingen af dyrerne må være fra zoologisk have. Mennesker er *ikke* dyr.""",
    ),
)
albertslund = State(
    3,
    "Albertslund",
    challenge=Challenge(
        "",
        """""",
    ),
)
ballerup = State(
    4,
    "Ballerup",
    challenge=Challenge(
        "",
        """""",
    ),
)
broendby = State(
    5,
    "Brøndby",
    challenge=Challenge(
        "",
        """""",
    ),
)
dragoer = State(
    6,
    "Dragør",
    challenge=Challenge(
        "",
        """""",
    ),
)
gentofte = State(
    7,
    "Gentofte",
    challenge=Challenge(
        "",
        """""",
    ),
)
gladsaxe = State(
    8,
    "Gladsaxe",
    challenge=Challenge(
        "",
        """""",
    ),
)
glostrup = State(
    9,
    "Glostrup",
    challenge=Challenge(
        "",
        """""",
    ),
)
herlev = State(
    10,
    "Herlev",
    challenge=Challenge(
        "",
        """""",
    ),
)
hvidovre = State(
    11,
    "Hvidovre",
    challenge=Challenge(
        "",
        """""",
    ),
)
hoeje_taastrup = State(
    12,
    "Høje-Taastrup",
    challenge=Challenge(
        "",
        """""",
    ),
)
ishoej = State(
    13,
    "Ishøj",
    challenge=Challenge(
        "",
        """""",
    ),
)
lyngby_taarbaek = State(
    14,
    "Lyngby-Taarbæk",
    challenge=Challenge(
        "",
        """""",
    ),
)
roedovre = State(
    15,
    "Rødovre",
    challenge=Challenge(
        "",
        """""",
    ),
)
taarnby = State(
    16,
    "Tårnby",
    challenge=Challenge(
        "",
        """""",
    ),
)
vallensbaek = State(
    17,
    "Vallensbæk",
    challenge=Challenge(
        "",
        """""",
    ),
)
alleroed = State(
    18,
    "Allerød",
    challenge=Challenge(
        "",
        """""",
    ),
)
egedal = State(
    19,
    "Egedal",
    challenge=Challenge(
        "",
        """""",
    ),
)
fredensborg = State(
    20,
    "Fredensborg",
    challenge=Challenge(
        "",
        """""",
    ),
)
frederikssund = State(
    21,
    "Frederikssund",
    challenge=Challenge(
        "",
        """""",
    ),
)
furesoe = State(
    22,
    "Furesø",
    challenge=Challenge(
        "",
        """""",
    ),
)
gribskov = State(
    23,
    "Gribskov",
    challenge=Challenge(
        "",
        """""",
    ),
)
halsnaes = State(
    24,
    "Halsnæs",
    challenge=Challenge(
        "",
        """""",
    ),
)
helsingoer = State(
    25,
    "Helsingør",
    challenge=Challenge(
        "",
        """""",
    ),
)
hilleroed = State(
    26,
    "Hillerød",
    challenge=Challenge(
        "",
        """""",
    ),
)
hoersholm = State(
    27,
    "Hørsholm",
    challenge=Challenge(
        "",
        """""",
    ),
)
rudersdal = State(
    28,
    "Rudersdal",
    challenge=Challenge(
        "",
        """""",
    ),
)
greve = State(
    29,
    "Greve",
    challenge=Challenge(
        "",
        """""",
    ),
)
solroed = State(
    30,
    "Solrød",
    challenge=Challenge(
        "",
        """""",
    ),
)
koege = State(
    31,
    "Køge",
    challenge=Challenge(
        "",
        """""",
    ),
)
roskilde = State(
    32,
    "Roskilde",
    challenge=Challenge(
        "",
        """""",
    ),
)
lejre = State(
    33,
    "Lejre",
    challenge=Challenge(
        "",
        """""",
    ),
)

# Edges
edges: list[tuple[State, State]] = [
    (koebenhavn, frederiksberg),
    (koebenhavn, taarnby),
    (koebenhavn, hvidovre),
    (koebenhavn, roedovre),
    (koebenhavn, herlev),
    (koebenhavn, gladsaxe),
    (koebenhavn, gentofte),
    (taarnby, dragoer),
    (taarnby, hvidovre),
    (hvidovre, roedovre),
    (hvidovre, broendby),
    (broendby, roedovre),
    (broendby, glostrup),
    (broendby, vallensbaek),
    (broendby, albertslund),
    (roedovre, glostrup),
    (roedovre, herlev),
    (gentofte, gladsaxe),
    (gentofte, lyngby_taarbaek),
    (gladsaxe, lyngby_taarbaek),
    (gladsaxe, herlev),
    (gladsaxe, furesoe),
    (herlev, glostrup),
    (herlev, ballerup),
    (herlev, furesoe),
    (glostrup, albertslund),
    (glostrup, ballerup),
    (vallensbaek, ishoej),
    (vallensbaek, albertslund),
    (vallensbaek, hoeje_taastrup),
    (albertslund, hoeje_taastrup),
    (albertslund, egedal),
    (albertslund, ballerup),
    (ballerup, egedal),
    (ballerup, furesoe),
    (furesoe, lyngby_taarbaek),
    (furesoe, rudersdal),
    (furesoe, alleroed),
    (furesoe, egedal),
    (lyngby_taarbaek, rudersdal),
    (rudersdal, alleroed),
    (rudersdal, hoersholm),
    (ishoej, greve),
    (ishoej, hoeje_taastrup),
    (greve, solroed),
    (greve, roskilde),
    (greve, hoeje_taastrup),
    (solroed, koege),
    (solroed, roskilde),
    (koege, roskilde),
    (koege, lejre),
    (lejre, roskilde),
    (lejre, frederikssund),
    (roskilde, hoeje_taastrup),
    (roskilde, egedal),
    (roskilde, frederikssund),
    (hoeje_taastrup, egedal),
    (egedal, frederikssund, alleroed),
    (alleroed, frederikssund),
    (alleroed, hilleroed),
    (alleroed, fredensborg),
    (alleroed, hoersholm),
    (hoersholm, fredensborg),
    (frederikssund, hilleroed),
    (frederikssund, halsnaes),
    (hilleroed, halsnaes),
    (hilleroed, gribskov),
    (hilleroed, fredensborg),
    (fredensborg, gribskov),
    (fredensborg, helsingoer),
    (halsnaes, gribskov),
    (gribskov, helsingoer),
]

for edge in edges:
    edge[0].neighbors.append(edge[1].id)
    edge[1].neighbors.append(edge[0].id)

states = {v.id: v for v in [koebenhavn, frederiksberg, albertslund, ballerup, broendby, dragoer, gentofte, gladsaxe, glostrup, herlev, hvidovre, hoeje_taastrup, ishoej, lyngby_taarbaek, roedovre, taarnby, vallensbaek, alleroed, egedal, fredensborg, frederikssund, furesoe, gribskov, halsnaes, helsingoer, hilleroed, hoersholm, rudersdal, greve, solroed, koege, roskilde, lejre]}

for s in states.values():
    s.neighbors.sort()

#statelist = list(states.values())
#statelist.sort(key=lambda s: -len(s.neighbors))
#for s in statelist:
#    print(f"{s.name}: {len(s.neighbors)}")

if __name__ == "__main__":
    with open("Data/States.json", "w") as f:
        dump(
            states,
            default=lambda o: o.__dict__,
            sort_keys=True,
            indent=4,
            fp=f,
        )
    
    with StateModel() as sm:
        for state in states.values():
            print(state.name)
            for neighbor in state.neighbors:
                print(f"  - {sm.get_state(neighbor).name}")
        print(len(sm.states))
