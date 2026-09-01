import fs from 'node:fs';
import path from 'node:path';

const [inputPath, rulesPath] = process.argv.slice(2);
if (!inputPath || !rulesPath || !fs.existsSync(inputPath) || !fs.existsSync(rulesPath)) {
  console.error('Usage: node tools/curate_v12.mjs <private-v12-html> <private-rules-json>');
  process.exit(1);
}

const rules = JSON.parse(fs.readFileSync(rulesPath, 'utf8'));
if (!Array.isArray(rules.replacements) || !Array.isArray(rules.blockedMarkers)) {
  throw new Error('Rules must define replacements and blockedMarkers arrays.');
}

let html = fs.readFileSync(inputPath, 'utf8');
const logoClass = 'brand' + 'Logo';
const logoPattern = new RegExp(`<img\\s+class="${logoClass}"[\\s\\S]*?>`, 'i');
html = html.replace(logoPattern, `<div class="${logoClass}" aria-label="Regional Sales Performance Analytics">RSP</div>`);
for (const rule of rules.replacements) html = html.split(rule.from).join(rule.to);
for (const marker of rules.blockedMarkers) {
  if (html.toLowerCase().includes(String(marker).toLowerCase())) throw new Error('A blocked publication marker remains.');
}
const embeddedImage = new RegExp('data:' + 'image|' + 'base' + '64,', 'i');
if (embeddedImage.test(html) || /[A-Z]:\\Users\\/i.test(html)) throw new Error('Embedded brand data or a private path remains.');
const block = html.match(/const\s+PAGE_META\s*=\s*\[([\s\S]*?)\];/);
const count = block ? (block[1].match(/^\s*\['/gm) || []).length : 0;
if (count !== 18) throw new Error(`Expected 18 PAGE_META entries, found ${count}.`);

const root = path.resolve(import.meta.dirname, '..');
const output = path.join(root, 'source', 'Regional_Sales_Performance_V12_PORTFOLIO.html');
fs.writeFileSync(output, html, 'utf8');
console.log(`Curated generalized V12 written with ${count} pages.`);
