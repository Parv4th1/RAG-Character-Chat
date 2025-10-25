import os
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

EMBEDDINGS_DIR = "embeddings"

def build_index(chunks, book_name):
    """
    Builds or loads a FAISS index for a given book.
    Saves the index and chunk vectors in the embeddings/ folder.
    Returns: embed_model, index, chunks, chunk_vectors
    """
    os.makedirs(EMBEDDINGS_DIR, exist_ok=True)
    safe_name = book_name.lower().replace(" ", "_")
    index_path = os.path.join(EMBEDDINGS_DIR, f"{safe_name}.index")
    metadata_path = os.path.join(EMBEDDINGS_DIR, f"{safe_name}_meta.npy")
    vectors_path = os.path.join(EMBEDDINGS_DIR, f"{safe_name}_vectors.npy")

    embed_model = SentenceTransformer('all-MiniLM-L6-v2')

    if os.path.exists(index_path) and os.path.exists(metadata_path) and os.path.exists(vectors_path):
        print(f"🔍 Loading existing index for '{book_name}'...")
        index = faiss.read_index(index_path)
        chunks = np.load(metadata_path, allow_pickle=True).tolist()
        chunk_vectors = np.load(vectors_path)
        return embed_model, index, chunks, chunk_vectors

    # Create new index
    print(f"📖 Creating new index for '{book_name}'...")
    chunk_vectors = embed_model.encode(chunks)
    dimension = chunk_vectors.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(chunk_vectors))

    # Save index and metadata
    faiss.write_index(index, index_path)
    np.save(metadata_path, np.array(chunks, dtype=object))
    np.save(vectors_path, chunk_vectors)

    print(f"✅ Index saved to {index_path}")
    return embed_model, index, chunks, chunk_vectors
