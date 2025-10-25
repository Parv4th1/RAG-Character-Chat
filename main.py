from modules.embeddings import build_index
from modules.retriever import retrieve_relevant_chunks
from modules.book_loader import load_book
from modules.character_manager import get_characters
from modules.chat_engine import generate_response
from modules.user_options import choose_option
from config.settings import DEFAULT_BOOK_PATH, CHUNK_SIZE

def main():
    print("\nWelcome to Talk to a Character!\n")

    # Load book
    print("Loading book...")
    book_chunks = load_book(DEFAULT_BOOK_PATH, CHUNK_SIZE)

    # Book selection (future feature)
    book_name = "A Christmas Carol"

    # Build or load index
    embed_model, index, book_chunks, chunk_vectors = build_index(book_chunks, book_name)

    # Load characters
    characters = get_characters(book_name)
    conversations = {c: [] for c in characters}

    while True:
        # Character selection
        character_name = choose_option("Available characters:", characters.keys())
        traits = characters[character_name]
        print(f"\nNow chatting with {character_name}. Type 'exit' to quit or 'switch' to change character.\n")

        while True:
            user_input = input("You: ")
            if user_input.lower() in ["exit", "quit"]:
                print("Goodbye!")
                return
            if user_input.lower() == "switch":
                break

            # Retrieve relevant context using prebuilt index and in-memory vectors
            context = retrieve_relevant_chunks(
                user_input,
                book_chunks,
                chunk_vectors,
                embed_model,
                index,
                top_k=3,
                filter_name=character_name.split()[0]
            )

            history = conversations[character_name]
            answer = generate_response(character_name, traits, context, history, user_input)
            print(f"{character_name}: {answer}\n")

            history.append(f"You: {user_input}")
            history.append(f"{character_name}: {answer}")

if __name__ == "__main__":
    main()
