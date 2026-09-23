import fs from 'fs';
import path from 'path';

const DIST_DIR = path.join(process.cwd(), 'dist');

const BANNED_PHRASES = [
  "24/7",
  "free estimate",
  "free quote",
  "guaranteed",
  "our technicians",
  "licensed",
  "insured",
  "same-day",
  "max_cpl",
  "lowest price",
  "#1",
  "placeholder"
];

// If site.ts is empty, "tel:" with no number might be rendered, or we might see a fake one. 
// We should check that tel:1-800 does not exist unless it's intended. 
// But actually, the code currently produces no `tel:` if the number is blank, so we just ban `tel:` for now to ensure no hardcoded numbers exist.
const BANNED_PATTERNS = [
  /tel:\d/, // Banning hardcoded phone numbers in hrefs for now
];

let errors = [];
let htmlFiles = [];

function walkDir(dir) {
  const files = fs.readdirSync(dir);
  for (const file of files) {
    const fullPath = path.join(dir, file);
    if (fs.statSync(fullPath).isDirectory()) {
      walkDir(fullPath);
    } else if (fullPath.endsWith('.html')) {
      htmlFiles.push(fullPath);
    }
  }
}

walkDir(DIST_DIR);

if (htmlFiles.length === 0) {
  console.error("No HTML files found in dist/. Did the build fail?");
  process.exit(1);
}

const seoSets = {
  titles: new Set(),
  descriptions: new Set(),
  canonicals: new Set()
};

let paPilotCityCount = 0;

for (const file of htmlFiles) {
  const content = fs.readFileSync(file, 'utf-8');
  const lowerContent = content.toLowerCase();
  
  const relPath = path.relative(DIST_DIR, file);

  // 1. Check SEO Tags
  const titleMatch = content.match(/<title>(.*?)<\/title>/);
  if (!titleMatch || !titleMatch[1].trim()) errors.push(`[${relPath}] Missing or empty <title>`);
  
  const descMatch = content.match(/<meta\s+name="description"\s+content="([^"]+)"/);
  if (!descMatch || !descMatch[1].trim()) errors.push(`[${relPath}] Missing or empty meta description`);
  
  const h1Match = content.match(/<h1[^>]*>(.*?)<\/h1>/i);
  if (!h1Match || !h1Match[1].trim()) errors.push(`[${relPath}] Missing or empty <h1>`);
  
  const canonicalMatch = content.match(/<link\s+rel="canonical"\s+href="([^"]+)"/);
  if (!canonicalMatch || !canonicalMatch[1].trim()) errors.push(`[${relPath}] Missing or empty canonical tag`);

  // Track Uniqueness (Skip home and hub pages for uniqueness check as they might overlap with pagination later, but for now just check exact duplication)
  if (titleMatch) {
    if (seoSets.titles.has(titleMatch[1])) errors.push(`[${relPath}] Duplicate title found: ${titleMatch[1]}`);
    seoSets.titles.add(titleMatch[1]);
  }
  if (descMatch) {
    if (seoSets.descriptions.has(descMatch[1])) errors.push(`[${relPath}] Duplicate description found.`);
    seoSets.descriptions.add(descMatch[1]);
  }
  if (canonicalMatch) {
    if (seoSets.canonicals.has(canonicalMatch[1])) errors.push(`[${relPath}] Duplicate canonical URL found: ${canonicalMatch[1]}`);
    seoSets.canonicals.add(canonicalMatch[1]);
  }

  // 2. Check Banned Phrases
  for (const phrase of BANNED_PHRASES) {
    if (lowerContent.includes(phrase)) {
      errors.push(`[${relPath}] Contains banned phrase: "${phrase}"`);
    }
  }

  for (const pattern of BANNED_PATTERNS) {
    if (pattern.test(content)) {
      errors.push(`[${relPath}] Contains banned pattern: ${pattern.toString()}`);
    }
  }

  // 3. Image Alt Tags and Src Check
  const imgTags = content.match(/<img[^>]+>/g) || [];
  for (const img of imgTags) {
    if (!img.includes('alt=')) {
      errors.push(`[${relPath}] Image missing alt attribute: ${img}`);
    } else {
      const altMatch = img.match(/alt="([^"]*)"/);
      if (!altMatch || altMatch[1].trim() === "") {
        errors.push(`[${relPath}] Image has empty alt attribute: ${img}`);
      }
    }
    
    // Check if the source file actually exists in the build output
    const srcMatch = img.match(/src="([^"]+)"/);
    if (srcMatch && srcMatch[1]) {
      const imgSrc = srcMatch[1];
      // Skip external URLs
      if (!imgSrc.startsWith('http')) {
        const localImgPath = path.join(DIST_DIR, imgSrc);
        if (!fs.existsSync(localImgPath)) {
          errors.push(`[${relPath}] Broken image link: ${imgSrc} does not exist in dist/`);
        }
      }
    }
  }

  // 4. Internal Link Check
  const linkTags = content.match(/<a[^>]+href="([^"]+)"/g) || [];
  for (const aTag of linkTags) {
    const hrefMatch = aTag.match(/href="([^"]+)"/);
    if (hrefMatch && hrefMatch[1]) {
      let href = hrefMatch[1];
      
      // Ignore external, tel, mailto, anchor links
      if (href.startsWith('http') || href.startsWith('tel:') || href.startsWith('mailto:') || href.startsWith('#')) {
        continue;
      }

      // Check if internal route exists
      // Convert to file path. e.g. /services/ -> dist/services/index.html or dist/services.html
      let checkPath = href.split('#')[0].split('?')[0];
      if (checkPath.endsWith('/')) {
        checkPath += 'index.html';
      } else if (!checkPath.endsWith('.html') && !checkPath.endsWith('.xml')) {
        checkPath += '/index.html';
      }
      
      // Remove leading slash
      if (checkPath.startsWith('/')) {
        checkPath = checkPath.substring(1);
      }

      const fullCheckPath = path.join(DIST_DIR, checkPath);
      if (!fs.existsSync(fullCheckPath)) {
        errors.push(`[${relPath}] Broken internal link: ${href} (checked ${checkPath})`);
      }
    }
  }

}

  console.log(`Generated HTML files: ${htmlFiles.length}`);

  // We expect a larger number now. For 199 locations * 7 services = 1393 pages + hubs + national = ~1400+.
  if (htmlFiles.length < 1300) {
    errors.push(`[PAGE COUNT] Expected ~1400 pages for the full rollout, but found ${htmlFiles.length}.`);
  } else {
    console.log(`Verified large-scale production page count (${htmlFiles.length} pages generated).`);
  }

if (errors.length > 0) {
  console.error("QA Validation FAILED with the following errors:\n");
  errors.forEach(e => console.error(e));
  process.exit(1);
} else {
  console.log(`QA Validation PASSED! Scanned ${htmlFiles.length} pages.`);
  process.exit(0);
}
