import random

print("Hej och välkommen till spelet Sten, Sax, Påse!")
print("Följ alternativen nedan och försök slå datorn.")
print("Välj mellan: sten, sax eller påse\n")

alternativ = ("sten", "sax", "påse")

while True:
    spelare_val = None
    dator_val = random.choice(alternativ)

    while spelare_val not in alternativ:
        spelare_val = input("Välj sten, sax eller påse: ").lower()

    print(f"\nSpelare: {spelare_val}")
    print(f"Dator: {dator_val}")

    if spelare_val == dator_val:
        print("Oavgjort! Försök igen.\n")
        continue
    elif (
        (spelare_val == "sten" and dator_val == "sax") or
        (spelare_val == "sax" and dator_val == "påse") or
        (spelare_val == "påse" and dator_val == "sten")
    ):
        print("Grattis, du vann!")
        break
    else:
        print("Beklagar men du förlorade")
        break
