/**
 * deck-stage.js — minimal slide-deck shell custom element
 *
 * Usage:
 *   <deck-stage width="1920" height="1080">
 *     <section>slide 1</section>
 *     <section>slide 2</section>
 *   </deck-stage>
 *
 * Features:
 *   - Fits the design canvas (default 1920x1080) into the viewport, preserving aspect ratio
 *   - Keyboard nav: arrows, PgUp/Dn, Home/End, space, Enter, Backspace, f for fullscreen
 *   - Click-nav: right half of slide advances, left half goes back
 *   - Slide-count overlay (bottom-right)
 *   - Persistence: URL hash (#7) and localStorage (per-deck path)
 *   - Print-to-PDF: one slide per page at the design dimensions
 *   - postMessage hook: emits {slideIndexChanged: N} to window.parent for speaker-notes windows
 */

class DeckStage extends HTMLElement {
  constructor() {
    super();
    this._slides = [];
    this._idx = 0;
    this._w = 1920;
    this._h = 1080;
    this._lsKey = null;
  }

  connectedCallback() {
    this._w = parseInt(this.getAttribute('width'), 10) || 1920;
    this._h = parseInt(this.getAttribute('height'), 10) || 1080;
    this._lsKey = 'deck-stage:' + location.pathname;

    // Host occupies the viewport
    Object.assign(this.style, {
      display: 'block',
      position: 'fixed',
      inset: '0',
      overflow: 'hidden',
      background: '#000',
      zIndex: '0',
    });

    // Canvas at design size; transform-scaled to fit
    this._canvas = document.createElement('div');
    this._canvas.className = 'deck-canvas';
    Object.assign(this._canvas.style, {
      position: 'absolute',
      top: '50%',
      left: '50%',
      width: this._w + 'px',
      height: this._h + 'px',
      transformOrigin: '0 0',
    });

    // Pull existing <section> children into the canvas
    this._slides = Array.from(this.querySelectorAll(':scope > section'));
    this._slides.forEach((s, i) => {
      Object.assign(s.style, {
        position: 'absolute',
        inset: '0',
        width: this._w + 'px',
        height: this._h + 'px',
        display: 'none',
      });
      if (!s.hasAttribute('data-screen-label')) {
        s.setAttribute('data-screen-label', String(i + 1).padStart(2, '0'));
      }
      this._canvas.appendChild(s);
    });
    this.appendChild(this._canvas);

    // Slide counter overlay
    this._counter = document.createElement('div');
    this._counter.className = 'deck-counter';
    this._counter.setAttribute('aria-hidden', 'true');
    Object.assign(this._counter.style, {
      position: 'absolute',
      bottom: '14px',
      right: '18px',
      color: 'rgba(255,255,255,0.55)',
      font: '500 13px/1 "JetBrains Mono", ui-monospace, monospace',
      letterSpacing: '0.14em',
      textTransform: 'uppercase',
      pointerEvents: 'none',
      zIndex: '10',
    });
    this.appendChild(this._counter);

    // Bind events
    this._onResize = this._scale.bind(this);
    window.addEventListener('resize', this._onResize);
    this._onKey = this._handleKey.bind(this);
    window.addEventListener('keydown', this._onKey);
    this._onHash = () => this._readHash();
    window.addEventListener('hashchange', this._onHash);

    // Tap navigation on the canvas itself
    this._canvas.addEventListener('click', (e) => {
      const rect = this._canvas.getBoundingClientRect();
      const x = e.clientX - rect.left;
      if (x > rect.width / 2) this._go(this._idx + 1);
      else this._go(this._idx - 1);
    });

    // Initial state: URL hash > stored > slide 0
    if (!this._readHash()) {
      if (!this._readStored()) this._go(0);
    }
    this._scale();
  }

  disconnectedCallback() {
    window.removeEventListener('resize', this._onResize);
    window.removeEventListener('keydown', this._onKey);
    window.removeEventListener('hashchange', this._onHash);
  }

  _scale() {
    const sx = window.innerWidth / this._w;
    const sy = window.innerHeight / this._h;
    const s = Math.min(sx, sy);
    this._canvas.style.transform = 'translate(-50%, -50%) scale(' + s + ')';
  }

  _handleKey(e) {
    if (e.metaKey || e.ctrlKey || e.altKey) return;
    let handled = true;
    switch (e.key) {
      case 'ArrowRight':
      case 'ArrowDown':
      case 'PageDown':
      case ' ':
      case 'Enter':
        this._go(this._idx + 1);
        break;
      case 'ArrowLeft':
      case 'ArrowUp':
      case 'PageUp':
      case 'Backspace':
        this._go(this._idx - 1);
        break;
      case 'Home':
        this._go(0);
        break;
      case 'End':
        this._go(this._slides.length - 1);
        break;
      case 'f':
      case 'F':
        if (document.fullscreenElement) document.exitFullscreen();
        else document.documentElement.requestFullscreen();
        break;
      default:
        handled = false;
    }
    if (handled) e.preventDefault();
  }

  _readHash() {
    const m = /^#(\d+)$/.exec(location.hash);
    if (m) {
      const i = parseInt(m[1], 10) - 1;
      if (i >= 0 && i < this._slides.length) {
        this._go(i, true);
        return true;
      }
    }
    return false;
  }

  _readStored() {
    try {
      const v = parseInt(localStorage.getItem(this._lsKey), 10);
      if (!Number.isNaN(v) && v >= 0 && v < this._slides.length) {
        this._go(v);
        return true;
      }
    } catch (_) {}
    return false;
  }

  _go(i, skipHash) {
    if (this._slides.length === 0) return;
    i = Math.max(0, Math.min(this._slides.length - 1, i));
    if (this._slides[this._idx]) this._slides[this._idx].style.display = 'none';
    this._idx = i;
    this._slides[this._idx].style.display = '';
    this._counter.textContent = (i + 1) + ' / ' + this._slides.length;
    try { localStorage.setItem(this._lsKey, String(i)); } catch (_) {}
    if (!skipHash) {
      history.replaceState(null, '', '#' + (i + 1));
    }
    if (window.parent !== window) {
      window.parent.postMessage({ slideIndexChanged: i }, '*');
    }
  }
}

// Print stylesheet: show every slide stacked, one per page at design size
const printStyle = document.createElement('style');
printStyle.textContent = `
@media print {
  html, body { background: white !important; }
  deck-stage {
    position: static !important;
    display: block !important;
    background: white !important;
  }
  deck-stage > .deck-canvas {
    position: static !important;
    transform: none !important;
    width: 1920px !important;
    height: auto !important;
  }
  deck-stage > .deck-canvas > section {
    display: block !important;
    position: relative !important;
    inset: auto !important;
    width: 1920px !important;
    height: 1080px !important;
    page-break-after: always;
    page-break-inside: avoid;
  }
  deck-stage > .deck-counter { display: none !important; }
  @page { size: 1920px 1080px; margin: 0; }
}
`;
document.head.appendChild(printStyle);

customElements.define('deck-stage', DeckStage);
