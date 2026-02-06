from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/transform', methods=['POST'])
def transform():
    data = request.get_json()
    text = data.get('text', '')

    return jsonify({
        "original": text,
        "uppercase": text.upper(),
        "reversed": text[::-1],
        "length": len(text)
    })


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)