from pkrhistoryreader.reader import HistoryReader

pkrreader = HistoryReader()
keys = [o.key for o in pkrreader.bucket.objects.filter(Prefix="data/histories/split/2016/03")]
key = keys[155]
hand_obj = pkrreader.bucket.Object(key).get()
hand_txt = hand_obj['Body'].read().decode('utf-8')
result = pkrreader.extract_winners(hand_txt)
