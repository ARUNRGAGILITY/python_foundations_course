import json

def write_to_json(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def read_from_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def create_book(file_path, book):
    library = read_from_json(file_path)
    library["library"]["books"].append(book)
    write_to_json(file_path, library)

def read_book(file_path, title):
    library = read_from_json(file_path)
    books = library["library"]["books"]
    for book in books:
        if book["title"] == title:
            return book
    return None

def update_book(file_path, title, updated_info):
    library = read_from_json(file_path)
    books = library["library"]["books"]
    for book in books:
        if book["title"] == title:
            book.update(updated_info)
            write_to_json(file_path, library)
            return True
    return False

def delete_book(file_path, title):
    library = read_from_json(file_path)
    books = library["library"]["books"]
    for i, book in enumerate(books):
        if book["title"] == title:
            del books[i]
            write_to_json(file_path, library)
            return True
    return False

# Sample usage:
if __name__ == "__main__":
    file_path = 'library.json'
    
    # Create a new book
    new_book = {"title": "Python Deep Dive", "author": "Mark Lutz", "year": 2021}
    create_book(file_path, new_book)
    
    # Read a book
    print(read_book(file_path, "Python Deep Dive"))
    
    # Update a book
    update_book(file_path, "Python Deep Dive", {"year": 2022})
    
    # Delete a book
    delete_book(file_path, "Python Deep Dive")
