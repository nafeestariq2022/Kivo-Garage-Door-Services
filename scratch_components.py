import os

components_dir = 'src/components'
ui_dir = 'src/components/ui'
layouts_dir = 'src/layouts'
content_dir = 'src/content'

os.makedirs(ui_dir, exist_ok=True)
os.makedirs(layouts_dir, exist_ok=True)
os.makedirs(content_dir, exist_ok=True)

files = {}

# ----------------- UI COMPONENTS -----------------

files[f'{ui_dir}/Container.astro'] = """---
interface Props {
  class?: string;
}
const { class: className = '' } = Astro.props;
---
<div class={`w-full max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 ${className}`}>
  <slot />
</div>
"""

files[f'{ui_dir}/Section.astro'] = """---
interface Props {
  class?: string;
  id?: string;
  bg?: 'alabaster' | 'surface' | 'charcoal';
}
const { class: className = '', id, bg = 'alabaster' } = Astro.props;
const bgClass = bg === 'charcoal' ? 'bg-brand-charcoal text-brand-alabaster' : bg === 'surface' ? 'bg-brand-surface' : 'bg-brand-alabaster';
---
<section id={id} class={`py-20 md:py-32 ${bgClass} ${className}`}>
  <slot />
</section>
"""

files[f'{ui_dir}/Button.astro'] = """---
interface Props {
  href?: string;
  variant?: 'primary' | 'secondary' | 'outline';
  class?: string;
  type?: 'button' | 'submit';
}
const { href, variant = 'primary', class: className = '', type = 'button' } = Astro.props;

const baseStyles = "inline-flex items-center justify-center px-8 py-4 font-sans font-semibold tracking-wide transition-colors duration-200 border-2 rounded-sm focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-brand-charcoal";
const variants = {
  primary: "bg-brand-charcoal text-brand-alabaster border-brand-charcoal hover:bg-brand-accent hover:border-brand-accent",
  secondary: "bg-brand-accent text-white border-brand-accent hover:bg-brand-charcoal hover:border-brand-charcoal",
  outline: "bg-transparent text-brand-charcoal border-brand-charcoal hover:bg-brand-charcoal hover:text-brand-alabaster",
};

const classes = `${baseStyles} ${variants[variant]} ${className}`;
---
{href ? (
  <a href={href} class={classes}>
    <slot />
  </a>
) : (
  <button type={type} class={classes}>
    <slot />
  </button>
)}
"""

files[f'{ui_dir}/PhoneCTA.astro'] = """---
import Button from './Button.astro';
interface Props {
  phone: string;
  label?: string;
  class?: string;
}
const { phone, label = "Call Now", class: className = '' } = Astro.props;
const cleanPhone = phone.replace(/[^\d+]/g, '');
---
<Button href={`tel:${cleanPhone}`} variant="secondary" class={className}>
  {label}: {phone}
</Button>
"""

files[f'{ui_dir}/Breadcrumbs.astro'] = """---
interface Crumb {
  label: string;
  href?: string;
}
interface Props {
  crumbs: Crumb[];
}
const { crumbs } = Astro.props;
---
<nav aria-label="Breadcrumb" class="mb-8">
  <ol class="flex items-center space-x-2 text-sm text-gray-600 font-sans">
    <li>
      <a href="/" class="hover:text-brand-accent focus:outline-none focus:underline">Home</a>
    </li>
    {crumbs.map((crumb, i) => (
      <li class="flex items-center space-x-2">
        <span class="text-gray-400">/</span>
        {crumb.href && i !== crumbs.length - 1 ? (
          <a href={crumb.href} class="hover:text-brand-accent focus:outline-none focus:underline">{crumb.label}</a>
        ) : (
          <span class="text-brand-charcoal font-medium" aria-current="page">{crumb.label}</span>
        )}
      </li>
    ))}
  </ol>
</nav>
"""

# ----------------- MACRO COMPONENTS -----------------

files[f'{components_dir}/SEO.astro'] = """---
interface Props {
  title: string;
  description: string;
  canonical?: string;
  type?: 'website' | 'article';
  image?: string;
  noindex?: boolean;
}
const { title, description, canonical, type = 'website', image, noindex = false } = Astro.props;
const siteUrl = 'https://kivogaragedoorservices.us';
const canonicalUrl = canonical ? new URL(canonical, siteUrl).toString() : new URL(Astro.url.pathname, siteUrl).toString();
const ogImage = image ? new URL(image, siteUrl).toString() : new URL('/og-image.jpg', siteUrl).toString();
---
<title>{title}</title>
<meta name="description" content={description} />
<link rel="canonical" href={canonicalUrl} />
{noindex && <meta name="robots" content="noindex, nofollow" />}
{!noindex && <meta name="robots" content="index, follow" />}

<meta property="og:title" content={title} />
<meta property="og:description" content={description} />
<meta property="og:type" content={type} />
<meta property="og:url" content={canonicalUrl} />
<meta property="og:image" content={ogImage} />
<meta property="og:site_name" content="Kivo Garage Door Services" />

<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content={title} />
<meta name="twitter:description" content={description} />
<meta name="twitter:image" content={ogImage} />
"""

files[f'{components_dir}/Header.astro'] = """---
import PhoneCTA from './ui/PhoneCTA.astro';
---
<header class="w-full bg-brand-alabaster border-b-2 border-brand-surface sticky top-0 z-50">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-20 flex items-center justify-between">
    <div class="flex-shrink-0">
      <a href="/" class="text-2xl font-heading font-bold text-brand-charcoal focus:outline-none focus:ring-2 focus:ring-brand-accent">
        KIVO<span class="text-brand-accent">.</span>
      </a>
    </div>
    <nav class="hidden md:flex items-center space-x-8 font-sans font-medium text-brand-charcoal">
      <a href="/services" class="hover:text-brand-accent transition-colors">Services</a>
      <a href="/locations" class="hover:text-brand-accent transition-colors">Locations</a>
      <a href="/about" class="hover:text-brand-accent transition-colors">About</a>
    </nav>
    <div class="hidden md:flex">
      <PhoneCTA phone="1-800-555-0199" label="24/7 Service" />
    </div>
    <!-- Mobile menu button placeholder -->
    <div class="md:hidden">
      <button aria-label="Menu" class="text-brand-charcoal p-2 focus:outline-none">
        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="square" stroke-linejoin="miter" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path></svg>
      </button>
    </div>
  </div>
</header>
"""

files[f'{components_dir}/Footer.astro'] = """---
const year = new Date().getFullYear();
---
<footer class="bg-brand-charcoal text-brand-surface py-16">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 grid grid-cols-1 md:grid-cols-3 gap-12">
    <div>
      <a href="/" class="text-2xl font-heading font-bold text-brand-alabaster">KIVO<span class="text-brand-accent">.</span></a>
      <p class="mt-4 font-sans text-gray-400">Premium architectural garage door services nationwide.</p>
    </div>
    <div>
      <h3 class="font-heading text-xl font-bold text-brand-alabaster mb-4">Core Services</h3>
      <ul class="space-y-2 font-sans text-gray-400">
        <li><a href="/garage-door-repair" class="hover:text-brand-accent">Repair</a></li>
        <li><a href="/garage-door-installation" class="hover:text-brand-accent">Installation</a></li>
        <li><a href="/garage-door-opener-repair" class="hover:text-brand-accent">Opener Service</a></li>
      </ul>
    </div>
    <div>
      <h3 class="font-heading text-xl font-bold text-brand-alabaster mb-4">Legal</h3>
      <ul class="space-y-2 font-sans text-gray-400">
        <li><a href="/privacy-policy" class="hover:text-brand-accent">Privacy Policy</a></li>
        <li><a href="/terms" class="hover:text-brand-accent">Terms of Service</a></li>
      </ul>
    </div>
  </div>
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 mt-16 pt-8 border-t border-gray-800 text-sm text-gray-500 font-sans">
    &copy; {year} Kivo Garage Door Services. All rights reserved.
  </div>
</footer>
"""

files[f'{components_dir}/Hero.astro'] = """---
import Button from './ui/Button.astro';
import Container from './ui/Container.astro';

interface Props {
  headline: string;
  subheadline: string;
  primaryCtaText: string;
  primaryCtaHref: string;
  imageSrc: string;
  imageAlt: string;
}
const { headline, subheadline, primaryCtaText, primaryCtaHref, imageSrc, imageAlt } = Astro.props;
---
<section class="relative w-full bg-brand-alabaster pt-12 pb-20 lg:pt-24 lg:pb-32 overflow-hidden">
  <Container class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
    <!-- Asymmetrical Left: Typography -->
    <div class="lg:col-span-5 z-10">
      <h1 class="text-5xl lg:text-7xl font-heading font-bold text-brand-charcoal leading-[1.1] uppercase tracking-tight">
        {headline}
      </h1>
      <p class="mt-6 text-lg lg:text-xl font-sans text-gray-700 leading-relaxed max-w-lg">
        {subheadline}
      </p>
      <div class="mt-10 flex flex-col sm:flex-row gap-4">
        <Button href={primaryCtaHref}>{primaryCtaText}</Button>
      </div>
      <div class="mt-8 flex items-center gap-4 text-sm font-sans font-medium text-gray-600 uppercase tracking-widest">
        <span>Licensed</span>
        <span class="w-1 h-1 bg-brand-accent rounded-sm"></span>
        <span>Insured</span>
        <span class="w-1 h-1 bg-brand-accent rounded-sm"></span>
        <span>Guaranteed</span>
      </div>
    </div>
    
    <!-- Asymmetrical Right: Image (No Dark Overlay) -->
    <div class="lg:col-span-7 relative">
      <div class="aspect-w-4 aspect-h-3 lg:aspect-w-16 lg:aspect-h-11">
        <img src={imageSrc} alt={imageAlt} class="object-cover w-full h-full rounded-sm shadow-xl" loading="eager" />
      </div>
      <!-- Decorative strict geometry element -->
      <div class="absolute -bottom-6 -left-6 w-32 h-32 border-l-4 border-b-4 border-brand-accent hidden lg:block"></div>
    </div>
  </Container>
</section>
"""

# ----------------- CONTENT ARCHITECTURE -----------------

files[f'{content_dir}/config.ts'] = """import { defineCollection, z } from 'astro:content';

const services = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    description: z.string(),
    shortDescription: z.string(),
    isPriority: z.boolean().default(false),
  }),
});

const locations = defineCollection({
  type: 'data',
  schema: z.object({
    city: z.string(),
    state: z.string(),
    stateSlug: z.string(),
    citySlug: z.string(),
    zips: z.array(z.string()),
    population: z.number().optional(),
    maxCpl: z.number(),
    status: z.enum(['candidate', 'approved', 'priority', 'indexable', 'excluded']),
    climate: z.string().optional(),
    housingAge: z.string().optional(),
  }),
});

export const collections = {
  services,
  locations,
};
"""

# ----------------- LAYOUTS -----------------

files[f'{layouts_dir}/BaseLayout.astro'] = """---
import '../styles/global.css';
import SEO from '../components/SEO.astro';
import Header from '../components/Header.astro';
import Footer from '../components/Footer.astro';

interface Props {
  title: string;
  description: string;
  canonical?: string;
  type?: 'website' | 'article';
  image?: string;
  noindex?: boolean;
}
const { title, description, canonical, type, image, noindex } = Astro.props;
---
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="icon" type="image/svg+xml" href="/favicon.svg" />
    <meta name="generator" content={Astro.generator} />
    <SEO 
      title={title} 
      description={description} 
      canonical={canonical} 
      type={type} 
      image={image} 
      noindex={noindex} 
    />
  </head>
  <body class="font-sans flex flex-col min-h-screen">
    <Header />
    <main class="flex-grow">
      <slot />
    </main>
    <Footer />
  </body>
</html>
"""

# Write all files
for path, content in files.items():
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Created component and content architecture.")
