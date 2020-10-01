# Lösenordsfras

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
