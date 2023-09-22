import unittest
import pkrhistoryreader.reader as reader
from dotenv import load_dotenv

load_dotenv(".env")


class ReaderTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.reader = reader.HistoryReader()
        self.key1 = "data/histories/split/2023/08/08/677652300/2910494466559180809-74-1691516183.txt"
        self.histo1 = self.reader.bucket.Object(self.key1).get()['Body'].read().decode('utf-8')

    def test_new_reader(self):
        self.assertIsInstance(self.reader, reader.HistoryReader)

    def test_extract_hand_id(self):
        hand_id_dict = (self.reader.extract_hand_id(self.histo1))
        hand_id = hand_id_dict["HandId"]
        self.assertIsInstance(hand_id_dict, dict)
        self.assertIsInstance(hand_id, str)
        self.assertEqual("2910494466559180809-74-1691516183", hand_id)



