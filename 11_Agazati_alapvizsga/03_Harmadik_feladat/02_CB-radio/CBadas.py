class CBadas:
    ora: int
    perc: int
    adas_db: int
    nev: str

    def __init__(self, sor: str) -> None:
        ora, perc, adas_db, nev = sor.split(';')
        self.ora = int(ora)
        self.perc = int(perc)
        self.adas_db = int(adas_db)
        self.nev = nev

    def atszamol_percre(self) -> int:
        return self.ora * 60 + self.perc
