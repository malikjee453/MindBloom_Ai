import json
import faiss
from sentence_transformers import SentenceTransformer
from core.config import EMBEDDING_MODEL,INDEX_DIR
INDEX_PATH=INDEX_DIR/"knowledge.faiss"; META_PATH=INDEX_DIR/"metadata.json"
_model=None
def _model():
    global _model
    if _model is None: _model=SentenceTransformer(EMBEDDING_MODEL)
    return _model
def _load():
    if not INDEX_PATH.exists() or not META_PATH.exists(): return None,[]
    return faiss.read_index(str(INDEX_PATH)),json.loads(META_PATH.read_text(encoding="utf-8"))
def add_documents(records):
    if not records:return
    idx,meta=_load(); vec=_model().encode([r["text"] for r in records],normalize_embeddings=True,convert_to_numpy=True).astype("float32")
    if idx is None: idx=faiss.IndexFlatIP(vec.shape[1])
    idx.add(vec); meta.extend(records); faiss.write_index(idx,str(INDEX_PATH)); META_PATH.write_text(json.dumps(meta,ensure_ascii=False),encoding="utf-8")
def search(query,top_k=5):
    idx,meta=_load()
    if idx is None:return []
    vec=_model().encode([query],normalize_embeddings=True,convert_to_numpy=True).astype("float32")
    scores,ids=idx.search(vec,min(top_k,len(meta))); return [(meta[i],float(s)) for s,i in zip(scores[0],ids[0]) if i>=0]
