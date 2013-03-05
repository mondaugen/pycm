import abc

class IndexableSequence:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def __len__(self):
	pass

    @abc.abstractmethod
    def __getitem__(self, key):
	pass

    @abc.abstractmethod
    def load_from_file(self, f):
	pass

    @abc.abstractmethod
    def adjust_indices(self, how):
	pass

