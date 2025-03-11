# Tijgers-workshop in PowerBI

## Voorbereiding

1. Bekijk de inhoud van het Excel-bestand. Begrijp je wat er in elke kolom staat? Kun je al iets zeggen over het soort dieren dat door tijgers opgegeten wordt?
2. Importeer het Excel-bestand in PowerBI. TODO: iets preciezer uitleggen.

## De eerste grafiek: prooidieren per soort

1. Maak een grafiekje van de verschillende prooidieren. Klik onder "Visualizations" op de knop "Stacked column chart".
2. Er verschijnt een nieuwe, lege grafiek. 
3. Klik op het pijltje naast "Brondata" rechts in het scherm, onder "Data". Er verschijnt een lijst met alle kolommen die je eerder al in het Excel-bestand hebt gezien.
4. We willen weten welke prooidieren het meest opgegeten worden door tijgers, dus selecteer de kolom "ProoiSoort" door het selectievakje te markeren.
5. Onder "Visualizations", onder "X-axis", staat nu dat de x-as van onze grafiek de verschillende soorten prooidieren gaat weergeven. Toch zien we nog niets. Dat komt omdat we nog niet hebben ingesteld wat er op de y-as moet worden weergegeven. Dat gaan we nu doen. Sleep "Prooisoort" onder "Brondata" naar het invoerveld onder "Y-axis".
6. Je grafiek toont ineens alle prooidieren. De Y-as geeft het aantal van elk type prooidier weer ("Count of Prooisoort"). De grafiek is gesorteerd van de prooidieren die het meest opgegeten worden naar het prooidier dat het minst wordt opgegeten. We kunnen nu zien of dorpelingen gelijk hebben als ze denken dat hun tijgers vooral koeien eten.
7. Het kan zijn, dat tijgers alleen in sommige dorpen koeien eten en in andere niet. Om hier achter te komen moeten we een zg. "Slicer" toevoegen waarmee we alleen de gegevens voor één of meer dorpen kunnen bekijken. Klik onder "Visualizations" op de knop "Slicer" (een rechthoek met een trechtertje). Er verschijnt een nieuw, leeg onderdeel in het hoofdvenster links.
8. Sleep de kolom "Dorp" onder "Brondata" rechts in het scherm naar het nieuwe lege onderdeel. Er verschijnt een lijst met namen van dorpen met naast elke dorpsnaam een selectievakje. Wanneer je zo'n selectievakje markeert, krijg je de gegevens te zien voor dat dorp.
9. Klik rond in de slicer die je zojuist hebt aangemaakt om te kijken of het tijgers in verschillende dorpen een verschillend dieet hebben. Kijk bijvoorbeeld eens wat tijgers in het dorp Bhadar eten en vergelijk dat met wat er in het dorp Tara gebeurt.

## De tweede grafiek: prooidieren per maand

1. Maak een nieuw tabblad door op het plusje in de tabbalk (onderin) te klikken. Er verschijnt een nieuwe, lege grafiek.
2. Selecteer opnieuw het visualisatietype "Stacked Bar Chart" door op het desbetreffende knopje te klikken onder "Visualizations". 
3. Klik op het pijltje naast "Brondata". **Sleep** de kolom "Maand" naar het veld "X-axis". Dit zorgt ervoor dat de maanden op de X-as getoond worden.
3. Op de Y-as willen we de aantallen prooien weergeven. Sleep de kolom "ProoiSoort" naar het veld "Y-axis". Er verschijnt nu een staafgrafiek met voor elke maand het aantal prooien dat opgegeten is. Merk op dat onder Y-axis nu staat "Count of ProoiSoort": het aantal waarden in de kolom ProoiSoort voor elke maand. Dat is precies wat we willen hebben. Dit doet PowerBI automatisch.
4. We weten nu dat tijgers niet elke maand hetzelfde aantal prooidieren opeten, maar misschien kunnen we meer ontdekken door weer te geven *welke* prooidieren er elke maand opgegeten worden. Hiervoor gebruiken we de zogenoemde "legend". Sleep de kolom "ProoiSoort" naar het veld "Legend" onder "Y-axis". Als het goed is, zie je dat elke staaf in het staafdiagram nu kleurtjes krijgt voor elke diersoort. Valt je iets op? [in juni en juli worden er minder koeien opgegeten].

## De derde grafiek: mannetjes en vrouwtjes

Tijgers leven in hun eentje. Alleen de vrouwtjestijgers voeden welpjes op. Mannetjestijgers zwerven in hun eentje door het bos. We vragen ons af of het verschil in leefwijze tussen mannetjestijgers en vrouwtjestijgers gevolgen heeft voor het aantal koeien dat ze eten (oftewel: moeten dorpelingen banger zijn als er een mannetjestijger in de buurt rondzwerft dan wanneer er een vrouwtjestijger, al dan niet met welpen in de buurt is).

Om hier achter te komen maken we een nieuwe "Stacked Bar Chart" (op een nieuw tabblad is wel zo netjes). Vervolgens:

1. Sleep de kolom "ProoiSoort" naar de X-as en ook naar de Y-as waar hij "Count of ProoiSoort" wordt: voor elke prooisoort het aantal dat ervan opgegeten is.
2. Net als bij de tweede grafiek gebruiken we de "Legend" om verschillen *binnen* de staven weer te geven. Deze keer slepen we de kolom "TijgerGeslacht" naar het veld "Legend". Wat zien we? [Vrouwtjestijgers maken meer slachtoffers dan mannetjestijgers maar bij koeien is het verschil 50/50].
3. Waarschijnlijk is het interessant om te weten hoeveel mannetjestijgers en vrouwtjestijgers er eigenlijk *zijn*. Dit is één van de weinige gevallen waarin het grafiektype "Pie chart" (taartdiagram) nuttig is. Sleep een "Pie chart" naar het tabblad en sleep de kolom "TijgerGeslacht" **zowel** naar het veld "Legend" als naar het veld "Values" (waar het "Count of TijgerGeslacht" wordt). Wat valt op? [er zijn veel meer vrouwtjestijgers dan mannetjestijgers, dus mannetjes eten disproportioneel meer koeien oftwel het antwoord op de vraag is: ja].

## Even samenvatten. Wat weten we nu?

- Iets minder dan de helft van de prooidieren van tijgers zijn koeien.
- In juni en juli worden er minder koeien opgegeten dan in de overige maanden.
- Mannetjestijgers pakken vaker een koe dan vrouwtjestijgers.

Met andere woorden: als dorpelingen klagen dat hun koeien gevaar lopen, hebben ze wel een beetje gelijk. Wat zouden ze kunnen doen om hun koeien te beschermen?

## De computer laten rekenen

Eén van de dingen die je zou kunnen doen om te voorkomen dat een tijger je koe opeet, is ervoor zorgen dat de koe niet te ver van huis gaat en zo het gevaar loopt een tijger tegen te komen.

Om te kunnen bepalen of dat zou helpen, moeten we eerst weten of koeien verder van huis meer gevaar lopen dan dichtbij. Hiervoor gaan we kijken hoeveel koeien er binnen 2 kilometer van hun dorp worden opgegeten en hoeveel erbuiten.

1. Om dit te kunnen vaststellen, hebben we een nieuw soort grafiek nodig: de "100% stacked colum chart". In deze grafiek zijn alle staven even lang. Met je "Legend" kun je vervolgens voor elke staaf de verhouding zien. Maak een nieuw tabblad en sleep daar een "100% stacked column chart" naartoe. Op de X-as zet je de kolom "Maand" en op de Y-as ook ("Count of Maand"). Vervolgens sleep je de kolom "Binnen2KmVanDorp" naar het veld "Legend".
2. Het lijkt er inderdaad op alsof de meeste aanvallen verder dan 2 kilometer van een dorp plaatsvinden. Maar wacht: hier zit een addertje onder het gras. Welke? [zonder filter zijn dit de aantallen voor *alle* prooien. Laat de deelnemers een "Slicer" toevoegen voor de kolom ProoiSoort en vervolgens alleen de waarden selecteren voor koeien]
3. Het lijkt er ook op alsof aanvallen dichter dan 2 kilometer van het dorp in bepaalde maanden van het jaar [juli tm november] vaker voorkomen dan in andere maanden, maar **hoeveel** vaker dat is, is met een grafiek moeilijk te zeggen. Laten we de computer inschakelen om ons te helpen.
4. Maak een nieuw tabblad en sleep daar het visualisatietype "Key influencers" naartoe. Een "key influencer" is een visualisatie waarbij de computer zelf gaat uitrekenen wat de invloed is van de ene kolom op de waarde van een andere.
5. Een "Key influencer" heeft een **doel**kolom en één of meer kolommen die deze doelkolom beïnvloeden. Sleep de kolom "Binnen2KmVanDorp" naar het veld "Analyze". Dit is onze doelkolom.
6. Sleep de kolom "Maand" naar het veld "Explain by". "Explain by" ("leg uit volgens") is de kolom die de waarde in de doelkolom helpt verklaren. **Let op** standaard wordt deze kolom omgezet in "Sum of Maand"(som van maand, wat natuurlijk onzin is). Klik op het pijltje naar beneden naast "Sum of Maand" en kies de optie "Don't summarize" (niet samenvatten) uit het menu dat verschijnt.
7. Zodra je de kolom "Maand" naar het veld "Explain by" hebt gesleept, gaat de computer rekenen. Dat kan even duren. Als hij klaar is zie je dat er inderdaad maanden zijn waarin tijgers vaker binnen een straal van 2 kilometer van een dorp een prooi aanvallen. Als de maand groter is dan 6, is de kans hierop 1,9x zo groot.

Wie wil, kan deze analyse verfijnen. Om te beginnen zou je een slicer moeten toevoegen zodat we het cijfer alleen voor koeien kunnen berekeken. Verder is het interessant om eens te kijken waarom de kans op een aanval binnen 2 kilometer van een dorp groter is in maanden groter dan 6. Hiervoor kun je de kolom "Maand" vervangen door de kolom "Seizoen". Wat blijkt? Tijgers vallen dichter bij dorpen aan tijdens het regenseizoen dan tijdens de andere seizoenen.

Je kunt ook extra slicers toevoegen. Is er bijvoorbeeld verschil tussen mannetjes en vrouwtjes [bij mannetjes springt de kans op een aanval dicht bij het dorp naar iets meer dan 2 tijdens het regenseizoen]?

## Conclusie

Dankzij ons dataspeurwerk kunnen we een advies formuleren aan de dorpelingen:

1. Zorg ervoor dat je koeien niet verder dan 2 kilometer buiten het dorp grazen.
2. Overweeg om koeien in de regentijd binnen te houden of op een andere manier extra te beschermen.
3. Kijk in het bijzonder uit als er een mannetjestijger is gesignaleerd in de buurt van het dorp.

Wanneer dorpelingen deze adviezen opvolgen, is de kans groter dat hun vee niet wordt opgegeten door een tijger.
