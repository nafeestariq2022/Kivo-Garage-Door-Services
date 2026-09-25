import seedrandom from 'seedrandom';

export function createRNG(seed: string) {
  return seedrandom(seed);
}

/**
 * Parses a spintax string (e.g., "{Hello|Hi} there!") deterministically 
 * based on the provided PRNG.
 */
export function parseSpintax(text: string, rng: any): string {
  if (!text || typeof text !== 'string') return text;
  
  let result = text;
  
  // Regex to match innermost spintax blocks that contain at least one pipe: {opt1|opt2}
  const regex = /\{([^{}]+\|[^{}]+)\}/g;
  
  // Iterate until no more spintax blocks are found (handles nesting)
  while (regex.test(result)) {
    result = result.replace(regex, (match, optionsString) => {
      const options = optionsString.split('|');
      const choiceIndex = Math.floor(rng() * options.length);
      return options[choiceIndex];
    });
  }
  
  return result;
}

/**
 * Recursively applies spintax parsing to all string values within an object or array.
 */
export function applySpintaxToObj<T>(obj: T, rng: any): T {
  if (typeof obj === 'string') {
    return parseSpintax(obj, rng) as any;
  }
  
  if (Array.isArray(obj)) {
    return obj.map(item => applySpintaxToObj(item, rng)) as any;
  }
  
  if (obj !== null && typeof obj === 'object') {
    const newObj: any = {};
    // Sort keys to guarantee deterministic order of RNG stream consumption
    const keys = Object.keys(obj).sort();
    for (const key of keys) {
      newObj[key] = applySpintaxToObj((obj as any)[key], rng);
    }
    return newObj;
  }
  
  return obj;
}
