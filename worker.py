from flask import Flask, request, jsonify
from collections import Counter
import re

app = Flask(__name__)

@app.route('/map', methods=['POST'])
def map_task():
    data = request.json['text']
    # Simple regex to find words
    words = re.findall(r'\w+', data.lower())
    return jsonify(Counter(words))

if __name__ == '__main__':
    # Run multiple workers on different ports (e.g., 5001, 5002)
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 5001
    app.run(port=port)