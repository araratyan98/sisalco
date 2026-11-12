// Usage: node shot.js <html> <outdir> [mobile]
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
const T = __dirname, NM = path.join(T, 'node_modules');
const [,, file, outdir, mode] = process.argv;
fs.mkdirSync(outdir, { recursive: true });
const mime = { '.js': 'text/javascript', '.mjs': 'text/javascript', '.woff2': 'font/woff2', '.css': 'text/css' };
function fontCss() {
  let css = '';
  for (const [fam, pkg] of [['Noto Serif Armenian', 'noto-serif-armenian'], ['Noto Sans Armenian', 'noto-sans-armenian']])
    for (const w of [400, 500, 600])
      for (const sub of ['armenian', 'latin'])
        css += `@font-face{font-family:'${fam}';font-weight:${w};font-style:normal;src:url(https://fonts.gstatic.com/${pkg}/${pkg}-${sub}-${w}-normal.woff2) format('woff2');${sub === 'armenian' ? 'unicode-range:U+0308,U+0530-058F,U+2010,U+2024,U+25CC,U+FB13-FB17;' : 'unicode-range:U+0000-00FF,U+2000-206F;'}}\n`;
  return css;
}
(async () => {
  const browser = await chromium.launch({ args: ['--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist'] });
  const mobile = mode === 'mobile';
  const ctx = await browser.newContext({ viewport: mobile ? { width: 400, height: 800 } : { width: 1440, height: 860 }, deviceScaleFactor: 1 });
  const page = await ctx.newPage();
  const errs = [];
  page.on('console', (m) => { if (m.type() === 'error') errs.push(m.text()); });
  page.on('pageerror', (e) => errs.push('PAGEERROR ' + e.message));
  await page.route('**/*', (route) => {
    const u = route.request().url();
    let m;
    if (u.startsWith('http://local/tex/')) return route.fulfill({ contentType: 'image/jpeg', body: fs.readFileSync(path.join(path.dirname(path.resolve(file)), u.replace('http://local/', ''))) });
    if (u === 'http://local/logo.png') return route.fulfill({ contentType: 'image/png', body: fs.readFileSync(path.join(path.dirname(path.resolve(file)), 'logo.png')) });
    if (u === 'http://local/') {
      const html = fs.readFileSync(file, 'utf8');
      return route.fulfill({ contentType: 'text/html; charset=utf-8', body: '<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><style>body{margin:0;font:14px system-ui}img{max-width:100%}[hidden]{display:none!important}</style></head><body>' + html + '</body></html>' });
    }
    if (u.includes('fonts.googleapis.com')) return route.fulfill({ contentType: 'text/css', body: fontCss() });
    if ((m = u.match(/fonts\.gstatic\.com\/([^/]+)\/(.+)$/))) return route.fulfill({ contentType: 'font/woff2', body: fs.readFileSync(path.join(NM, '@fontsource', m[1], 'files', m[2])) });
    if ((m = u.match(/cdn\.jsdelivr\.net\/npm\/three@[\d.]+\/(.+)$/))) return route.fulfill({ contentType: 'text/javascript', body: fs.readFileSync(path.join(NM, 'three', m[1])) });
    if ((m = u.match(/cdnjs\.cloudflare\.com\/ajax\/libs\/gsap\/[\d.]+\/(.+)$/))) return route.fulfill({ contentType: 'text/javascript', body: fs.readFileSync(path.join(NM, 'gsap/dist', m[1])) });
    if ((m = u.match(/cdn\.jsdelivr\.net\/npm\/lenis@[\d.]+\/dist\/(.+)$/))) return route.fulfill({ contentType: 'text/javascript', body: fs.readFileSync(path.join(NM, 'lenis/dist', m[1])) });
    console.log('BLOCKED', u); return route.abort();
  });
  await page.goto('http://local/');
  await page.waitForTimeout(2500);
  await page.screenshot({ path: path.join(outdir, '00-gate.png') });
  await page.click('#gate-yes').catch(() => {});
  await page.waitForTimeout(process.env.CAT ? 3000 : 7000);
  await page.screenshot({ path: path.join(outdir, '01-hero.png') });
  if (process.env.PROD) {
    await page.evaluate((h) => { location.hash = h; }, process.env.PROD); await page.waitForTimeout(9000);
    await page.screenshot({ path: path.join(outdir, 'prod.png') });
    await page.click('.lang button[data-l=ru]'); await page.waitForTimeout(3500); await page.screenshot({ path: path.join(outdir, 'prod-ru.png') });
    await page.click('#p-ask'); await page.waitForTimeout(700); await page.screenshot({ path: path.join(outdir, 'ask.png') }); await page.click('#ask-close');
    await page.evaluate(() => { location.hash = '#home'; }); await page.waitForTimeout(3000); await page.click('.lang button[data-l=en]'); await page.waitForTimeout(3500);
    await page.screenshot({ path: path.join(outdir, 'home-en.png') });
    console.log('errors', JSON.stringify(errs.slice(0, 8))); await browser.close(); return;
  }
  if (process.env.CAT) {
    await page.evaluate(() => { location.hash = '#catalog'; });
    await page.waitForTimeout(+process.env.CAT);
    await page.screenshot({ path: path.join(outdir, 'cat.png'), fullPage: !mobile });
    if (mobile) { await page.evaluate(() => scrollTo(0, 500)); await page.waitForTimeout(500); await page.screenshot({ path: path.join(outdir, 'cat2.png') }); }
    await page.evaluate(() => { location.hash = '#home'; }); await page.waitForTimeout(1500);
    const a = await page.evaluate(() => document.getElementById('about').getBoundingClientRect().top + scrollY);
    await page.evaluate((yy) => { if (window.SA && SA.lenis) SA.lenis.scrollTo(yy, { immediate: true }); else scrollTo(0, yy); }, a - 40);
    await page.waitForTimeout(2500); await page.screenshot({ path: path.join(outdir, 'about.png') });
    console.log('errors', JSON.stringify(errs.slice(0, 8))); await browser.close(); return;
  }
  const stops = await page.evaluate(() => {
    const ids = ['m-show', 'ch-1', 'ch-2', 'ch-3', 'ch-4', 'band', 'about', 'partners', 'contact'];
    return ids.map((id) => { const el = document.getElementById(id); return el && el.offsetHeight ? [id, el.getBoundingClientRect().top + scrollY] : null; }).filter(Boolean);
  });
  let i = 2;
  for (const [id, y] of stops) {
    await page.evaluate((yy) => { if (window.SA && SA.lenis) SA.lenis.scrollTo(yy, { immediate: true }); else scrollTo(0, yy); }, y + (id.startsWith('ch') ? 60 : 0));
    await page.waitForTimeout(id.startsWith("ch") ? 2500 : 2500);
    await page.screenshot({ path: path.join(outdir, String(i++).padStart(2, '0') + '-' + id + '.png') });
    if (id === 'ch-1' && process.env.VARIANTS) for (const v of (process.env.VARIANTS === '1' ? ['krunk-white', 'krunk-rose'] : ['krunk-white'])) {
      await page.click('#ch-1 li[data-v=' + v + '] .nm'); await page.waitForTimeout(10000);
      await page.screenshot({ path: path.join(outdir, '02-' + v + '.png') });
    }
    if (id === 'm-show') {
      await page.waitForTimeout(7000); await page.screenshot({ path: path.join(outdir, 'm1.png') });
      await page.click('#m-next'); await page.click('#m-next'); await page.waitForTimeout(9000); await page.screenshot({ path: path.join(outdir, 'm2.png') });
      await page.click('#m-tabs button:nth-child(4)'); await page.waitForTimeout(11000); await page.screenshot({ path: path.join(outdir, 'm3.png') });
    }
    if (process.env.ONLY && id === process.env.ONLY) break;
  }
  const ov = await page.evaluate(() => document.documentElement.scrollWidth - innerWidth);
  console.log('overflowX', ov, 'errors', JSON.stringify(errs.slice(0, 8)));
  await browser.close();
})();
