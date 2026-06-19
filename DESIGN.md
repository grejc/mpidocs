---
name: Neon Protocol
colors:
  surface: '#0e141a'
  surface-dim: '#0e141a'
  surface-bright: '#343a41'
  surface-container-lowest: '#090f15'
  surface-container-low: '#161c23'
  surface-container: '#1a2027'
  surface-container-high: '#252a31'
  surface-container-highest: '#2f353c'
  on-surface: '#dde3ec'
  on-surface-variant: '#b9cacb'
  inverse-surface: '#dde3ec'
  inverse-on-surface: '#2b3138'
  outline: '#849495'
  outline-variant: '#3a494b'
  surface-tint: '#00dbe7'
  primary: '#e1fdff'
  on-primary: '#00363a'
  primary-container: '#00f2ff'
  on-primary-container: '#006a71'
  inverse-primary: '#00696f'
  secondary: '#ebb2ff'
  on-secondary: '#520071'
  secondary-container: '#ce5dff'
  on-secondary-container: '#480064'
  tertiary: '#f6f8ff'
  on-tertiary: '#27313e'
  tertiary-container: '#d2dced'
  on-tertiary-container: '#57616f'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#74f5ff'
  primary-fixed-dim: '#00dbe7'
  on-primary-fixed: '#002022'
  on-primary-fixed-variant: '#004f54'
  secondary-fixed: '#f8d8ff'
  secondary-fixed-dim: '#ebb2ff'
  on-secondary-fixed: '#320047'
  on-secondary-fixed-variant: '#74009f'
  tertiary-fixed: '#d9e3f4'
  tertiary-fixed-dim: '#bdc7d8'
  on-tertiary-fixed: '#121c28'
  on-tertiary-fixed-variant: '#3e4755'
  background: '#0e141a'
  on-background: '#dde3ec'
  surface-variant: '#2f353c'
typography:
  headline-xl:
    fontFamily: Geist
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Geist
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-lg-mobile:
    fontFamily: Geist
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.2'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  code-sm:
    fontFamily: Space Mono
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
  label-caps:
    fontFamily: Space Mono
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.1em
spacing:
  base: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 48px
  container-max: 1280px
  gutter: 24px
---

## Brand & Style

The design system is built for high-performance cybernetic environments and technical documentation. It evokes a sense of "digital precision" and "synthetic intelligence," targeting developers, sysadmins, and high-tech enthusiasts. 

The aesthetic is a hybrid of **Minimalism** and **Cyberpunk-Modernism**. It utilizes deep obsidian backgrounds to reduce eye strain during long sessions, contrasted with hyper-vibrant neon accents that draw attention to critical data points. The interface feels like a high-end terminal: cold, efficient, and data-dense, yet refined through modern spacing and glassmorphism. It prioritizes clarity and information density over decorative elements.

## Colors

The palette is anchored in a "Deep Dark" base to establish a limitless digital canvas. 

- **Primary (Cyan):** Used for primary actions, success states, and active navigation. It represents "system online" status.
- **Secondary (Electric Purple):** Used for accents, secondary data streams, and branding elements.
- **Backgrounds:** The foundation is `#050a10`, with `#0a1420` used for elevated cards and containers to create subtle depth.
- **Status Colors:** Use Primary Cyan for success, a high-octane red (#ff0055) for errors, and a vivid amber (#ffb800) for warnings. All status colors should maintain high saturation to "glow" against the dark background.

## Typography

This design system utilizes a tiered typography strategy to balance technical utility with modern readability.

- **Headlines:** Use **Geist** for its razor-sharp terminals and technical precision. Large headings should be tightly tracked.
- **Body:** **Inter** provides maximum legibility for long-form documentation and technical specs, ensuring complex information is easily digestible.
- **Data & Labels:** **Space Mono** is utilized for all functional labels, metadata, and code snippets. This reinforces the "cybernetic" feel and ensures numerical data aligns perfectly in tables and logs.

## Layout & Spacing

The layout follows a strict **4px baseline grid** to ensure mathematical consistency. 

- **Desktop:** 12-column fluid grid with 24px gutters. Use wide margins (at least 48px) to keep content centered and readable.
- **Tablet:** 8-column grid with 16px gutters and 24px margins.
- **Mobile:** 4-column grid with 16px gutters.
- **Content Blocks:** Use "Technical Padding"—generous internal padding within cards (24px+) to prevent the dense data from feeling cluttered. Documentation sections should be separated by clear horizontal rules or high-contrast borders rather than just whitespace.

## Elevation & Depth

Depth is conveyed through **Tonal Layering** and **Luminescent Outlines** rather than traditional shadows.

1.  **Level 0 (Base):** `#050a10` - The main canvas.
2.  **Level 1 (Surface):** `#0a1420` - Cards, navigation bars, and sidebars. 
3.  **Level 2 (Overlay):** `#141e2d` - Modals and tooltips.

**High-Contrast Borders:** Every interactive surface must have a 1px solid border. Use `#1e293b` for inactive states and the **Primary Cyan** for active or hovered states. To simulate a "HUD" (Heads-Up Display) effect, use a very subtle inner-glow (box-shadow: inset 0 0 10px rgba(0, 242, 255, 0.05)).

## Shapes

The shape language is **Sharp**. This design system rejects softness in favor of architectural rigidity.

- **Corners:** 0px radius for all components (buttons, cards, inputs). This creates a brutalist, technical aesthetic reminiscent of legacy terminal systems and blueprints.
- **Accents:** Use "clipped corners" (45-degree chamfers) on decorative elements or primary buttons to reinforce the futuristic military-grade tech feel.

## Components

- **Buttons:** Sharp 0px corners. Primary buttons have a solid Cyan background with black text. Ghost buttons use a 1px Cyan border and Cyan text. On hover, buttons should trigger a "flicker" transition or a subtle outer glow.
- **Inputs:** Darker than the surface background. Use **Space Mono** for input text. The bottom border should be thicker (2px) than the other three sides to ground the element.
- **Cards:** No shadows. Defined solely by 1px borders. Header sections of cards should have a subtle diagonal-stripe pattern (CSS linear-gradient) in the background to denote "active data zones."
- **Chips/Status Tags:** Use **Label-caps** typography. Tags are rectangular with a background opacity of 10% of their status color (e.g., 10% Cyan background, 100% Cyan text).
- **Code Blocks:** Syntax highlighting must use a high-contrast neon theme. Background should be slightly darker than the base (`#020408`) to set it apart from the prose.
- **Data Tables:** Strict horizontal lines only. Use zebra-striping with a very low opacity change (`#0a1420` and `#0c1826`). All headers must be in **Space Mono** caps.