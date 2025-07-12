from .state import State


def rrf(state: State, config):
    """for hybrid search"""

    keyword_hits = state["keyword_hits"]
    vector_hits = state["vector_hits"]
    
    # 문서별 가중 RRF 점수 계산
    rrf_scores = {}
    k = 60
    keyword_weight = config['metadata']['keyword_weight']
    vector_weight = config['metadata']['vector_weight']

    # 키워드 검색 결과 처리
    for rank, hit in enumerate(keyword_hits, 1):
        doc_id = hit["_id"]
        rrf_score = keyword_weight * (1 / (k + rank))
        rrf_scores[doc_id] = rrf_scores.get(doc_id, 0) + rrf_score
    
    # 벡터 검색 결과 처리 
    for rank, hit in enumerate(vector_hits, 1):
        doc_id = hit["_id"]
        rrf_score = vector_weight * (1 / (k + rank))
        rrf_scores[doc_id] = rrf_scores.get(doc_id, 0) + rrf_score
    
    # 모든 문서 정보 수집
    all_docs = {}
    for hit in keyword_hits + vector_hits:
        doc_id = hit["_id"]
        if doc_id not in all_docs:
            all_docs[doc_id] = hit
    
    # 가중 RRF 점수로 정렬
    sorted_docs = sorted(rrf_scores.items(), key=lambda x: x[1], reverse=True)
    
    # 최종 결과 구성
    hybrid_hits = []
    for doc_id, score in sorted_docs[:state["search_num"]]:
        doc = all_docs[doc_id].copy()
        doc["_score"] = score
        doc["weighted_rrf_score"] = score
        doc["keyword_weight"] = keyword_weight
        doc["vector_weight"] = vector_weight
        hybrid_hits.append(doc)
    
    return {"hybrid_hits": hybrid_hits}
