NOTES = {
    1: {"owner": "alice", "text": "alice pay rise proposal"},
    2: {"owner": "bob", "text": "bob lunch order"},
}

def read_note(session_user, note_id):
    note = NOTES.get(note_id)
    if note is None:
        return "no such note"
    return note["text"]

print("bob is authenticated:", True)
print("bob asks for his own note:", read_note("bob", 2))
print("bob asks for note one:", read_note("bob", 1))
