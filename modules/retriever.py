import numpy as np
import faiss

def retrieve_relevant_chunks(query, chunks, chunk_vectors, embed_model, index, top_k=3, filter_name=None):
    """
    Retrieve relevant chunks using FAISS and precomputed embeddings.
    Supports character filtering using in-memory vectors.
    """
    query_vector = embed_model.encode([query])

    if filter_name:
        # Filter chunks containing the character name
        filtered_indices = [i for i, c in enumerate(chunks) if filter_name.lower() in c.lower()]
        if not filtered_indices:
            filtered_indices = list(range(len(chunks)))

        # Compute L2 distances manually
        filtered_vectors = np.array([chunk_vectors[i] for i in filtered_indices])
        distances = np.linalg.norm(filtered_vectors - query_vector, axis=1)
        top_indices = np.argsort(distances)[:top_k]

        retrieved = "\n\n".join([chunks[filtered_indices[i]] for i in top_indices])
    else:
        # Use full FAISS index
        D, I = index.search(np.array(query_vector), k=top_k)
        retrieved = "\n\n".join([chunks[i] for i in I[0]])

    return retrieved
