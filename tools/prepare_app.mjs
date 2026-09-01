import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';

const root = path.resolve(import.meta.dirname, '..');
const source = path.join(root, 'source', 'Regional_Sales_Performance_V12_PORTFOLIO.html');
if (!fs.existsSync(source)) throw new Error(`Portfolio V12 source not found: ${source}`);
const appDir = path.join(root, 'app');
const vendorDir = path.join(appDir, 'vendor');
fs.mkdirSync(vendorDir, { recursive: true });
const dependencies = [
  ['xlsx-js-style', 'dist/xlsx.bundle.js', 'xlsx.bundle.js'],
  ['chart.js', 'dist/chart.umd.js', 'chart.umd.js'],
  ['chartjs-plugin-datalabels', 'dist/chartjs-plugin-datalabels.js', 'chartjs-plugin-datalabels.js']
];
for (const [packageName, relativePath, outputName] of dependencies) {
  const installed = path.join(root, 'node_modules', packageName, relativePath);
  const existing = path.join(vendorDir, outputName);
  if (fs.existsSync(installed)) fs.copyFileSync(installed, existing);
  else if (!fs.existsSync(existing)) throw new Error(`Missing ${outputName}; run npm ci first.`);
}
let html = fs.readFileSync(source, 'utf8');
const replacements = [
  [/https:\/\/cdn\.jsdelivr\.net\/npm\/xlsx-js-style@1\.2\.0\/dist\/xlsx\.bundle\.js/g, 'vendor/xlsx.bundle.js'],
  [/https:\/\/cdn\.jsdelivr\.net\/npm\/chart\.js@4\.4\.1\/dist\/chart\.umd\.min\.js/g, 'vendor/chart.umd.js'],
  [/https:\/\/cdn\.jsdelivr\.net\/npm\/chartjs-plugin-datalabels@2\.2\.0(?:\/dist\/chartjs-plugin-datalabels(?:\.min)?\.js)?/g, 'vendor/chartjs-plugin-datalabels.js']
];
for (const [pattern, replacement] of replacements) html = html.replace(pattern, replacement);
if (/cdn\.jsdelivr\.net\/npm\/(?:xlsx-js-style|chart\.js|chartjs-plugin-datalabels)/.test(html)) throw new Error('Required CDN dependency remains.');
const safeArea = `<style id="portfolio-desktop-safe-area">
@media (min-width:981px){.sidebar{padding-bottom:120px!important;scroll-padding-bottom:120px!important}.nav{padding-bottom:90px!important}.main{padding-bottom:150px!important}.page{padding-bottom:80px!important}.page>*:last-child{margin-bottom:36px!important}}
@media (max-width:980px){.main{padding-bottom:120px!important}.page{padding-bottom:70px!important}.sidebar{padding-bottom:70px!important}}
</style>`;
html = html.replace(/<style id="portfolio-desktop-safe-area">[\s\S]*?<\/style>/gi, '').replace(/<\/head>/i, `${safeArea}\n</head>`);
fs.writeFileSync(path.join(appDir, 'index.html'), html, 'utf8');
const pageBlock = html.match(/const\s+PAGE_META\s*=\s*\[([\s\S]*?)\];/);
const pageCount = pageBlock ? (pageBlock[1].match(/^\s*\['/gm) || []).length : 0;
const sha256 = value => crypto.createHash('sha256').update(value).digest('hex');
fs.writeFileSync(path.join(appDir, 'generation-manifest.json'), JSON.stringify({
  sourceSha256: sha256(fs.readFileSync(source)),
  appSha256: sha256(Buffer.from(html, 'utf8')),
  pageCount,
  version: '1.0.2'
}, null, 2) + '\n');
console.log('Generated offline app/index.html from the generalized portfolio V12 source.');
