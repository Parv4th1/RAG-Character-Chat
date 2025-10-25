# Chat with Your Favourite Characters  

**Chat with your favourite characters from books, movies, and series!**  
This project is a **Retrieval-Augmented Generation (RAG)** based chat service that allows users to interact with fictional characters while keeping their responses faithful to the source material.  

---

## Project Goals  

- Deliver realistic, source-grounded character conversations.  
- Demonstrate practical RAG integration for educational and entertainment use.  
- Build a scalable, privacy-respecting framework for future AI storytelling experiences.   

---

## Future Scope  

- **Automatic Character Recognition** – Detect and extract characters automatically from any uploaded book.  
- **Multi-Character Chat** – Enable dynamic conversations between multiple characters and the user.  
- **Cloud Deployment** – Currently uses Gemini (free tier); AWS integration planned for secure, private, and commercial use.  

---

## Workflow  

1. **Upload Book**  
   - User uploads a text file (e.g., a novel or script).  

2. **Chunk Book Content**  
   - The text is divided into manageable sections (“chunks”) for embedding.  
   - *Current method:* Fixed-size chunking.  
   - *Future work:* Explore semantic or paragraph-based chunking for better coherence.  

3. **Create and Embed Vectors**  
   - Uses `SentenceTransformer('all-MiniLM-L6-v2')` to convert text chunks into embeddings.  
   - Stored in a **FAISS** vector database for fast similarity search.  
   - *Why FAISS?* Lightweight, efficient, and ideal for local prototyping.  
   - *Alternative considered:* Pinecone (scalable cloud option).  
   - *Without a vector DB:* Embeddings must be regenerated each run, increasing time and cost.  

4. **Retrieve Relevant Chunks**  
   - User query is encoded and compared against stored vectors.  
   - Top-matching chunks are retrieved using FAISS L2 similarity search.  

5. **Augment the Prompt**  
   - Retrieved context is added to the query to build a complete, context-aware prompt.  

6. **Generate Response**  
   - The prompt is passed to the **Gemini model**, which generates a grounded, character-consistent reply.  

---

## Tech Stack  

| Component | Technology |
|------------|-------------|
| **Language Model** | Gemini (Google) |
| **Embedding Model** | SentenceTransformer (all-MiniLM-L6-v2) |
| **Vector Database** | FAISS |
| **Language** | Python |
| **Architecture** | Retrieval-Augmented Generation (RAG) |

---

## Project Aims  

- **Secure Source Material** – When implemented on secure infrastructure (e.g., AWS), copyrighted authors or publishers can safely use their own works without risk of data exposure.  
- **Respect Copyright** – Only process texts that users own or have rights to use. The project prioritizes privacy, not copyright exemption.  
- **Authentic Character Interaction** – Characters respond according to their original traits and dialogue style.  
- **Cost Efficiency** – Uses RAG to reduce context length and token usage.  
- **Scalability** – Adding new books or series only requires adding them to the knowledge base. 

