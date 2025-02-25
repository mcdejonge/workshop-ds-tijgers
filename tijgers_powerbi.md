# Tijgers-workshop in PowerBI

0. Bekijk de inhoud van het Excel-bestand. Begrijp je wat er in elke kolom staat? Kun je al iets zeggen over het soort dieren dat door tijgers opgegeten wordt?
1. Importeer het Excel-bestand in PowerBI. TODO: iets preciezer uitleggen.
2. Maak een grafiekje van de verschillende prooidieren. Klik onder "Visualizations" op de knop "Stacked column chart".
3. Er verschijnt een nieuwe, lege grafiek. 
4. Klik op het pijltje naast "Brondata" rechts in het scherm, onder "Data". Er verschijnt een lijst met alle kolommen die je eerder al in het Excel-bestand hebt gezien.
5. We willen weten welke prooidieren het meest opgegeten worden door tijgers, dus selecteer de kolom "ProoiSoort" door het selectievakje te markeren.
6. Onder "Visualizations", onder "X-axis", staat nu dat de x-as van onze grafiek de verschillende soorten prooidieren gaat weergeven. Toch zien we nog niets. Dat komt omdat we nog niet hebben ingesteld wat er op de y-as moet worden weergegeven. Dat gaan we nu doen. Sleep "Prooisoort" onder "Brondata" naar het invoerveld onder "Y-axis".
7. Je grafiek toont ineens alle prooidieren. De Y-as geeft het aantal van elk type prooidier weer ("Count of Prooisoort"). De grafiek is gesorteerd van de prooidieren die het meest opgegeten worden naar het prooidier dat het minst wordt opgegeten. We kunnen nu zien of dorpelingen gelijk hebben als ze denken dat hun tijgers vooral koeien eten.
8. Het kan zijn, dat tijgers alleen in sommige dorpen koeien eten en in andere niet. Om hier achter te komen moeten we een zg. "Slicer" toevoegen waarmee we alleen de gegevens voor één of meer dorpen kunnen bekijken. Klik onder "Visualizations" op de knop "Slicer" (een rechthoek met een trechtertje). Er verschijnt een nieuw, leeg onderdeel in het hoofdvenster links.
9. Sleep de kolom "Dorp" onder "Brondata" rechts in het scherm naar het nieuwe lege onderdeel. Er verschijnt een lijst met namen van dorpen met naast elke dorpsnaam een selectievakje. Wanneer je zo'n selectievakje markeert, krijg je de gegevens te zien voor dat dorp.
10. Klik rond in de slicer die je zojuist hebt aangemaakt om te kijken of het tijgers in verschillende dorpen een verschillend dieet hebben. Kijk bijvoorbeeld eens wat tijgers in het dorp Bhadar eten en vergelijk dat met wat er in het dorp Tara gebeurt.