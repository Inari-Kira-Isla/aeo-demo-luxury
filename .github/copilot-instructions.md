# aeo-demo-luxury

## Project

AEO (AI-Optimized) demo template for luxury industry websites using HTML, Schema.org, and AI-friendly markup.

## Conventions

- Use semantic HTML5 elements (header, main, article, section, footer)
- Include structured data with JSON-LD Schema.org markup
- Add llms.txt for AI crawler compatibility
- Implement FAQ schema for rich snippets
- Keep all code in single HTML files per page
- Use aria-labels for accessibility

## Naming

- Use kebab-case for file names (e.g., `about-us.html`, `luxury-products.html`)
- Use descriptive, SEO-friendly URLs
- Name Schema.org entities clearly (e.g., `Product`, `FAQPage`, `BreadcrumbList`)

## Architecture

- Single-page HTML files with inline CSS/JS
- JSON-LD scripts for structured data
- Static HTML output (no build step required)
- Responsive design with mobile-first approach

## Commands

- No build commands (pure static HTML)
- Deploy to Vercel: `vercel deploy` or push to git

## Do Not

- Do not add JavaScript frameworks or libraries
- Do not use server-side rendering
- Do not omit Schema.org structured data
- Do not skip alt tags on images
- Do not use non-semantic div soup markup