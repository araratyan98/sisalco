const { chromium } = require('playwright'); const fs=require('fs');
(async()=>{const b=await chromium.launch();
for (const [w,h,n] of [[400,800,'m'],[1440,860,'d']]) { const p=await b.newPage({viewport:{width:w,height:h}}); const errs=[]; p.on('pageerror',e=>errs.push(e.message));
await p.route('**/*',r=>{const u=r.request().url(); if(u==='http://local/') return r.fulfill({contentType:'text/html; charset=utf-8',body:'<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><style>body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style></head><body>'+fs.readFileSync('../web/sis-alco.html','utf8')+'</body></html>'});
 if(u==='http://local/logo.png') return r.fulfill({contentType:'image/png',body:fs.readFileSync('../web/logo.png')}); if(u.startsWith('http://local/ph/')) return r.fulfill({contentType:'image/jpeg',body:fs.readFileSync('../web/'+u.slice(13))}); r.abort();});
await p.goto('http://local/'); await p.waitForTimeout(500); await p.click('#gate-yes'); await p.waitForTimeout(800);
await p.evaluate((id)=>{document.getElementById('gate').hidden=true; scrollTo(0, document.getElementById(id).getBoundingClientRect().top+scrollY)}, process.env.SEC||'about'); await p.waitForTimeout(500);
await (await p.$('#'+(process.env.SEC||'about'))).screenshot({path:'low-'+n+'.png'});

console.log(n,'overflow',await p.evaluate(()=>document.documentElement.scrollWidth-innerWidth), errs); await p.close(); }
await b.close()})();
