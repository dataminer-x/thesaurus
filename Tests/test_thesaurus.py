import unittest

from kalliope.core.NeuronModule import MissingParameterException, InvalidParameterException
from kalliope.neurons.thesaurus import Thesaurus


class TestThesaurus(unittest.TestCase):
    def setUp(self)
        pass
    # def __init__(self, **kwargs):
    #     super(Thesaurus, self).__init__(**kwargs)
    #     # api_key = 'a1dda690-09f1-4bed-b9d0-6abe98c6402b'
    #     self.api_key = kwargs.get('api_key', None)
    #     # word = 'umpire'
    #     self.word = kwargs.get('word', None)
    #     if not self._is_parameters_ok():
    #         raise InvalidParameterException
    #kalliop
    # def _is_parameters_ok(self):
    #     """
    #     Check if received parameters are ok to perform operations in the neuron
    #     :return: true if parameters are ok, raise an exception otherwise
    #     .. raises:: NotImplementedError
    #     """
    #     if self.api_key is None:
    #         raise MissingParameterException("Please provide an api_key")
    #     if self.word is None:
    #         raise MissingParameterException("Please provide a word")
    #
    #     return True
    #
    # def _get_ref_data(self):
    #     url = 'https://www.dictionaryapi.com/api/v3/references/thesaurus/json/' + word + '?key=' + api_key
    #     req = requests.get(url)
    #     todos = json.loads(req.text)
    #     self.Synonyms = todos[0]["meta"]["syns"]
    #     # word = todos[0]["meta"]["id"]
    #     self.Antonyms = todos[0]["meta"]["ants"]
    #     self.Definition = todos[0]["shortdef"]

# TODO Error handling - if empty, "Nothing found"

if __name__ == '__main__':
    unittest.main()