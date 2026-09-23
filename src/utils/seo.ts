export function generateSEO(template: string, data: { city: string; state: string }): string {
  if (!template) return '';
  return template
    .replace(/{City}/g, data.city)
    .replace(/{State}/g, data.state);
}
