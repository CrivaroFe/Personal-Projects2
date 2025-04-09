# Questo è un programma di calcolatrice avanzata che permette all'utente di eseguire operazioni matematiche complesse.
# La calcolatrice supporta operazioni come somma, sottrazione, moltiplicazione, divisione, calcoli di seno, coseno, tangente, radice quadrata, logaritmi e potenze.
# Inoltre, offre una semplice interfaccia grafica (GUI) usando la libreria tkinter.
# L'utente può anche scegliere di calcolare di nuovo o terminare il programma.

import tkinter as tk
import math

def calcola():
    try:
        operazione = operazione_entry.get()
        if operazione == 'somma':
            risultato = float(numero1_entry.get()) + float(numero2_entry.get())
        elif operazione == 'sottrazione':
            risultato = float(numero1_entry.get()) - float(numero2_entry.get())
        elif operazione == 'moltiplicazione':
            risultato = float(numero1_entry.get()) * float(numero2_entry.get())
        elif operazione == 'divisione':
            risultato = float(numero1_entry.get()) / float(numero2_entry.get())
        elif operazione == 'radice quadrata':
            risultato = math.sqrt(float(numero1_entry.get()))
        elif operazione == 'logaritmo':
            risultato = math.log(float(numero1_entry.get()))
        elif operazione == 'potenza':
            risultato = math.pow(float(numero1_entry.get()), float(numero2_entry.get()))
        elif operazione == 'seno':
            risultato = math.sin(math.radians(float(numero1_entry.get())))
        elif operazione == 'coseno':
            risultato = math.cos(math.radians(float(numero1_entry.get())))
        elif operazione == 'tangente':
            risultato = math.tan(math.radians(float(numero1_entry.get())))
        else:
            risultato = 'Operazione non valida'

        risultato_label.config(text='Risultato: ' + str(risultato))
    except Exception as e:
        risultato_label.config(text='Errore: ' + str(e))

def calcola_ancora():
    risposta = input('Vuoi calcolare un altro numero? (S per sì, N per no): ').upper()
    if risposta == 'S':
        risultato_label.config(text='')
        numero1_entry.delete(0, tk.END)
        numero2_entry.delete(0, tk.END)
        operazione_entry.delete(0, tk.END)
    else:
        root.quit()

# Creazione della finestra principale
root = tk.Tk()
root.title('Calcolatrice Avanzata')

# Creazione dei campi di input e dei bottoni
numero1_label = tk.Label(root, text='Primo numero:')
numero1_label.grid(row=0, column=0)
numero1_entry = tk.Entry(root)
numero1_entry.grid(row=0, column=1)

numero2_label = tk.Label(root, text='Secondo numero (se necessario):')
numero2_label.grid(row=1, column=0)
numero2_entry = tk.Entry(root)
numero2_entry.grid(row=1, column=1)

operazione_label = tk.Label(root, text='Operazione (somma, sottrazione, moltiplicazione, divisione, radice quadrata, logaritmo, potenza, seno, coseno, tangente):')
operazione_label.grid(row=2, column=0)
operazione_entry = tk.Entry(root)
operazione_entry.grid(row=2, column=1)

calcola_button = tk.Button(root, text='Calcola', command=calcola)
calcola_button.grid(row=3, column=0, columnspan=2)

risultato_label = tk.Label(root, text='Risultato:')
risultato_label.grid(row=4, column=0, columnspan=2)

# Inizializzazione della finestra principale
root.mainloop()