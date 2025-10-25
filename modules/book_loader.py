def load_book(file_path, chunk_size=500):
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    words = text.split()
    chunks = [" ".join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]

    return chunks
