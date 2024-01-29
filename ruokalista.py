import feedparser
import datetime

ravintolat = {
    "Piato": 'https://www.semma.fi/modules/MenuRss/MenuRss/CurrentWeek?costNumber=1408&language=fi',
    "Rentukka": 'https://www.semma.fi/modules/MenuRss/MenuRss/CurrentWeek?costNumber=1416&language=fi',
    "Maija": 'https://www.semma.fi/modules/MenuRss/MenuRss/CurrentWeek?costNumber=1402&amp&language=fi',
    "Ylisto": 'https://www.semma.fi/modules/MenuRss/MenuRss/CurrentWeek?costNumber=1403&language=fi',
    "Lozzi": 'https://www.semma.fi/modules/MenuRss/MenuRss/CurrentWeek?costNumber=1401&amp&language=fi',
    "Taide": 'https://www.compass-group.fi/menuapi/feed/rss/current-week?costNumber=0301&amp&language=fi',
    "Fiilu": 'https://www.compass-group.fi/menuapi/feed/rss/current-week?costNumber=3364&language=fi'
}

paivat = ['Maanantai', 'Tiistai', 'Keskiviikko', 'Torstai', 'Perjantai']

while True:
    print("\n1. Näytä ravintolan ruokalista")
    print("2. Näytä kaikki ravintolat")
    print("3. Lopeta")

    valinta = input("Valitse toiminto: ")

    if valinta == '1':
        valittu_ravintola = input("Syötä valitsemasi ravintolan nimi: ")
        if valittu_ravintola in ravintolat:
            url = ravintolat[valittu_ravintola]
            rss = feedparser.parse(url)
            print(rss.feed.title + "\n")

            day = datetime.datetime.today().weekday()

            print(paivat[day] + '\n')

            ruoka = rss.entries[day].summary_detail.value
            ruokalista = ruoka.split('<br />')
            for ruoka_annos in ruokalista:
                print(ruoka_annos.strip())

            print('---------------------------------------------------------------------')
        else:
            print("Valittua ravintolaa ei löytynyt.")

    elif valinta == '2':
        for ravintola, url in ravintolat.items():
            print(f"Ravintola: {ravintola}")
            rss = feedparser.parse(url)
            day = datetime.datetime.today().weekday()
            ruoka = rss.entries[day].summary_detail.value
            ruokalista = ruoka.split('<br />')
            for ruoka_annos in ruokalista:
                print(ruoka_annos.strip())
            print('---------------------------------------------------------------------')
        break

    elif valinta == '3':
        break

    else:
        print("Virheellinen valinta, yritä uudelleen.")