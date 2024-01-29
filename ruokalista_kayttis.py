import tkinter as tk
from tkinter import messagebox
import feedparser
import datetime

ravintolat = {
    "Piato": 'https://www.semma.fi/modules/MenuRss/MenuRss/CurrentWeek?costNumber=1408&language=fi',
    "Rentukka": 'https://www.semma.fi/modules/MenuRss/MenuRss/CurrentWeek?costNumber=1416&language=fi',
    "Maija": 'https://www.semma.fi/modules/MenuRss/MenuRss/CurrentWeek?costNumber=1402&amp&language=fi',
    "Ylisto": 'https://www.semma.fi/modules/MenuRss/MenuRss/CurrentWeek?costNumber=1403&language=fi',
    "Lozzi": 'https://www.semma.fi/modules/MenuRss/MenuRss/CurrentWeek?costNumber=1401&amp&language=fi',
    "Taide": 'https://www.compass-group.fi/menuapi/feed/rss/current-week?costNumber=0301&amp&language=fi'
}

paivat = ['Maanantai', 'Tiistai', 'Keskiviikko', 'Torstai', 'Perjantai']

def show_menu():
    valinta = var.get()

    if valinta == 1:
        valittu_ravintola = ravintola_entry.get()
        if valittu_ravintola in ravintolat:
            url = ravintolat[valittu_ravintola]
            rss = feedparser.parse(url)
            menu_text.set(rss.feed.title + "\n")

            day = datetime.datetime.today().weekday()

            menu_text.set(menu_text.get() + paivat[day] + '\n')

            ruoka = rss.entries[day].summary_detail.value
            ruokalista = ruoka.split('<br />')
            for ruoka_annos in ruokalista:
                menu_text.set(menu_text.get() + ruoka_annos.strip() + '\n')

        else:
            messagebox.showinfo("Virhe", "Valittua ravintolaa ei löytynyt.")

    elif valinta == 3:
        root.destroy()

    else:
        messagebox.showinfo("Virhe", "Virheellinen valinta, yritä uudelleen.")

root = tk.Tk()
root.title("Ruokalistat")

canvas = tk.Canvas(root, width=800, height=600)
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

var = tk.IntVar()
var.set(1)

ravintola_label = tk.Label(frame, text="Syötä valitsemasi ravintolan nimi:")
ravintola_label.pack()

ravintola_entry = tk.Entry(frame)
ravintola_entry.pack()


show_button = tk.Button(frame, text="Näytä", command=show_menu)
show_button.pack()

menu_text = tk.StringVar()
menu_label = tk.Label(frame, textvariable=menu_text)
menu_label.pack()

root.mainloop()
