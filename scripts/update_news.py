import json
from datetime import datetime

today = datetime.now().strftime("%Y-%m-%d")

news = [

    {
        "title":"🔥 Pokémon GO 最新情報",

        "date":today,

        "rating":"★★★★★",

        "summary":"系統成功自動更新。",

        "ai":"AI建議：留意最新活動公告。"
    }

]

with open(
    "news.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        news,
        f,
        ensure_ascii=False,
        indent=2
    )
