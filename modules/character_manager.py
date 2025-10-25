def get_characters(book_name):
    if "a christmas carol" == book_name.lower():
        return {
            "Ebenezer Scrooge": "grumpy, miserly, cold-hearted, later remorseful",
            "Bob Cratchit": "kind, hardworking, caring, humble",
            "Tiny Tim": "innocent, optimistic, kind, hopeful",
            "Ghost of Christmas Past": "wise, gentle, reflective, guiding",
            "Ghost of Christmas Present": "cheerful, generous, lively, instructive",
            "Ghost of Christmas Yet to Come": "silent, mysterious, foreboding"
        }
    else:
        # Placeholder for future uploaded books
        return {"Narrator": "neutral and descriptive"}
