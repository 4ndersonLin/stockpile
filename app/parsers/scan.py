<<<<<<< HEAD
from app.objects.c_relationship import Relationship
from plugins.stockpile.app.parsers.base_parser import BaseParser
=======
from app.objects.secondclass.c_fact import Fact
from app.objects.secondclass.c_relationship import Relationship
from app.utility.base_parser import BaseParser
>>>>>>> upstream/master


class Parser(BaseParser):

    def parse(self, blob):
        relationships = []
        for match in self.line(blob):
            values = match.split(':')
            for mp in self.mappers:
                relationships.append(
<<<<<<< HEAD
                    Relationship(source=(mp.source, values[0]),
                                 edge=mp.edge,
                                 target=(mp.target, values[1]))
=======
                    Relationship(source=Fact(mp.source, values[0]),
                                 edge=mp.edge,
                                 target=Fact(mp.target, values[1]))
>>>>>>> upstream/master
                )
        return relationships
