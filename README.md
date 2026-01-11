# Engeto-3-projekt Elections Scraper 2017
Třetí projekt na Python Akademi od Engeta.
# Popis projektu

Tento projekt slouží ke stažení výsledků parlamentních voleb z roku 2017
z webu volby.cz pro vybraný územní celek.

Program stáhne výsledky hlasování pro všechny obce daného celku
a uloží je do CSV souboru.

---

## Instalace knihoven
Knihovny, které jsou použity v kodu uložene v souboru requirements.txt.
Po instalaci doporučuji použit nové virtuální prostředí a s nainstalovaným manažerem spustit následovně:


```bash
pip --version                   # overim verzi manazeru
pip install -r requirements.txt # nainstalujeme knihovny
``` 
---

## Spuštění projektu

Spuštění souboru main.py v rámci přík. řádku požaduje dva povinné argumenty.

```bash
python main <odkaz-uzemniho-celku> <vysledny-soubor>
``` 
Následně se vám stáhnou výsledky jako soubor s příponou .csv.

# Ukázka projektu

Výsledky hlasování pro okres Benešov:

1. argument https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101
2. argument vysledky_benesov.csv

Spuštění programu:

```bash
python main.py ´https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101´ ´vysledky_benesov.csv´
``` 

Průběh stahování:

STAHUJI DATA Z VYBRANEHO URL: https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101
UKLADAM DO SOUBORU: vysledky_benesov.csv

UKONCUJI main

Částečný výstup:

```bash

code,location,registered,envelopes,valid,ANO 2011,Blok proti islam.-Obran.domova,CESTA ODPOVĚDNÉ SPOLEČNOSTI,Dobrá volba 2016,Dělnic.str.sociální spravedl.,Komunistická str.Čech a Moravy,Křesť.demokr.unie-Čs.str.lid.,Občanská demokratická aliance,Občanská demokratická strana,REALISTÉ,"ROZUMNÍ-stop migraci,diktát.EU",Radostné Česko,Referendum o Evropské unii,SPORTOVCI,SPR-Republ.str.Čsl. M.Sládka,STAROSTOVÉ A NEZÁVISLÍ,Strana Práv Občanů,Strana svobodných občanů,Strana zelených,Svob.a př.dem.-T.Okamura (SPD),TOP 09,Unie H.A.V.E.L.,Česká pirátská strana,Česká str.sociálně demokrat.,Česká strana národně sociální,Řád národa - Vlastenecká unie
529303,Benešov,13104,8485,8437,2577,6,2,3,16,597,314,11,1052,58,35,3,6,17,21,802,10,112,109,682,414,3,948,624,5,10
532568,Bernartice,191,148,148,39,0,0,0,0,7,37,0,4,3,4,0,0,0,0,6,0,0,1,20,3,0,7,17,0,0

``` 

