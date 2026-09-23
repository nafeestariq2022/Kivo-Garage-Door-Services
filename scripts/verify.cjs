const fs = require('fs');
const path = require('path');
const dist = path.join(process.cwd(), 'dist');

// 1. Gather all HTML files
const htmlFiles = [];
function walk(dir) {
  const files = fs.readdirSync(dir);
  for (const file of files) {
    const fullPath = path.join(dir, file);
    if (fs.statSync(fullPath).isDirectory()) {
      walk(fullPath);
    } else if (fullPath.endsWith('.html')) {
      htmlFiles.push(fullPath);
    }
  }
}
walk(dist);
console.log('Total HTML files:', htmlFiles.length);

// 2. Count local pages
let localPages = 0;
let hubPages = 0; // /, /about, /contact, /privacy, /terms, /services/
let nationalServicePages = 0; // /services/garage-door-repair
let stateHubs = 0; // /pa/
for (const file of htmlFiles) {
  const rel = path.relative(dist, file).replace(/\\/g, '/');
  if (rel === 'index.html' || rel === 'about/index.html' || rel === 'contact/index.html' || rel === 'privacy-policy/index.html' || rel === 'terms/index.html' || rel === 'services/index.html') {
    hubPages++;
  } else if (rel.startsWith('services/') && rel !== 'services/index.html') {
    nationalServicePages++; 
  } else if (rel.endsWith('/index.html') && rel.split('/').length === 2) {
    stateHubs++; 
  } else {
    localPages++;
  }
}
console.log('Local Pages:', localPages);
console.log('Hub Pages:', hubPages);
console.log('National Service Pages:', nationalServicePages);
console.log('State Hubs:', stateHubs);

// 3. Sitemap URL Count
const sitemapPath = path.join(dist, 'sitemap-0.xml');
if (fs.existsSync(sitemapPath)) {
  const sitemap = fs.readFileSync(sitemapPath, 'utf8');
  const urls = sitemap.match(/<url>/g);
  console.log('Sitemap URLs:', urls ? urls.length : 0);
} else {
  console.log('Sitemap not found!');
}

// 4. Internal Data Leakage
const leaks = ['LeadSmart', 'Ringba', 'CPL', 'payout', 'buyer', 'routing', 'campaign', 'placeholder'];
let leakFound = false;
for (const file of htmlFiles) {
  const content = fs.readFileSync(file, 'utf8');
  for (const leak of leaks) {
    if (content.toLowerCase().includes(leak.toLowerCase())) {
      console.log('Leak found:', leak, 'in', file);
      leakFound = true;
    }
  }
}
if (!leakFound) console.log('No internal data leakage found.');

// 5. Test content differentiation
try {
  const sample1 = fs.readFileSync(path.join(dist, 'tx/garage-door-repair-plano/index.html'), 'utf8');
  const sample2 = fs.readFileSync(path.join(dist, 'tx/garage-door-repair-dallas/index.html'), 'utf8');
  const h1Match = /<h1[^>]*>(.*?)<\/h1>/i;
  console.log('TX Plano H1:', sample1.match(h1Match)[1]);
  console.log('TX Dallas H1:', sample2.match(h1Match)[1]);
} catch(e) {
  console.log("Error comparing files: " + e.message);
}
