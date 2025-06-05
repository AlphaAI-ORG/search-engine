from veckeysearch.graph import graph

config1 = {
    "configurable": {
        "thread_id": "user_1",  #uuid 로 변경?
        "index_name": "test_0603",
        "search_num": 5,
        "debug": True
    }
}
user_query = "투자의 공포"
search_method = "vector"

result = graph.invoke({"user_query": user_query, "search_method": search_method}, config=config1)

print(result["search_results"])
print(len(result["search_results"])) # 5 = search_num

# 결과 저장
import json
data = result["search_results"]

with open(f"data/{search_method}_output_example.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)


