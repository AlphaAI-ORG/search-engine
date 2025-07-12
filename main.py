from veckeysearch.graph import graph

config1 = {
    "configurable": {
        "index_name": "test_0712",
        "host" : "localhost",
        "port" : 9200,
        "id" : "admin",
        "pwd" : "Fnmedia!12",
        "api_key" : "sk-proj-5mcCjPsGXAAMrCSNV3QuT3BlbkFJIDGGF1emXre3vz6wZ8HE",
        "keyword_weight" : 0.6, # hybrid search
        "vector_weight" : 0.4 , # hybrid search
        "debug": True
    }
}
user_query = "공포"
search_method = "hybrid" #keyword, vector, hybrid
search_num = 5
target_docs = ['아빠와 딸의 주식 투자 레슨']

result = graph.invoke({"user_query": user_query, "search_method": search_method, "search_num" : search_num, "target_docs": target_docs}, config=config1)

print(result["search_results"])
print(len(result["search_results"])) # 5 = search_num

# 결과 저장
import json
data = result["search_results"]

with open(f"data/{search_method}_output_example.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)


