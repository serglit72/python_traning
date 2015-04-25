__author__ = 'Sergei'
from sys import maxsize
class Contact:

    def __init__(self, first_n=None, mid_n=None, last_n=None, nick_n=None, company=None, address=None, home_ph=None, cell_ph=None, email=None, id=None):
        self.first_n=first_n
        self.mid_n=mid_n
        self.last_n=last_n
        self.nick_n=nick_n
        self.company=company
        self.address=address
        self.home_ph=home_ph
        self.cell_ph=cell_ph
        self.email=email
        self.id=id


#эта функция выдает значение данных в нормальном виде
    def __repr__(self):
        return "%s:%s" % ( self.id, self.first_n)

#это сравнение логическое двух значений по смыслу
    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id and self.first_n == other.first_n)


    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

