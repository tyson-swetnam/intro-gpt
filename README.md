# Generative AI & Prompt Engineering Workshop

A self-paced online workshop on generative AI and prompt engineering for academic research and education.

## Authors/Contributors

*   [Tyson Swetnam](https://github.com/tyson-swetnam)

## License

This work is licensed under a [Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/).

## About This Site

This documentation website is built with [Zensical](https://zensical.co/), the next-generation static site generator by the Material for MkDocs team. Zensical provides enhanced performance, better plugin support, and a modern configuration approach using TOML.

## Setup & Installation

To view the website locally, you will need to have Python and `pip` installed.

1.  Clone the repository:
    ```bash
    git clone https://github.com/tyson-swetnam/intro-gpt.git
    ```
2.  Navigate to the project directory:
    ```bash
    cd intro-gpt
    ```
3.  Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Development Server

To start the local development server with live reload:

```bash
zensical serve
```

Open your web browser and navigate to `http://127.0.0.1:8000` to view the website. Changes to markdown files will automatically refresh the browser.

### Building the Site

To build the static site for production:

```bash
zensical build
```

The generated site will be in the `site/` directory.

## Configuration

The site configuration is in `zensical.toml`. This file defines:
- Site metadata and theme settings
- Navigation structure
- Markdown extensions
- Plugin configurations

