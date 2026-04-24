# eine Liste von Zahlen im Speicher (RAM)
# Der Speicher reserviert Platz für die Liste [1, 2, 3, 4, 5] und weist jeder Zahl eine Adresse zu.
numbers = [1, 2, 3, 4, 5]

# Die CPU beginnt, die Schleife auszuführen.
# Sie liest die Anweisung: "Für jede Zahl in der Liste, drucke sie aus."
for num in numbers:
    # Die CPU fragt den Speicher: "Gib mir die nächste Zahl."
    # Der Speicher sendet die Zahl (z.B. `1`) an die CPU.
    # Die CPU speichert die Zahl temporär in einem Register (schneller Speicher im CPU).
    print(num)  # Die CPU sendet die Zahl an die Konsole zum Ausdrucken.