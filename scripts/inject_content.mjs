import fs from 'fs';
import path from 'path';

const servicesDir = path.join(process.cwd(), 'src/content/services');

const additions = {
  'garage-door-installation.md': `
benefits:
  - title: "Enhanced Curb Appeal"
    description: "A new garage door is one of the most effective ways to instantly modernize your home's exterior and boost its market value."
  - title: "Improved Insulation"
    description: "Modern, insulated doors help regulate garage temperatures, improving energy efficiency and protecting stored belongings."
  - title: "Whisper-Quiet Operation"
    description: "New installations replace rattling tracks and worn hinges with smooth, quiet mechanics."
process:
  - title: "1. Consultation & Selection"
    description: "Discuss materials, styles, insulation values, and color options to match your home's architecture."
  - title: "2. Precise Measurement"
    description: "The opening is meticulously measured to ensure a perfect, weather-tight fit."
  - title: "3. Professional Installation"
    description: "The old door is removed and the new tracks, panels, and springs are securely installed."
  - title: "4. System Calibration"
    description: "The entire system is balanced and calibrated for effortless, safe operation."
`,
  'garage-door-replacement.md': `
benefits:
  - title: "Total System Renewal"
    description: "Replacing the door eliminates all recurring mechanical issues, giving you a fresh start with zero hassle."
  - title: "Structural Integrity"
    description: "Old doors with severe rot or rust compromise security. A replacement restores the physical barrier protecting your home."
  - title: "Modern Safety Standards"
    description: "New doors and hardware are built to strict modern safety codes to protect your family."
process:
  - title: "1. Damage Assessment"
    description: "Determine whether the door is beyond repair and discuss replacement options."
  - title: "2. Safe Removal"
    description: "Heavy, damaged panels and springs are safely disconnected and hauled away."
  - title: "3. Track & Door Replacement"
    description: "New tracks are aligned, and the replacement panels are assembled and secured."
  - title: "4. Final Walkthrough"
    description: "The new system is tested, and the area is cleaned, leaving your driveway spotless."
`,
  'garage-door-opener-repair.md': `
benefits:
  - title: "Restored Convenience"
    description: "Stop manually lifting a heavy door in the rain. Repairing the motor brings back effortless automatic access."
  - title: "Cost-Effective"
    description: "Fixing a stripped gear or bad logic board is often significantly cheaper than buying an entirely new unit."
  - title: "Security Regained"
    description: "A malfunctioning opener can leave your garage unlocked. Professional repair ensures the locking mechanism engages properly."
process:
  - title: "1. Motor Diagnostics"
    description: "The technician inspects the logic board, travel limits, gears, and capacitors."
  - title: "2. Sensor Alignment"
    description: "Safety eyes are checked and realigned to ensure the door can close safely."
  - title: "3. Component Repair"
    description: "Defective parts are swapped out for high-quality replacements."
  - title: "4. Recalibration"
    description: "Force and travel limits are reset so the door opens and closes perfectly."
`,
  'garage-door-opener-installation.md': `
benefits:
  - title: "Smart Connectivity"
    description: "New openers feature Wi-Fi integration, allowing you to monitor and control your door from anywhere."
  - title: "Unbeatable Quiet"
    description: "Upgrading to a belt-drive or jackshaft opener drastically reduces noise, perfect for garages under bedrooms."
  - title: "Advanced Security"
    description: "Modern rolling-code technology prevents hackers from cloning your remote signal."
process:
  - title: "1. Opener Selection"
    description: "Choose between chain, belt, or wall-mounted openers based on your garage's layout and noise preferences."
  - title: "2. Professional Mounting"
    description: "The motor is securely mounted to the ceiling or wall to eliminate intense vibrations."
  - title: "3. Wiring & Sensor Setup"
    description: "Safety eyes and wall consoles are wired in cleanly without exposed messes."
  - title: "4. Smart Home Sync"
    description: "The unit is connected to your home network and remotes are programmed."
`,
  'garage-door-spring-repair.md': `
benefits:
  - title: "Immediate Restoration"
    description: "A broken spring paralyzes your door. Replacement instantly restores its ability to open and close."
  - title: "Prevent Opener Damage"
    description: "Running a motor with a broken spring will destroy the opener. New springs protect your existing hardware."
  - title: "Safer Environment"
    description: "Properly tensioned springs prevent the door from crashing down unexpectedly."
process:
  - title: "1. Safe Unwinding"
    description: "Any remaining tension is safely bled from the old springs to prevent injury."
  - title: "2. Complete Replacement"
    description: "Old springs are removed and matched with high-cycle replacements for maximum longevity."
  - title: "3. Precision Tensioning"
    description: "The new springs are wound to the exact tension required for your door's specific weight."
  - title: "4. Balance Check"
    description: "The door is lifted halfway and released to verify it stays perfectly balanced in place."
`,
  'emergency-garage-door-repair.md': `
benefits:
  - title: "Immediate Security"
    description: "A door stuck open overnight is an invitation to intruders. Emergency repair secures your home fast."
  - title: "Prevent Further Damage"
    description: "Forcing a crooked door to close can rip the tracks off the wall. Professional intervention stops the bleeding."
  - title: "Peace of Mind"
    description: "Get your car out of the garage and get back to your life without waiting days for an appointment."
process:
  - title: "1. Rapid Response"
    description: "Priority dispatch to get a technician to your home to secure the situation."
  - title: "2. Crisis Stabilization"
    description: "The door is safely stabilized to prevent a collapse or structural damage."
  - title: "3. Critical Repairs"
    description: "The snapped cables, broken springs, or derailed rollers causing the emergency are replaced."
  - title: "4. Functional Restoration"
    description: "The door is re-secured to the tracks and verified safe to operate."
`
};

for (const [filename, addition] of Object.entries(additions)) {
  const filePath = path.join(servicesDir, filename);
  let content = fs.readFileSync(filePath, 'utf-8');
  
  if (content.includes('benefits:')) {
    console.log(`Skipping ${filename}, already has benefits.`);
    continue;
  }
  
  // Find the 'faqs:' line and insert before it
  content = content.replace(/^faqs:/m, addition.trim() + '\nfaqs:');
  fs.writeFileSync(filePath, content, 'utf-8');
  console.log(`Updated ${filename}`);
}
