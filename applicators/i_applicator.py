from model.model import Model


class IApplicator:

    def apply(self, model: Model):
        raise NotImplementedError
