const { chromium } = require('playwright'); const fs=require('fs'), path=require('path');
const NM=path.join(__dirname,'node_modules'); const mode=process.argv[2];
(async()=>{const b=await chromium.launch({ args: ['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist'] });
const p=await b.newPage({viewport: mode==='m'?{width:400,height:800}:{width:1440,height:860}}); const errs=[]; p.on('pageerror',e=>errs.push(e.message)); p.on('console',m=>{if(m.type()==='error')errs.push(m.text())});
await p.route('**/*',r=>{const u=r.request().url(); let m;
 if(u==='http://local/') return r.fulfill({contentType:'text/html; charset=utf-8',body:'<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><style>body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style></head><body>'+fs.readFileSync('../web/sis-alco.html','utf8')+'</body></html>'});
 if(u.startsWith('http://local/')) { const f='../web/'+u.slice(13); return fs.existsSync(f)?r.fulfill({contentType:f.endsWith('png')?'image/png':'image/jpeg',body:fs.readFileSync(f)}):r.abort(); }
 if((m=u.match(/cdn\.jsdelivr\.net\/npm\/three@[\d.]+\/(.+)$/))) return r.fulfill({contentType:'text/javascript',body:fs.readFileSync(path.join(NM,'three',m[1]))});
 if((m=u.match(/cdnjs\.cloudflare\.com\/ajax\/libs\/gsap\/[\d.]+\/(.+)$/))) return r.fulfill({contentType:'text/javascript',body:fs.readFileSync(path.join(NM,'gsap/dist',m[1]))});
 if((m=u.match(/cdn\.jsdelivr\.net\/npm\/lenis@[\d.]+\/dist\/(.+)$/))) return r.fulfill({contentType:'text/javascript',body:fs.readFileSync(path.join(NM,'lenis/dist',m[1]))});
 r.abort();});
await p.goto('http://local/'); await p.waitForTimeout(2500); await p.click('#gate-yes');
await p.waitForTimeout(16000); await p.evaluate(()=>{location.hash='#catalog'}); await p.waitForTimeout(25000); await p.click('.cat-card[data-id="fayton"] .cat-img'); await p.waitForTimeout(12000); await p.screenshot({path:'flow-'+mode+'1.png'}); await p.evaluate(()=>{location.hash='#home'}); await p.waitForTimeout(9000); await p.screenshot({path:'flow-'+mode+'2.png'}); console.log(await p.evaluate(()=>{const c=document.querySelector('#stage canvas');return [c.width,c.height,location.hash]}));
console.log('intro class', await p.evaluate(()=>document.documentElement.className), 'scrollLocked', await p.evaluate(()=>document.body.style.overflow), errs.slice(0,5));
await b.close()})();
