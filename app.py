from flask import Flask, request, jsonify
from models import Note

app = Flask(__name__)

@app.route('/notes', methods=['GET'])
def get_notes():
    return jsonify([note.json() for note in Note.query.all()])

@app.route('/notes/<int:id>', methods=['GET'])
def get_note(id):
    note = Note.query.get_or_404(id)
    return jsonify(note.json())

@app.route('/notes', methods=['POST'])
def create_note():
    data = request.get_json()
    new_note = Note(title=data['title'], content=data['content'])
    db.session.add(new_note)
    db.session.commit()
    return jsonify(new_note.json()), 201

@app.route('/notes/<int:id>', methods=['PUT', 'PATCH'])
def update_note(id):
    note = Note.query.get_or_404(id)
    data = request.get_json()
    note.title = data['title']
    note.content = data['content']
    db.session.commit()
    return jsonify(note.json())

@app.route('/notes/<int:id>', methods=['DELETE'])
def delete_note(id):
    note = Note.query.get_or_404(id)
    db.session.delete(note)
    db.session.commit()
    return '', 204

db.init_app(app)
if __name__ == '__main__':
    app.run(debug=True)