const { chromium } = require('playwright'); const fs=require('fs'), path=require('path');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:400,height:800}});
await p.route('**/*',r=>{const u=r.request().url(); if(u==='http://local/') return r.fulfill({contentType:'text/html; charset=utf-8',body:'<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><style>body{margin:0}[hidden]{display:none!important}</style></head><body>'+fs.readFileSync('../web/sis-alco.html','utf8')+'</body></html>'});
 const m=u.match(/cdnjs\.cloudflare\.com\/ajax\/libs\/gsap\/[\d.]+\/(.+)$/); if(m) return r.fulfill({contentType:'text/javascript',body:fs.readFileSync(path.join('node_modules/gsap/dist',m[1]))}); r.abort();});
await p.goto('http://local/'); await p.waitForTimeout(600); await p.click('#gate-yes'); await p.waitForTimeout(2500);
const top=await p.evaluate(()=>document.getElementById('m-show').getBoundingClientRect().top+scrollY);
for (const d of [-120, 90, -300, 330]) { await p.evaluate(y=>scrollTo(0,y), top+d); await p.waitForTimeout(1500); console.log(d, 'settled offset', await p.evaluate(()=>Math.round(document.getElementById('m-show').getBoundingClientRect().top))); }
await b.close()})();
