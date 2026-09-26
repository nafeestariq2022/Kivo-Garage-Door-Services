import { defineCollection, z } from 'astro:content';
import { file, glob } from 'astro/loaders';

const services = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/services" }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    shortDescription: z.string(),
    isPriority: z.boolean().default(false),
    seo: z.object({
      titleTemplate: z.string(),
      metaDescriptionTemplate: z.string(),
      h1Template: z.string(),
    }),
    hero: z.object({
      subtitleTemplate: z.string(),
      imageSrc: z.string(),
      imageAlt: z.string(),
    }),
    commonProblems: z.array(z.object({
      title: z.string(),
      description: z.string(),
    })).optional(),
    faqs: z.array(z.object({
      question: z.string(),
      answer: z.string(),
    })).optional(),
    benefits: z.array(z.object({
      title: z.string(),
      description: z.string(),
    })).optional(),
    process: z.array(z.object({
      title: z.string(),
      description: z.string(),
    })).optional(),
  }),
});

const locations = defineCollection({
  loader: file("data/processed/canonical_locations.json", {
    parser: (text) => {
      const data = JSON.parse(text);
      return data.map((item: any) => ({ ...item, id: item.slug.replace('/', '-') }));
    }
  }),
  schema: z.object({
    id: z.string(),
    city: z.string(),
    state: z.string(),
    slug: z.string(),
    zips: z.string(),
    max_cpl: z.coerce.number(),
    population: z.coerce.string().optional(),
    mentor_score: z.coerce.string().optional(),
    status: z.enum(['candidate', 'approved', 'priority', 'indexable', 'excluded']),
  }),
});

const authors = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/authors" }),
  schema: z.object({
    name: z.string(),
    role: z.string(),
    image: z.string(),
    shortBio: z.string(),
    linkedin: z.string().url().optional(),
  }),
});

const blog = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/blog" }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    pubDate: z.date(),
    author: z.string(), // references an author slug
    category: z.string(), // corresponds to C-Node
    image: z.string().optional(),
    imageAlt: z.string().optional(),
  }),
});

export const collections = {
  locations,
  services,
  authors,
  blog,
};
