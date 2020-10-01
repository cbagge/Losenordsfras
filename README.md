# Lösenordsfras

## Vad

Genererar svenska lösenordsfraser från GU:s Saldo (https://spraakbanken.gu.se/resurser/saldo).

Strippar ordlistan från formatet

`abakus..1	räkna..1	PRIM..1	abakus..nn.1	abakus	nn	nn_3u_karbid`

till en js-lista

```
var wordlist = [
'abakus'
] 
```

Den tar även bort dubbletter och accenter samt ord längre än 10 och kortare än 3 tecken.

Resulteradnde ordlistan (från ungefär 120k poster till knappa hälften) funkar hyfsat att använda för att bygga lösenordsfraser med.

## Utveckling

Att bygga om så att man genererar ordlistor utifrån ordklass för att skapa lösenfraser som är enklare att komma ihåg. I nuläget får du X antal slumpade ord, men med ordlistor som är medvetna om ordklass kan du skapa lösenfraser av typen adjektiv + substantiv + verb + substantiv (exempelvis). Så istället för 

`ledbruten lustmord kaustika hälsoskäl`

får du exempelvis

`gul höna städar utefest`

vilket även har en språklig dimension som gör det lättare att komma ihåg. Det skulle sänka komplexiteten för lösenfraserna, men det skulle vara intressant att se med hur mycket/lite. Jag tror det skulle kunna vara en rimlig trade-off.

# English

Project generates a dictionary of swedish words suitable for building passphrases from. The basis i Gothenburg University's Saldo project (https://spraakbanken.gu.se/en/resources/saldo).
