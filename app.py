from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

posts = []
next_id = 1

# Criar post
@app.route('/posts', methods=['POST'])
def create_post():
    global next_id

    data = request.get_json()

    # Validação
    if not data or not all(k in data for k in ("title", "content", "category", "tags")):
        return jsonify({"error": "Dados inválidos"}), 400

    post = {
        "id": next_id,
        "title": data["title"],
        "content": data["content"],
        "category": data["category"],
        "tags": data["tags"],
        "createdAt": datetime.utcnow().isoformat(),
        "updatedAt": datetime.utcnow().isoformat()
    }

    posts.append(post)
    next_id += 1

    return jsonify(post), 201


# Listar todos os posts (com filtro)
@app.route('/posts', methods=['GET'])
def get_posts():
    term = request.args.get('term')

    if term:
        filtered = [
            p for p in posts
            if term.lower() in p["title"].lower()
            or term.lower() in p["content"].lower()
            or term.lower() in p["category"].lower()
        ]
        return jsonify(filtered), 200

    return jsonify(posts), 200


# Buscar 1 post
@app.route('/posts/<int:id>', methods=['GET'])
def get_post(id):
    for post in posts:
        if post["id"] == id:
            return jsonify(post), 200

    return jsonify({"error": "Post não encontrado"}), 404


# Atualizar post
@app.route('/posts/<int:id>', methods=['PUT'])
def update_post(id):
    data = request.get_json()

    for post in posts:
        if post["id"] == id:
            if not data:
                return jsonify({"error": "Dados inválidos"}), 400

            post["title"] = data.get("title", post["title"])
            post["content"] = data.get("content", post["content"])
            post["category"] = data.get("category", post["category"])
            post["tags"] = data.get("tags", post["tags"])
            post["updatedAt"] = datetime.utcnow().isoformat()

            return jsonify(post), 200

    return jsonify({"error": "Post não encontrado"}), 404


# Deletar post
@app.route('/posts/<int:id>', methods=['DELETE'])
def delete_post(id):
    for i, post in enumerate(posts):
        if post["id"] == id:
            posts.pop(i)
            return '', 204

    return jsonify({"error": "Post não encontrado"}), 404


if __name__ == '__main__':
    app.run(debug=True)
