# Hvis man skriver en crunch eller hashtag eller hva du ønsker å kalle
# det, så blir alt etter det på linja ignorert av python. Det er fint
# å kommentere koden sin så folk som leser den forstår hva den gjør.

# Dette er bare en linje som skriver noe greier:
print("Dette er en test!")

# Dette er en funksjonsdefinisjon som gir gjennomsnittet av to tall:
def testfunksjon(x: int, y: int) -> int:
    """
    Gir tilbake gjennomsnittet av parametrene som en int.
    >>> testfunksjon(3,5)
    4
    >>> testfunksjon(1,5)
    3
    >>> tesfunksjon(12, -12)
    0
    """
    return int((x + y) / 2)

# Her skriver jeg ut gjennomsnittet av to verdier:
print(testfunksjon(98, 0))