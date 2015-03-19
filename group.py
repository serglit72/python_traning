class Group:

    def __init__(self, name, header, footer):
        self.name = name
        self.header = header
        self.footer = footer

class Groups:

    def __init__(self, first_n, mid_n, last_n, nick_n, company, address, home_ph, cell_ph, email):
        self.first_n=first_n
        self.mid_n=mid_n
        self.last_n=last_n
        self.nick_n=nick_n
        self.company=company
        self.address=address
        self.home_ph=home_ph
        self.cell_ph=cell_ph
        self.email=email