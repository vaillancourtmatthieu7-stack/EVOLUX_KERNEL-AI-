import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

SERVER = "http://127.0.0.1:8765"
MODEL = "/data/data/com.termux/files/home/models/nano.gguf"

SYSTEM = """Tu es Nano, une IA locale d'ingénierie.
Tu aides à programmer et à créer des simulations 3D.
Tu ne prétends pas être une personne réelle."""

@app.get("/")
def home():
    return """
    <h1>🧠 NanoAI</h1>
    <input id="p" style="width:80%;padding:12px" placeholder="Écris à Nano...">
    <button onclick="send()">Envoyer</button>
    <pre id="r"></pre>
    <script>
    async function send(){
      const prompt=document.getElementById("p").value;
      document.getElementById("r").textContent="Nano réfléchit...";
      const r=await fetch("/api/chat",{
        method:"POST",
        headers:{"Content-Type":"application/json"},
        body:JSON.stringify({prompt})
      });
      const d=await r.json();
      document.getElementById("r").textContent=d.answer||d.error;
    }
    </script>
    """

@app.post("/api/chat")
def chat():
    prompt=request.json.get("prompt","")

    try:
        r=requests.post(
            SERVER + "/v1/chat/completions",
            json={
                "model": MODEL,
                "messages":[
                    {"role":"system","content":SYSTEM},
                    {"role":"user","content":prompt}
                ],
                "temperature":0.7,
                "max_tokens":512,
                "stream":False
            },
            timeout=180
        )
        r.raise_for_status()
        data=r.json()

        return jsonify({
            "answer":data["choices"][0]["message"]["content"]
        })

    except Exception as e:
        return jsonify({"error":str(e)}),500

app.run(host="127.0.0.1",port=8787)
