import re, json
p='web/sis-alco.html'; s=open(p,encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(s.count(a),a[:70]); s=s.replace(a,b)
def cut(a,b,new):
    global s
    i=s.index(a); j=s.index(b,i); s=s[:i]+new+s[j:]

# ---------- fonts ----------
rep("family=Noto+Sans+Armenian:wght@400;500;600&family=Noto+Serif+Armenian:wght@400;500;600&display=swap", "family=Noto+Sans+Armenian:wght@400;500;600&family=Noto+Serif+Armenian:wght@400;500;600&family=Noto+Sans:wght@400;500;600&family=Noto+Serif:wght@400;500;600&display=swap")
rep("--serif:'Noto Serif Armenian', 'Times New Roman', serif;", "--serif:'Noto Serif Armenian', 'Noto Serif', 'Times New Roman', serif;")
rep("--sans:'Noto Sans Armenian', system-ui, sans-serif;", "--sans:'Noto Sans Armenian', 'Noto Sans', system-ui, sans-serif;")

# ---------- CSS ----------
rep("\n/* chapter rail */", r'''
/* ---------- language, logo ---------- */
.logo img{display:block;height:34px;width:auto}
.lang{display:inline-flex;align-items:center;gap:2px}
.lang button{background:none;border:none;padding:10px 6px;min-height:40px;font-size:14px;color:#8B968C;cursor:pointer}
.lang button.on{color:var(--fg)}
header.top.light .lang button{color:var(--stone-muted)}
header.top.light .lang button.on{color:var(--stone-ink)}
.more{align-self:flex-start;margin-top:14px;font-size:15px;color:var(--tuff-hi);text-underline-offset:4px}
.more:hover{color:var(--fg)}

/* ---------- ask sheet ---------- */
#ask{position:fixed;inset:0;z-index:90;display:flex;align-items:center;justify-content:center;background:rgba(8,11,9,.72);backdrop-filter:blur(6px);-webkit-backdrop-filter:blur(6px);padding:24px max(16px, env(safe-area-inset-right,0px)) calc(24px + env(safe-area-inset-bottom,0px)) max(16px, env(safe-area-inset-left,0px))}
.ask-box{position:relative;width:100%;max-width:460px;background:#151D19;border:1px solid var(--line);border-radius:4px;padding:32px 28px 28px}
.ask-box h2{margin:6px 0 22px;font-family:var(--serif);font-weight:500;font-size:28px;line-height:1.2;letter-spacing:-.01em;padding-right:64px}
.ask-box .kind{margin:0}
.ask-opts{display:grid;gap:10px}
.ask-opts .btn{width:100%}
.ask-x{position:absolute;top:14px;right:14px;background:none;border:none;min-height:44px;padding:0 10px;font-size:15px;color:var(--muted);cursor:pointer}
.ask-x:hover{color:var(--fg)}
.ask-tel{margin:18px 0 0;text-align:center;color:var(--muted);font-size:15px;user-select:all}
@media (max-width:760px){#ask{align-items:flex-end;padding-left:0;padding-right:0;padding-bottom:0}.ask-box{max-width:none;border-radius:8px 8px 0 0;border-bottom:none;padding-bottom:calc(28px + env(safe-area-inset-bottom,0px))}}
.msgr{display:flex;flex-wrap:wrap;gap:10px;margin-top:28px}
.msgr a{display:inline-flex;align-items:center;min-height:46px;padding:0 20px;border:1px solid var(--stone-ink);border-radius:2px;color:var(--stone-ink);text-decoration:none;font-weight:500;font-size:15px;transition:background .2s,color .2s}
.msgr a:hover{background:var(--stone-ink);color:var(--stone)}
.done pre{margin:0 0 20px;padding:16px;background:#F3F4F0;border:1px solid var(--stone-line);border-radius:2px;font:400 15px/1.6 var(--sans);white-space:pre-wrap;word-break:break-word;user-select:all}
.done .row{display:flex;flex-wrap:wrap;gap:10px}
.done a.btn{text-decoration:none}

/* ---------- product page ---------- */
#product-view{position:relative;z-index:2;min-height:100svh;padding-block:calc(104px + env(safe-area-inset-top,0px)) 80px}
.p-drag{position:fixed;left:0;top:0;width:50%;height:100%;cursor:grab;touch-action:pan-y}
.p-drag:active{cursor:grabbing}
.p-hint{position:fixed;left:0;width:50%;bottom:28px;margin:0;text-align:center;font-size:13px;color:#B9C0B6;pointer-events:none;transition:opacity .6s}
.p-hint.off{opacity:0}
.p-wrap{position:relative;display:flex;justify-content:flex-end;pointer-events:none}
.p-panel{width:100%;max-width:520px;display:flex;flex-direction:column;pointer-events:auto}
.p-panel h1{margin:0;font-family:var(--serif);font-weight:500;font-size:clamp(40px, 5.2vw, 76px);line-height:1;letter-spacing:-.035em;text-wrap:balance}
.p-panel .kind{margin:18px 0 10px}
.p-desc{margin:22px 0 0;font-size:18px;color:#D3D9D1;max-width:480px}
.p-facts{margin:32px 0 0;border-top:1px solid rgba(237,230,216,.2)}
.p-facts div{display:flex;justify-content:space-between;gap:24px;padding:13px 0;border-bottom:1px solid rgba(237,230,216,.12)}
.p-facts dt{color:var(--muted);font-size:15px}
.p-facts dd{margin:0;text-align:right;font-size:16px;font-variant-numeric:tabular-nums}
.p-serve{margin:28px 0 0;display:grid;grid-template-columns:repeat(2, minmax(0, 1fr));gap:8px 28px}
.p-serve dt{font-size:14px;color:var(--tuff-hi)}
.p-serve dd{margin:6px 0 0;font-family:var(--serif);font-size:19px;line-height:1.35}
.p-note{grid-column:1 / -1;margin:8px 0 0;font-size:13px;color:#8B968C}
.p-actions{display:flex;flex-wrap:wrap;gap:10px;margin-top:32px}
.p-nav{display:flex;justify-content:space-between;gap:16px;margin-top:40px;padding-top:20px;border-top:1px solid rgba(237,230,216,.14);font-size:15px}
.p-nav a{display:inline-flex;align-items:center;gap:8px;min-height:44px;color:#C9D0C8;text-decoration:none}
.p-nav a:hover{color:var(--fg)}
.m .p-drag{width:100%;height:46svh}
.m .p-hint{width:100%;bottom:auto;top:calc(46svh - 30px)}
.m #product-view{padding-block:46svh 110px}
.m .p-wrap{background:linear-gradient(to bottom, rgba(10,14,12,0), rgba(10,14,12,.82) 70px);padding-top:56px}
.m .p-panel{max-width:none}

/* chapter rail */''')

# ---------- HTML ----------
LOGO_IMG='<img src="logo.png" alt="" width="33" height="34">'
rep('''      <svg width="34" height="22" viewBox="0 0 34 22" fill="none" stroke="#C4836C" stroke-width="1.4" stroke-linejoin="round" aria-hidden="true"><path d="M1 21 L12 3 L20 14 L24 9 L33 21"></path></svg>
      <span>Սիս Ալկո</span>''', '      '+LOGO_IMG+'\n      <span>Սիս Ալկո</span>')
rep('''    <svg class="mark" width="64" height="42" viewBox="0 0 34 22" fill="none" stroke="#C4836C" stroke-width="1.1" stroke-linejoin="round" aria-hidden="true"><path d="M1 21 L12 3 L20 14 L24 9 L33 21"></path></svg>''', '    <img src="logo.png" alt="" width="108" height="110">')
rep('''      <span class="lang hide-sm"><b>Հայ</b> / <a href="https://sisalco.am/en" lang="en" style="color:inherit;padding:0">EN</a></span>
    </nav>''', '''    </nav>
    <span class="lang" data-noi18n aria-label="Language"><button type="button" data-l="hy" class="on">Հայ</button><button type="button" data-l="en" lang="en">EN</button><button type="button" data-l="ru" lang="ru">RU</button></span>''')
for ch in ['<p class="hint r">Ընտրեք տեսակը, և շիշը կփոխվի</p>']:
    rep(ch, ch+'\n        <a class="more r" href="#p-krunk-red">Մանրամասն այս շշի մասին</a>')
# details link for other chapters: insert after their lists
def add_more(first_id):
    global s
    i=s.index('data-v="%s"'%first_id); j=s.index('</ul>',i)+5
    s=s[:j]+'\n        <a class="more r" href="#p-%s">Մանրամասն այս շշի մասին</a>'%first_id+s[j:]
for fid in ['sis-red','fayton','hayanist']: add_more(fid)
rep('<div class="m-meta"><span id="m-spec"></span><span id="m-count"></span></div>', '<div class="m-meta"><span id="m-spec"></span><a class="more" id="m-more" href="#p-krunk-red" style="margin:0">Մանրամասն</a><span id="m-count" data-noi18n></span></div>')
rep('''          <div><dt>Հասցե</dt><dd>գ․ Հայանիստ, Էջմիածնի փողոց 39</dd></div>
        </dl>''', '''          <div><dt>Հասցե</dt><dd>գ․ Հայանիստ, Էջմիածնի փողոց 39</dd></div>
        </dl>
        <div class="msgr" data-noi18n>
          <a href="https://wa.me/37444449244" target="_blank" rel="noopener">WhatsApp</a>
          <a href="https://t.me/+37444449244" target="_blank" rel="noopener">Telegram</a>
          <a href="viber://chat?number=%2B37444449244">Viber</a>
        </div>''')
cut('        <div class="done" id="done" hidden>', '      </div>\n    </div>\n  </section>\n</main>', '''        <div class="done" id="done" hidden>
          <h3 id="done-h">Հարցումը պատրաստ է</h3>
          <p id="done-p">Ուղարկեք այն մեզ ձեզ հարմար եղանակով։</p>
          <pre id="done-text" data-noi18n></pre>
          <div class="row">
            <a class="btn send" id="done-wa" target="_blank" rel="noopener">Ուղարկել WhatsApp-ով</a>
            <button class="btn btn-ghost" type="button" id="done-copy" style="color:var(--stone-ink);border-color:var(--stone-line)">Պատճենել տեքստը</button>
            <button class="btn btn-ghost" type="button" id="again" style="color:var(--stone-ink);border-color:var(--stone-line)">Գրել նոր հարցում</button>
          </div>
        </div>
''')
rep('<main>', '''<div id="product-view" hidden>
  <div class="p-drag" id="p-drag" aria-hidden="true"></div>
  <div class="wrap p-wrap">
    <div class="p-panel">
      <a class="back" href="#catalog"><svg width="16" height="16" viewBox="0 0 18 18" fill="none" stroke="currentColor" stroke-width="1.4" aria-hidden="true"><path d="M11 3 L5 9 L11 15"></path></svg>Կատալոգ</a>
      <p class="kind" id="p-kind"></p>
      <h1 id="p-name"></h1>
      <p class="p-desc" id="p-desc"></p>
      <dl class="p-facts" id="p-facts"></dl>
      <dl class="p-serve">
        <div><dt>Մատուցում</dt><dd id="p-serve"></dd></div>
        <div><dt>Համադրվում է</dt><dd id="p-pair"></dd></div>
        <p class="p-note">Ընդհանուր խորհուրդ այս տեսակի խմիչքների համար</p>
      </dl>
      <div class="p-actions"><button class="btn btn-fill" type="button" id="p-ask">Հարցնել գինը</button></div>
      <nav class="p-nav" aria-label="Այլ շշեր"><a id="p-prev" href="#catalog"><svg width="16" height="16" viewBox="0 0 18 18" fill="none" stroke="currentColor" stroke-width="1.4" aria-hidden="true"><path d="M11 3 L5 9 L11 15"></path></svg><span></span></a><a id="p-next" href="#catalog"><span></span><svg width="16" height="16" viewBox="0 0 18 18" fill="none" stroke="currentColor" stroke-width="1.4" aria-hidden="true"><path d="M7 3 L13 9 L7 15"></path></svg></a></nav>
    </div>
  </div>
  <p class="p-hint" id="p-hint">Քաշեք շիշը՝ պտտելու համար</p>
</div>

<div id="ask" role="dialog" aria-modal="true" aria-labelledby="ask-h" hidden>
  <div class="ask-box">
    <button class="ask-x" id="ask-close" type="button">Փակել</button>
    <p class="kind" id="ask-p"></p>
    <h2 id="ask-h">Ինչպե՞ս եք ուզում գրել մեզ</h2>
    <div class="ask-opts">
      <a class="btn btn-fill" id="ask-wa" target="_blank" rel="noopener" data-noi18n>WhatsApp</a>
      <a class="btn btn-ghost" id="ask-tg" href="https://t.me/+37444449244" target="_blank" rel="noopener" data-noi18n>Telegram</a>
      <a class="btn btn-ghost" id="ask-vb" href="viber://chat?number=%2B37444449244" data-noi18n>Viber</a>
      <button class="btn btn-ghost" id="ask-form" type="button">Գրել ձևով</button>
    </div>
    <p class="ask-tel" data-noi18n>+374 44 449 244</p>
  </div>
</div>

<main>''')

# ---------- JS: data + i18n ----------
DATA = open('data7.js',encoding='utf-8').read()
rep("  function lock(on){ document.body.style.overflow = on ? 'hidden' : ''; if (lenis) { on ? lenis.stop() : lenis.start(); } }\n  function askFor(p){", DATA + "\n  function lock(on){ document.body.style.overflow = on ? 'hidden' : ''; if (lenis) { on ? lenis.stop() : lenis.start(); } }\n  function toForm(p){")
rep("  function split(el){", "  function askFor(p){\n    var a = document.getElementById('ask'); askName = p;\n    document.getElementById('ask-p').textContent = p; delete document.getElementById('ask-p').firstChild.__hy;\n    document.getElementById('ask-wa').href = 'https://wa.me/' + WA + '?text=' + encodeURIComponent(askMsg(p));\n    a.hidden = false; applyLang(a); lock(true); document.getElementById('ask-wa').focus();\n  }\n  var askName = '';\n  function askClose(){ document.getElementById('ask').hidden = true; lock(false); }\n  function split(el){")
# footer letters with language
rep("  split(document.getElementById('foot-letters'));", "  split(document.getElementById('foot-letters'));\n  document.querySelectorAll('#f-topic option').forEach(function(o){ o.value = o.textContent; });")

# mobile showroom: details link + translate
rep("      $('m-count').textContent = (idx + 1) + ' / ' + items.length;", "      $('m-count').textContent = (idx + 1) + ' / ' + items.length; $('m-more').href = '#p-' + it.id; applyLang(sec);")
rep("    var idx = 0, inView = !window.ScrollTrigger, tabs = $('m-tabs'), prog = $('m-prog');", "    var idx = 0, inView = !window.ScrollTrigger, tabs = $('m-tabs'), prog = $('m-prog'), sec = $('m-show');")
rep("    var sx = 0, sy = 0, down = false, sec = $('m-show');", "    var sx = 0, sy = 0, down = false;")
rep("    sec.addEventListener('pointerdown', function(e){ if (e.target.closest('button')) return;", "    sec.addEventListener('pointerdown', function(e){ if (e.target.closest('button, a')) return;")
# desktop variants: update details link
rep("      SA.variant[ch] = li.dataset.v;\n", "      SA.variant[ch] = li.dataset.v;\n      var mo = list.parentNode.querySelector('.more'); if (mo) mo.href = '#p-' + li.dataset.v;\n")

# form
cut("  /* form */", "  /* scroll story */", r'''  /* form: sends to FORM_ENDPOINT when one is set; otherwise hands the finished message to WhatsApp or the clipboard */
  var FORM_ENDPOINT = '';   // e.g. 'https://formspree.io/f/xxxx' or your own API; leave empty until the site is hosted
  var form = document.getElementById('form'), done = document.getElementById('done'), err = document.getElementById('f-err');
  function setText(id, hy){ var el = document.getElementById(id); el.textContent = hy; applyLang(el); }
  form.addEventListener('submit', function(e){
    e.preventDefault();
    var name = document.getElementById('f-name'), mail = document.getElementById('f-mail'), msg = document.getElementById('f-msg'), tel = document.getElementById('f-phone'), topic = document.getElementById('f-topic');
    if (!name.value.trim()) { setText('f-err', 'Գրեք ձեր անունը։'); name.focus(); return; }
    if (!/^\S+@\S+\.\S+$/.test(mail.value.trim())) { setText('f-err', 'Գրեք ճիշտ էլ․ փոստի հասցե, օրինակ՝ anun@mail.am'); mail.focus(); return; }
    if (msg.value.trim().length < 5) { setText('f-err', 'Գրեք մի քանի բառ ձեր հարցի մասին։'); msg.focus(); return; }
    err.textContent = '';
    var subject = tr(topic.value), body = subject + '\n' + name.value.trim() + '\n\n' + msg.value.trim();
    function show(sent){
      setText('done-h', sent ? 'Հարցումն ուղարկված է' : 'Հարցումը պատրաստ է');
      setText('done-p', sent ? 'Շուտով կպատասխանենք։' : 'Ուղարկեք այն մեզ ձեզ հարմար եղանակով։');
      document.getElementById('done-text').textContent = body;
      document.getElementById('done-text').hidden = sent; document.getElementById('done-wa').hidden = sent; document.getElementById('done-copy').hidden = sent;
      document.getElementById('done-wa').href = 'https://wa.me/' + WA + '?text=' + encodeURIComponent(body);
      form.hidden = true; done.hidden = false;
    }
    if (!FORM_ENDPOINT) { show(false); return; }
    fetch(FORM_ENDPOINT, { method: 'POST', headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' }, body: JSON.stringify({ name: name.value.trim(), email: mail.value.trim(), phone: tel.value.trim(), topic: subject, message: msg.value.trim() }) })
      .then(function(r){ if (!r.ok) throw new Error(); show(true); })
      .catch(function(){ setText('f-err', 'Չհաջողվեց ուղարկել։ Փորձեք WhatsApp-ով կամ զանգահարեք։'); });
  });
  document.getElementById('again').addEventListener('click', function(){ form.reset(); done.hidden = true; form.hidden = false; });
  document.getElementById('done-copy').addEventListener('click', function(){
    var b = this, el = document.getElementById('done-text');
    function ok(){ b.textContent = tr('Պատճենված է'); setTimeout(function(){ b.textContent = tr('Պատճենել տեքստը'); }, 1800); }
    function sel(){ var r = document.createRange(); r.selectNodeContents(el); var s2 = getSelection(); s2.removeAllRanges(); s2.addRange(r); }
    try { navigator.clipboard.writeText(el.textContent).then(ok, sel); } catch (x) { sel(); }
  });

  /* ask sheet */
  document.getElementById('ask-close').addEventListener('click', askClose);
  document.getElementById('ask').addEventListener('click', function(e){ if (e.target === this) askClose(); });
  document.addEventListener('keydown', function(e){ if (e.key === 'Escape' && !document.getElementById('ask').hidden) askClose(); });
  document.getElementById('ask-form').addEventListener('click', function(){ askClose(); toForm(askName); });
  ['ask-wa', 'ask-tg', 'ask-vb'].forEach(function(id){ document.getElementById(id).addEventListener('click', function(){ setTimeout(askClose, 200); }); });

''')
rep("      function ok(){ b.textContent = 'Պատճենված է'; setTimeout(function(){ b.textContent = 'Պատճենել'; }, 1800); }\n      function sel(){ var r = document.createRange(); r.selectNodeContents(el); var s = getSelection(); s.removeAllRanges(); s.addRange(r); b.textContent = 'Ընտրված է, պատճենեք'; }",
    "      function ok(){ b.textContent = tr('Պատճենված է'); setTimeout(function(){ b.textContent = tr('Պատճենել'); }, 1800); }\n      function sel(){ var r = document.createRange(); r.selectNodeContents(el); var s = getSelection(); s.removeAllRanges(); s.addRange(r); b.textContent = tr('Ընտրված է, պատճենեք'); }")
rep("    document.getElementById('gate-msg').textContent = 'Կայքը հասանելի է միայն 21 տարին լրացած անձանց։';", "    var gm = document.getElementById('gate-msg'); gm.textContent = 'Կայքը հասանելի է միայն 21 տարին լրացած անձանց։'; applyLang(gm);")

# ---------- router ----------
cut("  function view3d(id){", "  function buildCatalog(){", "")
rep("      card.querySelector('.cat-img').setAttribute('aria-label', 'Դիտել 3D-ով՝ ' + name);\n      card.querySelector('.cat-img').addEventListener('click', function(){ view3d(li.dataset.v); });",
    "      card.querySelector('.cat-img').setAttribute('aria-label', name);\n      card.querySelector('.cat-img').addEventListener('click', function(){ location.hash = '#p-' + li.dataset.v; });")
rep("      grid.appendChild(card);\n    });", "      grid.appendChild(card);\n    });\n    setTimeout(function(){ applyLang(catView); }, 0);")
rep("      b.innerHTML = f[1] + '<span>' + counts[f[0]] + '</span>';", "      b.innerHTML = '<i style=\"font-style:normal\"></i><span data-noi18n>' + counts[f[0]] + '</span>'; b.firstChild.textContent = f[1];")
rep("  function toMain(fn){ if (!SA.cat) { fn(); return; } afterMain = fn; location.hash = '#home'; }", "  function toMain(fn){ if (!SA.view || SA.view === 'main') { fn(); return; } afterMain = fn; location.hash = '#home'; }")
rep("    if (SA.cat) key = 'cat';", "    if (SA.view && SA.view !== 'main') key = 'cat';")
cut("  function route(){", "  window.addEventListener('hashchange', route);", r'''  var prodView = document.getElementById('product-view');
  function renderProduct(id){
    var d = PD[id], k = KIND[d.k], i = ORDER.indexOf(id), pv = ORDER[(i + ORDER.length - 1) % ORDER.length], nx = ORDER[(i + 1) % ORDER.length];
    function put(el, hy){ el.textContent = hy; }
    put(document.getElementById('p-kind'), k.cat); put(document.getElementById('p-name'), NAME[id]); put(document.getElementById('p-desc'), d.desc);
    var f = document.getElementById('p-facts'); f.innerHTML = '';
    d.facts.forEach(function(r){ var row = document.createElement('div'), dt = document.createElement('dt'), dd = document.createElement('dd'); dt.textContent = r[0]; dd.textContent = r[1]; row.appendChild(dt); row.appendChild(dd); f.appendChild(row); });
    put(document.getElementById('p-serve'), k.serve); put(document.getElementById('p-pair'), k.pair);
    var a = document.getElementById('p-prev'), b = document.getElementById('p-next');
    a.href = '#p-' + pv; put(a.querySelector('span'), NAME[pv]); b.href = '#p-' + nx; put(b.querySelector('span'), NAME[nx]);
    document.getElementById('p-ask').onclick = function(){ askFor(FULL[id]); };
    applyLang(prodView);
  }
  (function(){
    var z = document.getElementById('p-drag'), down = false, lx = 0;
    z.addEventListener('pointerdown', function(e){ down = true; lx = e.clientX; try { z.setPointerCapture(e.pointerId); } catch (x) {} document.getElementById('p-hint').classList.add('off'); });
    z.addEventListener('pointermove', function(e){ if (!down) return; if (SA.dragBy) SA.dragBy((e.clientX - lx) * 0.011); lx = e.clientX; });
    ['pointerup', 'pointercancel'].forEach(function(n){ z.addEventListener(n, function(){ down = false; }); });
  })();
  function parse(){
    var h = location.hash;
    if (h === '#catalog') return { v: 'cat', id: null };
    if (h.indexOf('#p-') === 0 && PD[h.slice(3)]) return { v: 'prod', id: h.slice(3) };
    return { v: 'main', id: null };
  }
  function route(){
    var r = parse(), prev = SA.view || 'main', prevId = SA.prod || null;
    if (r.v !== prev || r.id !== prevId) {
      if (prev === 'main') savedY = window.scrollY;
      SA.view = r.v; SA.cat = r.v === 'cat'; SA.prod = r.id;
      catView.hidden = r.v !== 'cat'; prodView.hidden = r.v !== 'prod'; mainEl.hidden = r.v !== 'main'; stageEl.hidden = r.v === 'cat';
      rail.classList.toggle('on', r.v === 'main' && SA.chapter > 0);
      if (r.v !== 'main') head.classList.remove('light');
      if (r.v === 'cat') buildCatalog();
      if (r.v === 'prod') renderProduct(r.id);
      if (window.ScrollTrigger) ScrollTrigger.refresh();
      setScroll(r.v === 'main' ? savedY : 0);
      if (r.v === 'cat') thumbs();
      if (SA.onProd && (prev === 'prod' || r.v === 'prod')) SA.onProd(SA.prod);
    }
    if (r.v === 'main' && afterMain) { var f = afterMain; afterMain = null; f(); }
    tabState();
  }
''')
rep("  initScroll();\n  route();", "  initScroll();\n  route();\n  setLang(LANG, true);")
open(p,'w',encoding='utf-8').write(s)
print('html ok')
