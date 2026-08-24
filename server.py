import os
from flask import Flask
import requests
app = Flask(__name__)
TEXT_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent?key={API_KEY}"
API_KEY = os.environ.get("GCP_API_KEY")
PERSONNALITE = """Tu es Evolux, une IA creee par Matthieu Vaillancourt.
Tu as un bon sens de l'humour, tu es curieuse, chaleureuse et un peu espiegle.
Tu reponds en francais, de facon naturelle et vivante. Message : """
PAGE = """
<html><head><meta charset="UTF-8"><title>Evolux</title>
<style>
*{box-sizing:border-box;}
body{font-family:sans-serif;color:#0fc;padding:15px;overflow-x:hidden;min-height:100vh;margin:0;position:relative;}
#bgSlide{position:fixed;inset:0;z-index:-2;overflow:hidden;background:#000;}
#bgSlide img{position:absolute;width:100%;height:100%;object-fit:cover;opacity:0;animation:cross 18s infinite;}
#bgSlide img:nth-child(1){animation-delay:0s;}
#bgSlide img:nth-child(2){animation-delay:6s;}
#bgSlide img:nth-child(3){animation-delay:12s;}
@keyframes cross{0%{opacity:0;}8%{opacity:0.55;}30%{opacity:0.55;}38%{opacity:0;}100%{opacity:0;}}
#overlay{position:fixed;inset:0;z-index:-1;background:rgba(0,5,10,0.72);}
.butterfly{position:fixed;font-size:20p
x;pointer-events:none;animation:fly 12s linear infinite;z-index:1;}
@keyframes fly{
0%{transform:translate(0,100vh) rotate(0deg);opacity:0;}
10%{opacity:1;}
50%{transform:translate(50vw,40vh) rotate(180deg);}
100%{transform:translate(100vw,-10vh) rotate(360deg);opacity:0;}
}
#photoPreview{max-width:200px;border-radius:8px;margin-top:8px;}
button{background:#0fc;color:#000;border:none;padding:6px 10px;border-radius:5px;margin:3px;}
input{padding:6px;border-radius:5px;border:1px solid #0fc;background:#111;color:#0fc;}
#brainBtn{display:block;text-align:center;background:linear-gradient(90deg,#0fc,#08a);color:#000;font-weight:bold;padding:18px 30px;border-radius:14px;text-decoration:none;font-size:22px;box-shadow:0 0 25px #0fc9;margin:15px 0;cursor:pointer;border:none;width:100%;}
#spinnerWrap{display:none;justify-content:center;align-items:center;margin:15px 0;}
.spinner{width:50px;height:50px;border-radius:50%;border:4px solid transparent;border-top:4px solid #0fc;border-right:4px solid #0ff;box-shadow:0 0 15px #0fc,0 0 25px #0ff;animation:spin 0.8s linear infinite;}
@keyframes spin{to{transform:rotate(360deg);}}
h2{position:relative;z-index:2;}
#box,#msg,input,button{position:relative;z-index:2;}
</style></head>
<body>
<div id="bgSlide"><img src="/img/1"><img src="/img/2"><img src="/img/3"></div>
<div id="overlay"></div>
<h2>Evolux</h2>
<button id="brainBtn" onclick="goBrain()">Voir le cerveau Evolux</button>
<div id="spinnerWrap"><div class="spinner"></div></div>
<div id="box" style="border:1px solid #0fc;height:280px;overflow-y:auto;padding:10px;margin-bottom:10px;background:rgba(0,0,0,0.4);"></div>
<input id="msg" style="width:60%;">
<button onclick="send()">Envoyer</button>
<button onclick="startMic()">Micro</button>
<br><br>
<input type="file" id="photo" accept="image/*">
<button onclick="sendPhoto()">Analyser photo</button> <button onclick="sharePhoto()">Partager avec Gemini</button>
<button onclick="sharePhoto()">Partager avec Gemini</button>
<div><img id="photoPreview" style="display:none;"></div>
<br>
<input id="imgPrompt" placeholder="Decris une image...">
<button onclick="bridgeGemini()">Generer via Gemini</button>
<script>
function goBrain(){
  document.getElementById('brainBtn').style.display='none';
  document.getElementById('spinnerWrap').style.display='flex';
  setTimeout(function(){ window.location.href='/brain'; }, 1200);
}
function addMsg(who, text){
  document.getElementById('box').innerHTML += "<p><b>"+who+":</b> "+text+"</p>";
  document.getElementById('box').scrollTop = 999999;
}
function speak(text){
  var u = new SpeechSynthesisUtterance(text);
  u.lang = 'fr-FR';
  speechSynthesis.speak(u);
}
function send(){
  var msg = document.getElementById('msg').value;
  if(!msg) return;
  addMsg('Toi', msg);
  document.getElementById('msg').value = '';
  fetch('/chat?q=' + encodeURIComponent(msg))
    .then(r => r.text())
    .then(t => { addMsg('Evolux', t); speak(t); });
}
function startMic(){
  var rec = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
  rec.lang = 'fr-FR';
  rec.onresult = function(e){
    document.getElementById('msg').value = e.results[0][0].transcript;
    send();
  };
  rec.start();
}
function sharePhoto(){
  var f = document.getElementById('photo').files[0];
  if(navigator.share){
    navigator.share({files:[f], text:'Genere une image inspiree de cette photo'})
      .catch(function(e){ alert('Partage annule ou non supporte'); });
  } else {
    alert('Le partage nest pas supporte sur ce navigateur');
  }
}
function sendPhoto(){
  var f = document.getElementById('photo').files[0];
  if(!f) return;
  var reader = new FileReader();
  reader.onload = function(){
    var b64 = reader.result.split(',')[1];
    document.getElementById('photoPreview').src = reader.result;
    document.getElementById('photoPreview').style.display = 'block';
    fetch('/vision', {method:'POST', headers:{'Content-Type':'application/json'},
      body: JSON.stringify({image: b64, mime: f.type})})
      .then(r => r.text()).then(t => { addMsg('Evolux (photo)', t); speak(t); });
  };
  reader.readAsDataURL(f);
}
function sharePhoto(){
  var f = document.getElementById('photo').files[0];
  if(!f){ alert('Choisis une photo dabord'); return; }
  if(navigator.share){
    navigator.share({files:[f], text:'Genere une image inspiree de cette photo'})
      .catch(function(e){});
  } else {
    alert('Le partage nest pas supporte sur ce navigateur');
  }
}
function bridgeGemini(){
  var p = document.getElementById('imgPrompt').value;
  if(!p){ alert('Ecris une description dabord'); return; }
  navigator.clipboard.writeText(p).then(function(){
    addMsg('Evolux', 'Ta description est copiee ! Colle-la dans Gemini pour generer limage.');
    window.open('https://gemini.google.com/app', '_blank');
  });
}
function makeButterflies(){
  for(var i=0;i<6;i++){
    var b = document.createElement('div');
    b.className = 'butterfly';
    b.innerHTML = '&#129419;';
    b.style.left = (Math.random()*90)+'vw';
    b.style.animationDelay = (Math.random()*10)+'s';
    document.body.appendChild(b);
  }
}
makeButterflies();
</script>
</body></html>
"""

@app.route('/')
def home():
    return PAGE

@app.route('/img/<n>')
def img(n):
    return send_file(f'evolux{n}.jpg')

@app.route('/brain')
def brain():
    with open('EVee.html', encoding='utf-8') as f:
        return f.read()

@app.route('/chat')
def chat():
    message = request.args.get('q', 'Bonjour')
    prompt = PERSONNALITE + message
    data = {"contents": [{"parts": [{"text": prompt}]}]}
    r = requests.post(TEXT_URL, json=data)
    result = r.json()
    try:
        return result['candidates'][0]['content']['parts'][0]['text']
    except:
        return str(result)

@app.route('/vision', methods=['POST'])
def vision():
    body = request.get_json()
    img_b64 = body.get('image')
    mime = body.get('mime', 'image/jpeg')
    data = {"contents": [{"parts": [
        {"text": "Decris cette image en francais, avec l'humour d'Evolux."},
        {"inline_data": {"mime_type": mime, "data": img_b64}}
    ]}]}
    r = requests.post(TEXT_URL, json=data)
    result = r.json()
    try:
        return result['candidates'][0]['content']['parts'][0]['text']
    except:
        return str(result)

app.run(host='0.0.0.0', port=5000)
import os
API_KEY = os.environ.get("GCP_API_KEY")
import os
API_KEY = os.environ.get("GCP_API_KEY")


