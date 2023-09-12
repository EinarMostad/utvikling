def pastapenger(folk: int, gram_per_pers:int, kilopris: float) -> float:
    """
    Regner ut hvor mye det koster å kjøpe inn pasta for kantina basert
    på hvor mange folk de bergner til, hvor mange gram de beregner per 
    person og kiloprisen på pasta.
    >>> pastapenger(50, 250, 100)
    1250
    >>> pastapenger(100, 200, 80)
    1600
    >>> pastapenger(1000, 300, 500)
    150000
    """
    return folk * kilopris * gram_per_pers / 1000

print(pastapenger(50, 250,100))
print(pastapenger(100, 200,80))
print(pastapenger(1000, 300,500))