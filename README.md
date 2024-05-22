[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/PwWMOy4Q)
# Domácí úkol č. 6

> **Upravujte pouze soubor `assignment_6_1.py`!**

### Opilcova procházka
Opilec se probral v půli cesty mezi domovem a hospodou. V každé iteraci se posune o jeden krok doleva (směrem k domovu)
nebo doprava (směrem do hospody). Pohyb je řízen náhodně s předem definovanou pravděpodobností pro návrat domů. 

Do skriptu `assignemnt_6_1.py` implementujte algoritmus, který bude simulovat pohyb opilce. Základními parametry budou 
vzdálenost mezi domovem a hospodou a maximální počet kroků, které může opilec udělat. Simulace skončí ve chvíli, 
kdy dojde k vyčerpání počtu kroků nebo opilec dojde do jednoho z cílů. Program se bude skládat z následujících funkcí, 
bloků a vazeb:

> **Pozn.:** Při realizaci programu se striktně držte v zadání definovaných názvů funkcí, proměnných a parametrů. 
> V opačném případě váš úkol neprojde automatickými testy.


### Řídící funkce programu – 1. část
* Prozkoumejte dokumentační řetězec funkce `main()` a na jeho základě definujte vstupní parametry v hlavičce funkce 
  `main()`.


### Funkce pro generování cesty
* Do skriptu implementujte funkci s názvem `footpath_generator()`. 
* Funkce bude mít 1 vstupní parametr `path_len` s výchozí hodnotou `11`.
* Funkce vygeneruje a **vrátí** grafický výstup simulace v podobě seznamu textových řetězců. Délka seznamu bude 
  rovna parametru `path_len`. Seznam s délkou cesty `11` bude vypadat takto:
  ```python
  ['home', '_', '_', '_', '_', 'X', '_', '_', '_', '_', 'pub']
  ```
  Kde řetězec `'_'` značí cestu a `'X'` značí výchozí pozici opilce, která bude vždy v polovině seznamu.
* Všechny textové řetězce budou do seznamu generovány z globálních konstant `TARGET_1`, `TARGET_2`, `DRUNKARD` a 
  `FOOTPATH`. Např. `TARGET_1 = 'home'`.
* Funkce vrátí `None`, pokud hodnota argumentu `path_len` bude menší než `3` nebo bude sudé číslo.


### Funkce pro posun opilce
* Do skriptu implementujte funkci s názvem `update_footpath()`. 
* Funkce bude mít 3 vstupní parametry `footpath`, `old_pos` a `new_pos`.
* Funkce posune opilce `'X'` v proměnné `footpath` z původní pozice `old_pos` na novou pozici `new_pos`:
  * Původní: 
    ```python
    ['home', '_', '_', '_', '_', 'X', '_', '_', '_', '_', 'pub']
    ```
  * Upravená:
    ```python
    ['home', '_', '_', '_', '_', '_', 'X', '_', '_', '_', 'pub']
    ```
* Funkce vrátí upravenou proměnnou `footpath`.

> **Pozn.:** Pozor na to, aby funkce po posunu opilce správně vyplnila jeho původní pozici řetězcem symbolizující
> cestu.


### Funkce pro náhodné generování směru cesty
Aby byla simulace skutečně založená na náhodě, vytvoříme si jednoduchou funkci pro generování směru pomocí simulace 
hodu 100 stěnnou kostkou.
* Ve skriptu proveďte import funkce `randint()` z balíčku `random`.
* Implementujte funkci `get_direction()`. 
* Funkce bude mít jeden vstupní parametr `p_home` s výchozí hodnotou `0.5`. Parametr udává pravděpodonost, že se opilec
  vydá směrem k domovu.
* Naše funkce pomocí funkce `randint()` vygeneruje náhodné celé číslo `dice` v rozmezí od `1` do `100`. Funkce dále
  **spočítá pravděpodobnost** jevu, že na kostce padne číslo stejné nebo menší než `dice`. Všechna čísla na kostce 
  mají stejnou pravděpodobnost, že padnou.
* Funkce vrátí hodnotu posunu o 1 doprava, pokud je vypočítaná pravděpodobnost větší nebo rovno `p_home`. V opačném 
  případě funkce vrátí hodnotu posunu o 1 doleva.


### Řídící funkce programu – 2. část
V této části si celou simulaci poskládáme dohromady.
* Do funkce `main()` doplňte uložení výchozí pozice opilce a generování cesty pomocí funkce `footpath_generator()`.
* Ukončete funkci `main()` s vrácením hodnoty `None`, pokud nelze cestu vygenerovat (je příliš krátká nebo uživatel 
  zadal sudou délku cesty).
* Do funkce `main()` doplňte cyklus ukončený po dosažení maximálního počtu kroků `max_steps`, který bude simulovat 
  jednotlivé kroky procházky. V každé iteraci cyklu dojde k:
    * Uložení kopie pozice opilce do proměnné `old_pos`.
    * Určení směru pohybu.
    * Aktualizace pozice opilce.
    * Vyhodnocení nové pozice opilce – pokud opilec došel buď domů nebo zpět do hospody, bude funkce ukončena a vrátí
      textový řetězec odpovídající dosaženému cíli (např.: `'home'`).
    * Aktualizace vygenerované cesty pomocí funkce `update_footpath()`.
    * Vytisknutí upravené cesty opilce do terminálu.
    * Pozastavení simulace na 0.2 vteřiny pomocí funkce `sleep()` z modulu `time`.
* Pokud opilec nedojde do jednoho z cílů v určeném počtu kroků, vrátí funkce řetězec `'darkness'`. 


### Dokumentační řetězce
Doplňte všechny funkce o dokumentační řetězec s popisem účelu funkce a jednotlivých vstupních a výstupních parametrů.
