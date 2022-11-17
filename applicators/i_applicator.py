from model.cell import Cell


class IApplicator:

    def apply(self, cell: Cell):
        raise NotImplementedError
