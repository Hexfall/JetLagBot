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
        "Få en and til at grine",
        """Kommikeren Anders "Anden" Matthesen voksede op i Albertslund. I hans ånd, find en and og fortæl den en joke.""",
    ),
)
ballerup = State(
    4,
    "Ballerup",
    challenge=Challenge(
        "Støt Socialdemokratiet",
        """Ballerup kommune har været socialdemokratisk ledet siden 1933. Vis din støtte til partiet ved at finde 24 forskellige røde roser, en rose per kommunalvalg.
Afbildninger af roser tæller, men en bukket af roser tæller kun for én enkelt.""",
    ),
)
broendby = State(
    5,
    "Brøndby",
    challenge=Challenge(
        "Hader FCK",
        """Jeg hører at Brøndby ikke er kæmpe fan af deres rivaler FCK.
Tag et billede af grafiti, klistermærker eller tags med budskaber i retning af "Fuck FCK", "Hader FCK" på 6 af disse 8 steder:
- Lygtepæle
- Elskabe/teknikskabe
- Skilte (fx vejskilte eller informationsskilte)
- Busstoppesteder
- Broer/tunneller.
- Mure og plankeværker.
- Affaldsspande
- Døren til eller inde på et offentligt toilet.""",
    ),
)
dragoer = State(
    6,
    "Dragør",
    challenge=Challenge(
        "Vis jeres had til Kastrup lufthavn",
        """Dragør kommune har en masse flotte stille villakvarterer med den lille bagatel at kommunen ligger lige op ad Kastrup lufthavn, hvilket giver noget støj.
Støt de lokale beboere ved at vise jeres had til lufthavnen! 
Et gruppemedlem skal stå mindst 3 meter fra en offentlig skraldespand og kaste et papirfly ned i skraldespanden.
Hvis I misser, så må I vente 30 sekunder hvor I kan skamme jer over at metalfuglene får lov til at blive ved med at støje""",
    ),
)
gentofte = State(
    7,
    "Gentofte",
    challenge=Challenge(
        "Estimer Boligpriser",
        """Gentofte er den dyreste kommune at købe villa per kvadratmeter i. 
Find to huse til salg, og gæt hvilket hus er dyrest. Hvis i gætter forkert, så er udfordringen automatisk vetoed.""",
    ),
)
gladsaxe = State(
    8,
    "Gladsaxe",
    challenge=Challenge(
        "Sten, Gladsaxe, Papir",
        """Find sakse til salg i Gladsaxe og spil et spil sten, saks, papir (ikke sten, papir, saks 😠). 
I skal beslutte jer hvem kommer til at vinde inden i går i gang, og skal spille indtil den person vinder, med 5 minutter mellem runder.
Det er, selvfølgelig, forbudt at snakke omkring spillet inden spillet, eller mellem runder.""",
    ),
)
glostrup = State(
    9,
    "Glostrup",
    challenge=Challenge(
        "Tårn jer over det gamle vandtårn",
        """Glostrup er kendt for deres gamle vandtårn fra 1897. Tårnet er 33.5 meter højt... men er det ikke lidt lavt? Det kan i vel gøre bedre.
Løft vand en samlet højde af 33.5 meter eller højere. Vandet behøver ikke blive løftet hele distancen på en gang, men hver løft skal være minimum 3 meter.""",
    ),
)
herlev = State(
    10,
    "Herlev",
    challenge=Challenge(
        "Ha' det herligt i Herlev",
        """Herlev savner at folk ikke leger meget længere. Opmundre Herlev ved at:
- Spil gæt og grimasser 3 gange hver med valgfrie filmtitler. (No colluding!)
- Spil ""Catch"" med en valgfri genstand over 10 meters distance med 5 gennemførte grib i streg.
- Lav, op hop en hinkesti på minimum 10 hink. (En hvid-ish sten kan som reglt bruges some make-shift kridt)""",
    ),
)
hvidovre = State(
    11,
    "Hvidovre",
    challenge=Challenge(
        "Er hvid ovre i Hvidovre?",
        """Hvid er så ovre. Men måske er det ikke i Hvidovre.
Gå 500m væk fra nogen togstationer, for at finde de lokale. 
Lokaliser 3 personer som kun går helt i hvidt tøj eller alt pånær en artikkel af tøj er hvidt. 
Vis Danmark at hvid stadig er 'en vogue'""",
    ),
)
hoeje_taastrup = State(
    12,
    "Høje-Taastrup",
    challenge=Challenge(
        "Ludo Vaner til Ludomaner",
        """Høje Taastrup kommune er hjem til en af Danmarks mest bekendte brætspil spillere: Simon Breum.
Men fleste brætspil tager jo alt for lang tid og er alt for kedelige! Kan vi ikke bare spille noget simpelt istedetfor?

Lav et spil Ludo ud af sten, planter, affald, et spil Ludo, eller andre ting som i kan finde.
Herefter, spil en omgang Ludo imod hinanden, hvor hver spiller har kun en enkelt brik som de skal få i mål.

Spillet må ikke laves af ting som i bringer med ind i kommunen, dog i må genre bruge jeres egne terninge til at rulle med.
""Slutbanerne"" skal være anderledes og genkendelige fra ""rundbanen,"" og spillebrikkerne skal være genkendelige fra hinanden og selve spillet. I er ikke nødt til at lave startfelt eller hjemmezone.
En brik er i mål når den lander på det inderste felt i dens slutbane. Hvis i roller over, så ""hopper den tilbage.""
Udfordringen er færdig når den første person får deres brik i mål. Taberen må oplyse det andet hold med at sige til hvor dårlige de er til brætspil.""",
    ),
)
ishoej = State(
    13,
    "Ishøj",
    challenge=Challenge(
        "No Kommune for Old Men",
        """Ishøj kommune har en den korteste forventede middel levealdre i Danmark af de kommuner vi har i spil. 
It truly is no ~~country~~ kommune for old men. Channel your inner cowboy and duel to the death.
I skal finde 2 genstande i kommunen i vil kaste og i skal finde en græsplæne hvor i kan stå ryg til ryg. 
I skal derefter gå 5 lange skridt frem, vende jer om og med det samme kaste genstanden på jeres fjende.
Som i et rigtig duel skal i samtidig sige, 1... 2... 3... 4... 5... skyd!
Hvis i begge dør (rammer hinaden), så har i hjulpet Ishøj med at holde middellevealderen nede og i har vundet kommunens kærlighed.
Hvis i ikke begge bliver ramt eller i ikke skyder (stort set) samtidig, så skal i vente 5 minnuter før i kan duallere igen.""",
    ),
)
lyngby_taarbaek = State(
    14,
    "Lyngby-Taarbæk",
    challenge=Challenge(
        "__K__an I __K__ortlægge __K__-vitamins __K__ilder?",
        """DTU har mange kendte alumnier, deriblandt Henrik Dam som opdagede K-vitamin i 1943. 
Støt op om hans opdagelse ved at finde 11 af de her 16 forskellige kilder til K-vitamin:
- Grønkål
- Spinat
- Majroe
- Broccoli
- Kiwi
- Blåbær
- Hasselnød
- Vindrue
- Tomat
- Olivenolie
- Zucchini
- Mango
- Pære
- Kartoffel
- Sød kartoffel
- Brød""",
    ),
)
roedovre = State(
    15,
    "Rødovre",
    challenge=Challenge(
        "Tjek op på lokal buttikkerne",
        """Rødovre har Danmarks første rigtige indendørs shoppingcenter i ""Rødovre Centrum"" som åbnede i 1966.
Siden da har de små butikker selvfølgelig haft det svært. Så det ville være rart hvis i kunne tjekke op på om der stadig er gang i dem!
Observer 20 mennesker gå ind i en ""uafhængig butik"" (Ikke kæde-butik). I må ikke tælle jer selv som at gå ind i buttiken.""",
    ),
)
taarnby = State(
    16,
    "Tårnby",
    challenge=Challenge(
        "Hjælp Tårnby med at leve op til navnet",
        """Tårnby er selvbevidst omkring de ikke har mange tårne. Byg et stentårn som går over begge holdkameraters knæ.
Tårnby har ikke pengene til at give dig ordentlige materialler, så i skal selv finde alle sten i kommunen og i må ikke bruge sten som er åbentlyst menneskeskabte ""fx Mursten""""",
    ),
)
vallensbaek = State(
    17,
    "Vallensbæk",
    challenge=Challenge(
        "Short-king Vallensbæk",
        """Vallensbæk kommune er Danmarks næst-mindste og den er utrolig smal. Det ikke nogen stor sag et gå fra ende til ende. Men det behøver i ikke fortælle vallensbæk.
Gå øst til vest fra grænsen til brøndby kommune, til grænsen af ishøj/høje-taastrup kommune. Eller omvendt vest til øst.
I har ikke travlt, så i må ikke løbe eller tage nogen form for offentlig transport. 
Når i er gået ende til ende skal i fortælle vallensbæk kommune ""Woow du er *så* stor""""",
    ),
)
alleroed = State(
    18,
    "Allerød",
    challenge=Challenge(
        "Hanna er Sulten",
        """Hanna Halerød er trolden som kan findes i Allerøds skove. Men at beskytte Allerøds skove er sultent arbejde og Hanna er Huuungy!
Trolde spiser sten og mineraler (og baby geder??), så find minimum 30 sten som er større end 3cm, og placer dem i et hjerte form i en af Allerøds kommunes skove. 
Skriv derefter ""Hanna"" med vilkårlige sten i midten er hjertet så Hanna ved det er til hende.""",
    ),
)
egedal = State(
    19,
    "Egedal",
    challenge=Challenge(
        "Start en ny navnestrid",
        """Egedal kommune har haft mange problemer med deres navn. Egedal hed ""Kongsdal"" indtil trussel om sagsanlæg. Navnet ""Egedal"" blev derefter valgt på trods af endnu en trussel om sagsanlæg. 
Find to personer med det samme navn (fornavn eller efternavn). Vælg hvem der repræsenterer kommunen og hvem der repræsenterer privatpersonerne og derefter slå plat og krone to gange i træk, om hvem der må beholde deres navn. Først skal privatpersonen vinde og derefter skal kommunen vinde. """,
    ),
)
fredensborg = State(
    20,
    "Fredensborg",
    challenge=Challenge(
        "Ødelæg freden i Fredensborg",
        """Find et sted enten på stranden eller i en skov, hvor man i 60 sekunder ikke kan høre et bil eller menneske, men bare naturens lyde...
Efter 60 sekunder stilhed skal i begge råbe det første chat-GPT foreslår i skal råbe når du giver den denne promt:
""giv mig en meget uhøfelig ting at råbe på en meget stille strand""/""giv mig en meget uhøfelig ting at råbe i en meget stille skov""""",
    ),
)
frederikssund = State(
    21,
    "Frederikssund",
    challenge=Challenge(
        "Afkod vikingrunerne",
        """Frederikssund kommune er verdenskendt for sit fantastiske årlige vikingespil og vikingske efterladenskaber, der tiltrækker folk fra alle verdenshjørner.
For at bringe vikingetiden tilbage, skal den ene i gruppen nu med sin krop vælge et 4-bogstavs dansk ord og stave det i det yngre futhark-alfabet og bagefter vise 4 billeder af hvert tegn til den anden!
Hvis de ikke gætter ordet, må I skamme jer i 5 minutter over at jeres vikingeblod svigtede jer før I prøver igen med et nyt ord.""",
    ),
)
furesoe = State(
    22,
    "Furesø",
    challenge=Challenge(
        "Gør Furesø til \"Sure-sø\"",
        """Furesø har haft det for godt for længe! Tag til Furesø eller en af Furesøs venner,
Sønderssø og Farum sø, og slå søen fysisk med din knytnæve. That'll show em'""",
    ),
)
gribskov = State(
    23,
    "Gribskov",
    challenge=Challenge(
        "Plant et træ, hvis skygge i aldrig vil sidde i.",
        """Det bedste tidspunkt at plante et træ var 30 år siden, det næstbedste tidspunkt er lige nu. Altså *nu* nu.
Find og grav et ""træ-frø"" 10cm ned i jorden (agern, kogle eller lign.) og dæk det med jord igen.
I må kun bruge jeres hænder eller grene/pinde/sten i finder på jorden som skovle.""",
    ),
)
halsnaes = State(
    24,
    "Halsnæs",
    challenge=Challenge(
        "Identitetspolitik",
        """*Halsnæs Kommune* ændrede deres navn i 2008, væk fra *Frederiksværk-Hundested* Kommune.
Der er dog stadig mennesker som nægter at give slip på det gamle navn og respektere Halsnæs' nye identitet [mangler kilde].
Find en offentlig bygning og lav en video på minimum 1 minut hvor du beskytter Halsnæs' nye navn, og forklarer hvorfor det burde respekteres.
Send derefter denne video til det andet hold og skæld dem ud for deres gammeldags mentalitet.""",
    ),
)
helsingoer = State(
    25,
    "Helsingør",
    challenge=Challenge(
        "Genindfør Øresundstolden",
        """Find et sted hvor i kan se over til Sverige(Yuck), og vælg et betemt punkt på den Svenske kyst.
Hvert skib som sejler mellem jer og det valgte punkt skal nu betale en told!
privatskibe betaler 5 kroner, kommercielskibe betaler 10 kroner.
Når nok skibe er sejlet gennem sundet til at statskassen er blevet 200 kr. rigere, så kan i holde fyraften!""",
    ),
)
hilleroed = State(
    26,
    "Hillerød",
    challenge=Challenge(
        "Hjælp Region H med nyt supersygehus",
        """Det nye flotte supersygehus i Hillerød er uheldigvis blevet ramt af forsinkelser og gået over budget, så nu skal I vise Hillerød hvordan man bygger et sygehus.
I skal først finde et fladt stykke jord at bygge på, hvorefter I får 10 minutter til at samle naturmaterialer (pinde, kogler, sten osv.) og bygge et sygehus med dem.
Derefter skal I tage et billede ovenfra af jeres byggeri som I kan være stolte af. Byggeriet skal mindst have:
- Et tydeligt H (som selvfølgelig står for Hillerød)
- 3 separate aflukkede rum, hvoraf 1 har en åbning i sig (til ambulancerne)
- En helipad, dvs. en cirkel/cirkulært objekt
Hvis I ikke når det inden for tiden, må I gå mindst 100 meter væk og starte forfra efter 10 minutters tænkepause til at overveje hvordan I forklarer denne forsinkelse til kommunen
""",
    ),
)
hoersholm = State(
    27,
    "Hørsholm",
    challenge=Challenge(
        "Hør om en ny holm i Hørsholm",
        """En holm er en lille ubeboet ø, og Hørsholm har brug for en ny.
Find en vandmasse (sø, å, vandpyt) og skab en ny holm med minimum en plante. Fortæl så hinanden om den nye holm.""",
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
        "Erklær jeg som den retmæssige greve.",
        """Greve blev lovet til dine forfædre for 4000 år siden, det er tid til at genvinde det!
Lav en krone af græs, hø og minimum 3 forskellige blomster og overgiv den til en holdkamerat for at Erklære dem som den retsmæssige greve af Greve.
Hvis den retsmæssige greve kan gå med kronen i 3 minutter uden den falder af hovedet eller fra hinaden, så har i vundet greve tilbage!
Kronen skal være minimum 10 centimeter i diameter, og må ikke bindes fast på nogen måde til håret/hovedet. Den skal bare kunne sidde på hovedet.""",
    ),
)
solroed = State(
    30,
    "Solrød",
    challenge=Challenge(
        "Hemmeligheden bag solrøds navn.",
        """Solrød er et anagram for ""ordløs"", hvilket giver meget bedre mening da solen faktisk ikke er rød!
Så ehrm hjælp Solrød med at finde et ord.
I skal finde et tilfædigt 10 bogstaver langt ord ved at google ""giv mig et tilfældigt 10 bogstaver langt ord"".
I skal derefter finde bogstaverne til jeres ord rundt i byen på skilte bygninger eller ligende. Det skal altså være perminent skrift, ikke en avis i fandt på jorden.
I må kun bruge et bogstav pr bygning/skilt/lignende. Når i kan danne ordet med bogstaver i har fudnet har i gjort solrød til ordrig :)""",
    ),
)
koege = State(
    31,
    "Køge",
    challenge=Challenge(
        "Hyldest til Suzuki-Torben",
        """Køge er bl.a. kendt for sine hæderlige politikere og deres meget lovlydige venner, bl.a. Suzuki-Torben. 
For at vise Køge-egnets kærlighed til Suzuki-biler skal I derfor nu tage 3 billeder med et gruppemedlems overraskede ansigt ved siden af en Suzuki-biler (ikke fra bilforhandler, dvs. med reelle nummerplader) i det offentlige rum, for at vise hvor imponerede I er over de flotte biler.""",
    ),
)
roskilde = State(
    32,
    "Roskilde",
    challenge=Challenge(
        "Become *the* Rap God",
        """Roskilde lægger plads til Danmarks største live-musik festival, og Eminems optræden på Orange Scene i 2018 var festivalens største med mere end 100.000 i publikum. I skal nu overgå hans koncert.
Vælg tilfældigt en af Eminems mest lyttede-til sange på Spotify. Lær og udfør et tilfældigt vers plus omkvædet.""",
    ),
)
lejre = State(
    33,
    "Lejre",
    challenge=Challenge(
        "Vi kigger på fugle 🎵",
        """Én fugl i hånden er bedre end ti på taget. Men vi tager hvad vi kan få.
Enten rør en fugl eller fotografer 10 fugle på tag.""",
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
