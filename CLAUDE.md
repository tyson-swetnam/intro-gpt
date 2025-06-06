# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a documentation website built with MkDocs Material for a "GPT 101" workshop on AI prompt engineering. The site provides educational content on generative AI, prompt engineering, and AI tools for academic research and education.

## Development Commands

### Setup and Installation
```bash
pip install -r requirements.txt
```

### Development Server
```bash
python3 -m mkdocs serve
```
This starts a local development server with live reload for content changes.

### Building the Site
```bash
mkdocs build
```

## Project Structure

- `docs/` - All markdown content and assets for the website
- `mkdocs.yml` - Main configuration file defining site structure, theme, and plugins
- `material/` - Custom extensions (currently contains emoji extension)
- `requirements.txt` / `environment.yml` - Python dependencies for MkDocs and plugins

## Key Configuration

The site is configured in `mkdocs.yml` with:
- Material theme with custom University of Arizona branding
- Navigation structure covering AI landscape, setup guides, prompt engineering, education, research, and ethics
- Multiple markdown extensions for enhanced formatting (admonitions, code highlighting, emoji, etc.)
- Custom CSS and JavaScript for chatbot widget functionality
- Google Analytics integration
- MkDocs plugins: mkdocstrings, mkdocs-jupyter, search

## Content Guidelines

Documentation covers five main areas:
1. **Setup** - Instructions for various AI platforms (ChatGPT, Claude, Gemini, etc.)
2. **Prompt Engineering** - Core techniques and productivity applications  
3. **Education** - AI integration in teaching and learning
4. **Research** - AI applications in academic research
5. **Ethics** - Responsible AI use and considerations

The site includes interactive tutorials and case studies in the `tutorials/` subdirectory.