<<<<<<< HEAD
from plugins.stockpile.app.parsers.base_parser import BaseParser
from app.objects.c_relationship import Relationship
=======
from app.utility.base_parser import BaseParser
from app.objects.secondclass.c_fact import Fact
from app.objects.secondclass.c_relationship import Relationship
>>>>>>> upstream/master


class Parser(BaseParser):

    def parse(self, blob):
        relationships = []
        vm_names = self._get_vm_names(blob)
        for name in vm_names:
            for mp in self.mappers:
                relationships.append(
<<<<<<< HEAD
                    Relationship(source=(mp.source, name),
                                 edge=mp.edge,
                                 target=(mp.target, None))
=======
                    Relationship(source=Fact(mp.source, name),
                                 edge=mp.edge,
                                 target=Fact(mp.target, None))
>>>>>>> upstream/master
                )
        return relationships

    """ PRIVATE """

    @staticmethod
    def _get_vm_names(blob):
        vm_names = []
<<<<<<< HEAD
        index = 0
        for line in blob.split('\n'):
            if 'VM NAME' in line:
                index = line.index('VM ID')
                continue
            if '=====' in line:
                continue
            if len(line) > 0:
                vm_names.append(line[0:index].strip())
=======
        for line in blob.split('\n'):
            line = line.split('\t\t')
            vm_names.append(line[0])
>>>>>>> upstream/master
        return vm_names
