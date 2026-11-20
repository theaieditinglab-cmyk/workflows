"""Agrega a cada workflow el botón "← Volver", que solo aparece si se entró desde la página del equipo.
Se corre después de agregar un workflow nuevo:  python agregar_volver.py   (no repite si ya está)."""
import os
MARCA = "<!-- volver-lab -->"
JS = MARCA + """<script>(function(){try{var h=location.origin+'/workflows/',r=document.referrer||'';
if(!(r===h||r===h+'index.html'||r.indexOf(h+'#')===0||r.indexOf(h+'?')===0))return;
var a=document.createElement('a');a.href='../';a.textContent='\u2190 Volver';
a.onclick=function(e){if(history.length>1){e.preventDefault();history.back();}};
a.style.cssText='position:fixed;left:max(14px,env(safe-area-inset-left,0px));bottom:calc(16px + env(safe-area-inset-bottom,0px));z-index:2147483647;background:#141210;color:#F6F0E6;border:2px solid #F6F0E6;font:600 16px system-ui,-apple-system,sans-serif;padding:12px 18px;border-radius:999px;text-decoration:none;box-shadow:0 6px 18px rgba(0,0,0,.35)';
document.body.appendChild(a);}catch(e){}})();</script>"""
n = 0
for d in sorted(os.listdir(".")):
    f = os.path.join(d, "index.html")
    if not os.path.isfile(f) or d == "one-line": continue
    s = open(f, encoding="utf-8").read()
    if MARCA in s: continue
    i = s.lower().rfind("</body>")
    s = s[:i] + JS + "\n" + s[i:] if i >= 0 else s + JS
    open(f, "w", encoding="utf-8", newline="").write(s); n += 1
print("agregado en", n, "workflows")
