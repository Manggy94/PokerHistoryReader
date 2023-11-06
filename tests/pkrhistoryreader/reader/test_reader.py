import unittest
import pkrhistoryreader.reader as reader
from dotenv import load_dotenv
import datetime

load_dotenv(".env")


class ReaderTestCase(unittest.TestCase):
    """
    A class to test the HistoryReader class
    """
    def setUp(self) -> None:
        """
        Set up the test by creating a HistoryReader object and parsing a hand history
        :return:
        """
        self.reader = reader.HistoryReader()
        self.key1 = "data/histories/split/2023/08/08/677652300/2910494466559180809-74-1691516183.txt"
        self.histo1 = self.reader.bucket.Object(self.key1).get()['Body'].read().decode('utf-8')
        self.hand_id_dict = self.reader.parse_history_from_key(self.key1)

    def test_new_reader(self):
        """
        Test the creation of a HistoryReader object
        :return:
        """
        self.assertIsInstance(self.reader, reader.HistoryReader)

    def test_parse_history_from_key(self):
        """
        Test the parsing of a hand history from a key
        :return:
        """
        histo_dict = self.reader.parse_history_from_key(self.key1)
        self.assertIsInstance(histo_dict, dict)
        self.assertEqual("2910494466559180809-74-1691516183", histo_dict["HandId"])
        self.assertEqual(histo_dict, self.hand_id_dict)

    def test_extract_hand_id(self):
        """
        Test the extraction of the hand id from a hand history
        :return:
        """
        hand_id_dict = (self.reader.extract_hand_id(self.histo1))
        hand_id = hand_id_dict["HandId"]
        self.assertIsInstance(hand_id_dict, dict)
        self.assertIsInstance(hand_id, str)
        self.assertEqual("2910494466559180809-74-1691516183", hand_id)

    def test_extract_game_type(self):
        """
        Test the extraction of the game type from a hand history
        :return:
        """
        game_type_dict = (self.reader.extract_game_type(self.histo1))
        game_type = game_type_dict["Gametype"]
        self.assertIsInstance(game_type_dict, dict)
        self.assertIsInstance(game_type, str)
        self.assertEqual("Tournament", game_type)

    def test_extract_players(self):
        """
        Test the extraction of the players from a hand history
        :return:
        """
        players_dict = (self.reader.extract_players(self.histo1))
        p1 = players_dict.get(1)
        p3 = players_dict.get(3)
        print(p1, p3)
        self.assertIsInstance(players_dict, dict)
        self.assertEqual(8, len(players_dict))
        self.assertIsInstance(p1, dict)
        self.assertEqual(set(p1.keys()), {"seat", "pseudo", "stack", "bounty"})
        self.assertEqual(1, p1["seat"])
        self.assertIsInstance(p1["seat"], int)
        self.assertEqual("pti math", p1["pseudo"])
        self.assertIsInstance(p1["pseudo"], str)
        self.assertEqual(34558, p1["stack"])
        self.assertIsInstance(p1["stack"], float)
        self.assertEqual(4.5, p1["bounty"])
        self.assertIsInstance(p1["bounty"], float)
        self.assertEqual(3, p3["seat"])
        self.assertEqual("manggy94", p3["pseudo"])
        self.assertEqual(76981, p3["stack"])
        self.assertEqual(6.75, p3["bounty"])

    def test_extract_posting(self):
        """
        Test the extraction of the postings from a hand history
        :return:
        """
        posting_list = (self.reader.extract_posting(self.histo1))
        self.assertIsInstance(posting_list, list)
        posting1 = posting_list[0]
        self.assertIsInstance(posting1, dict)
        self.assertEqual(set(posting1.keys()), {"pseudo", "amount", "blind_type"})
        self.assertEqual("Sniper_Evx", posting1["pseudo"])
        self.assertIsInstance(posting1["pseudo"], str)
        self.assertEqual(160, posting1["amount"])
        self.assertIsInstance(posting1["amount"], float)
        self.assertEqual("ante", posting1["blind_type"])
        self.assertIsInstance(posting1["blind_type"], str)

    def test_extract_buyin(self):
        """
        Test the extraction of the buyin from a hand history
        :return:
        """
        buyin_dict = (self.reader.extract_buyin(self.histo1))
        self.assertIsInstance(buyin_dict, dict)
        self.assertEqual(set(buyin_dict.keys()), {"Buyin", "ko", "Rake"})
        self.assertEqual(9, buyin_dict["Buyin"])
        self.assertIsInstance(buyin_dict["Buyin"], float)
        self.assertEqual(0, buyin_dict["ko"])
        self.assertIsInstance(buyin_dict["ko"], float)
        self.assertEqual(1, buyin_dict["Rake"])
        self.assertIsInstance(buyin_dict["Rake"], float)

    def test_extract_datetime(self):
        """
        Test the extraction of the datetime from a hand history
        :return:
        """
        datetime_dict = (self.reader.extract_datetime(self.histo1))
        self.assertIsInstance(datetime_dict, dict)
        self.assertEqual(set(datetime_dict.keys()), {"Datetime"})
        self.assertIsInstance(datetime_dict["Datetime"], datetime.datetime)
        self.assertEqual(datetime.datetime(2023, 8, 8, 17, 36, 23), datetime_dict["Datetime"])

    def test_extract_blinds(self):
        """
        Test the extraction of the blinds from a hand history
        :return:
        """
        blinds_dict = (self.reader.extract_blinds(self.histo1))
        self.assertIsInstance(blinds_dict, dict)
        self.assertEqual(set(blinds_dict.keys()), {"SB", "BB", "Ante"})
        self.assertIsInstance(blinds_dict["SB"], float)
        self.assertEqual(700, blinds_dict["SB"])
        self.assertIsInstance(blinds_dict["BB"], float)
        self.assertEqual(1400, blinds_dict["BB"])
        self.assertIsInstance(blinds_dict["Ante"], float)
        self.assertEqual(160, blinds_dict["Ante"])

    def test_extract_level(self):
        """
        Test the extraction of the level from a hand history
        :return:
        """
        level_dict = (self.reader.extract_level(self.histo1))
        self.assertIsInstance(level_dict, dict)
        self.assertEqual(set(level_dict.keys()), {"Level"})
        self.assertIsInstance(level_dict["Level"], int)
        self.assertEqual(12, level_dict["Level"])

    def test_extract_max_players(self):
        """
        Test the extraction of the max players from a hand history
        :return:
        """
        max_players_dict = (self.reader.extract_max_players(self.histo1))
        self.assertIsInstance(max_players_dict, dict)
        self.assertEqual(set(max_players_dict.keys()), {"max_players"})
        self.assertIsInstance(max_players_dict["max_players"], int)
        self.assertEqual(8, max_players_dict["max_players"])

    def test_extract_button_seat(self):
        """
        Test the extraction of the button seat from a hand history
        :return:
        """
        button_seat_dict = (self.reader.extract_button_seat(self.histo1))
        self.assertIsInstance(button_seat_dict, dict)
        self.assertEqual(set(button_seat_dict.keys()), {"Button"})
        self.assertIsInstance(button_seat_dict["Button"], int)
        self.assertEqual(3, button_seat_dict["Button"])

    def test_extract_hero_hand(self):
        """
        Test the extraction of the hero hand from a hand history
        :return:
        """
        hero_combo_dict = (self.reader.extract_hero_hand(self.histo1))
        self.assertIsInstance(hero_combo_dict, dict)
        self.assertEqual(set(hero_combo_dict.keys()), {"Hero", "Card1", "Card2"})
        self.assertIsInstance(hero_combo_dict["Hero"], str)
        self.assertEqual("manggy94", hero_combo_dict["Hero"])
        self.assertIsInstance(hero_combo_dict["Card1"], str)
        self.assertEqual("8s", hero_combo_dict["Card1"])
        self.assertIsInstance(hero_combo_dict["Card2"], str)
        self.assertEqual("Ah", hero_combo_dict["Card2"])

    def test_extract_flop(self):
        """
        Test the extraction of the flop from a hand history
        :return:
        """
        flop_dict = (self.reader.extract_flop(self.histo1))
        self.assertIsInstance(flop_dict, dict)
        self.assertEqual(set(flop_dict.keys()), {"Flop1", "Flop2", "Flop3"})
        self.assertIsInstance(flop_dict["Flop1"], str)
        self.assertEqual("5c", flop_dict["Flop1"])
        self.assertIsInstance(flop_dict["Flop2"], str)
        self.assertEqual("2h", flop_dict["Flop2"])
        self.assertIsInstance(flop_dict["Flop3"], str)
        self.assertEqual("6d", flop_dict["Flop3"])

    def test_extract_turn(self):
        """
        Test the extraction of the turn from a hand history
        :return:
        """
        turn_dict = (self.reader.extract_turn(self.histo1))
        self.assertIsInstance(turn_dict, dict)
        self.assertEqual(set(turn_dict.keys()), {"Turn"})
        self.assertIsInstance(turn_dict["Turn"], str)
        self.assertEqual("2s", turn_dict["Turn"])

    def test_extract_river(self):
        """
        Test the extraction of the river from a hand history
        :return:
        """
        river_dict = (self.reader.extract_river(self.histo1))
        self.assertIsInstance(river_dict, dict)
        self.assertEqual(set(river_dict.keys()), {"River"})
        self.assertIsInstance(river_dict["River"], str)
        self.assertEqual("Th", river_dict["River"])

    def test_extract_actions(self):
        """
        Test the extraction of the actions from a hand history
        :return:
        """
        actions_dict = (self.reader.extract_actions(self.histo1))
        self.assertIsInstance(actions_dict, dict)
        self.assertEqual(set(actions_dict.keys()), {"PreFlop", "Flop", "Turn", "River"})
        preflop_actions = actions_dict["PreFlop"]
        self.assertIsInstance(preflop_actions, list)
        action2 = preflop_actions[1]
        self.assertIsInstance(action2, dict)
        self.assertEqual(set(action2.keys()), {"player", "action", "amount"})
        self.assertIsInstance(action2["player"], str)
        self.assertEqual("WhyMe0", action2["player"])
        self.assertIsInstance(action2["action"], str)
        self.assertEqual("folds", action2["action"])
        self.assertIsInstance(action2["amount"], float)
        self.assertEqual(0.0, action2["amount"])

    def test_extract_showdown(self):
        """
        Test the extraction of the showdown from a hand history
        :return:
        """
        showdown_dict = (self.reader.extract_showdown(self.histo1))
        self.assertIsInstance(showdown_dict, dict)
        showdown1 = showdown_dict.get("manggy94")
        self.assertIsInstance(showdown1, dict)
        self.assertEqual(set(showdown1.keys()), {"Card1", "Card2"})
        self.assertIsInstance(showdown1["Card1"], str)
        self.assertEqual("8s", showdown1["Card1"])
        self.assertIsInstance(showdown1["Card2"], str)
        self.assertEqual("Ah", showdown1["Card2"])

    def test_extract_winners(self):
        """
        Test the extraction of the winners from a hand history
        :return:
        """
        winners_dict = (self.reader.extract_winners(self.histo1))
        self.assertIsInstance(winners_dict, dict)
        winner1 = winners_dict.get("manggy94")
        self.assertIsInstance(winner1, dict)
        self.assertEqual(set(winner1.keys()), {"amount", "pot_type"})
        self.assertIsInstance(winner1["amount"], float)
        self.assertEqual(10380, winner1["amount"])
        self.assertIsInstance(winner1["pot_type"], str)
        self.assertEqual("pot", winner1["pot_type"])

    def test_parse_hand(self):
        """
        Test the parsing of a hand history
        :return:
        """
        parsed_hand_dict = self.reader.parse_hand(self.histo1)
        self.assertIsInstance(parsed_hand_dict, dict)
        self.assertEqual(set(parsed_hand_dict.keys()), {
            "HandId", "Datetime", "GameType", "Buyins", "Blinds", "Level", "MaxPlayers", "ButtonSeat", "TableName",
            "Players", "HeroHand", "Postings", "Actions", "Flop", "Turn", "River", "Showdown", "Winners"})
