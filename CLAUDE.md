# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a documentation website built with Zensical (the next-generation static site generator by the Material for MkDocs team) for a "GPT 101" workshop on AI prompt engineering. The site provides educational content on generative AI, prompt engineering, and AI tools for academic research and education.

## Development Commands

### Setup and Installation
```bash
pip install -r requirements.txt
```

### Development Server
```bash
zensical serve
```
This starts a local development server with live reload for content changes.

### Building the Site
```bash
zensical build
```

## Project Structure

- `docs/` - All markdown content and assets for the website
- `zensical.toml` - Main configuration file defining site structure, theme, and plugins
- `requirements.txt` - Python dependencies for Zensical and plugins
- `site/` - Generated static site output (created by `zensical build`)

## Key Configuration

The site is configured in `zensical.toml` with:
- Material theme with custom University of Arizona branding
- Navigation structure covering AI landscape, setup guides, prompt engineering, education, research, and ethics
- Multiple markdown extensions for enhanced formatting (admonitions, code highlighting, emoji, etc.)
- Custom CSS and JavaScript for chatbot widget functionality
- Google Analytics integration
- Zensical plugins: mkdocstrings (preliminary support), search (built-in)

## Content Guidelines

Documentation covers five main areas:
1. **Setup** - Instructions for various AI platforms (ChatGPT, Claude, Gemini, etc.)
2. **Prompt Engineering** - Core techniques and productivity applications  
3. **Education** - AI integration in teaching and learning
4. **Research** - AI applications in academic research
5. **Ethics** - Responsible AI use and considerations

The site includes interactive tutorials and case studies in the `tutorials/` subdirectory.