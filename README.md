# Rückgeld-Rechner-mit-GUI
Ein Simples Python Programm das Rückgeld mit einer Benutzeroberfläche berechnet.
Dokumentation des Codes:

    Die erste Zeile importiert die Bibliothek Tkinter, die verwendet wird, um die GUI zu erstellen.
    
    Der Code definiert eine Funktion "calculate_change()", die aufgerufen wird, wenn der Benutzer auf die Schaltfläche "Berechnen" klickt.
    Innerhalb der Funktion wird versucht, die Eingaben des Benutzers in den Eingabefeldern "amount_due" und "cash_received" in float-Werte umzuwandeln.
    Dann wird der Rückgeldbetrag berechnet, indem man cash_received von amount_due subtrahiert.
    Wenn der Rückgeldbetrag kleiner als Null ist, wird eine Warnung angezeigt, dass die Zahlung unzureichend ist.
    Andernfalls wird der Rückgeldbetrag normal angezeigt.
    Im Falle einer ValueError, wird die Meldung "Invalid input" angezeigt
    Der nächste Teil des Codes erstellt das Fenster der Anwendung mit dem Titel "Change Calculator"
    Es erstellt Labels und Eingabefelder für die Eingabe des Betrags und des in bar gezahlten Betrags.
    Es erstellt auch eine Schaltfläche "Berechnen", die die oben definierte Funktion "calculate_change()" aufruft, und ein Label "Change", das das Rückgeldanzeigt.
    Schließlich wird die Funktion mainloop() aufgerufen, um die Anwendung zu starten und auf Ereignisse zu warten.
