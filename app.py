from reader import PokerHistoryReader

pkrreader = PokerHistoryReader()
keys = [o.key for o in pkrreader.bucket.objects.filter(Prefix="data/histories/split/2016/03")]
key = keys[155]
hand_obj = pkrreader.bucket.Object(key).get()
hand_txt = hand_obj['Body'].read().decode('utf-8')
print(hand_txt)
result = pkrreader.extract_winners(hand_txt)
print(result)