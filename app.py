from flask import Flask, request, render_template_string
from nodes.llm_router_node import LLMRouterNode
from nodes.asset_worker_node import AssetWorkerNode
from nodes.llm_response_node import LLMResponseNode
from utils.query_builder import build_asset_query
from flask import send_from_directory
from pipeline import run_pipeline

app = Flask(__name__)

router = LLMRouterNode()
worker = AssetWorkerNode()
response_node = LLMResponseNode()


HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>AI Assistant</title>

    <style>
        body {
            font-family: Arial;
            background: #f5f6fa;
            direction: rtl;
            margin: 0;
            padding: 0;
        }

        .container {
            width: 55%;
            margin: 40px auto;
            background: white;
            padding: 25px;
            border-radius: 12px;
            box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
        }

        h2 {
            text-align: center;
        }

        input {
            width: 75%;
            padding: 10px;
            border-radius: 8px;
            border: 1px solid #ccc;
        }

        button {
            padding: 10px 15px;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            background: #4CAF50;
            color: white;
        }

        .result {
            margin-top: 20px;
            padding: 15px;
            background: #f9f9f9;
            border-radius: 10px;
        }

        img {
            max-width: 250px;
            margin-top: 10px;
            border-radius: 10px;
            display: block;
        }

        textarea {
            width: 100%;
            height: 120px;
            margin-top: 10px;
        }

        .copy {
            background: #2196F3;
            margin-top: 8px;
        }
    </style>
</head>

<body>

<div class="container">

    <h2>🤖 AI Assistant</h2>

    <!-- FORM פשוט -->
    <form method="POST">
        <input name="message" placeholder="כתוב בקשה..." required>
        <button type="submit">שלח</button>
    </form>
    
    {% if response %}
        {% if user_message %}
        <div class="result-box" style="background:#e8f0fe;">
            <b>הבקשה שלך:</b><br><br>
            {{ user_message }}
        </div>
        {% endif %}
    <div class="result">

        <h3>תוצאה:</h3>

        <div>{{ response.text }}</div>

        {% if response.image %}
            <img src="{{ url_for('static', filename='images/' + response.image) }}">
        {% endif %}

        <textarea id="out">{{ response.text }}</textarea>

        <button class="copy" onclick="copyText()">העתק טקסט</button>

    </div>

    {% endif %}

</div>

<script>
function copyText() {
    let text = document.getElementById("out");
    text.select();
    document.execCommand("copy");
    alert("הועתק!");
}
</script>

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    response = None
    user_message = ""
    
    if request.method == "POST":
        user_message = request.form["message"]

        result = run_pipeline(user_message)
        print(result)

        image_path = result.get("image")

        if image_path:
            image_path = image_path.replace("\\", "/")
            image_path = image_path.replace("./images/", "")
            image_path = image_path.replace("images/", "")

        response = {
            "text": result["text"],
            "image": image_path
        }

    return render_template_string(HTML, response=response, user_message=user_message)

if __name__ == "__main__":
    app.run(debug=True)