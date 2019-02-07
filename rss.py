import feedparser

# 取得したい RSS を設定する
RSS = "http://b.hatena.ne.jp/hotentry.rss"
dic = feedparser.parse(RSS)

# ステータスコードを確認する
if int(dic.status) != 200:
    print("ERROR:" + str(dic.status))
    exit()

# RSS 情報を出力する
for entry in dic.entries:
    print(entry.title)
    print(entry.link)
