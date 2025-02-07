// chatbot_widget.js
document.addEventListener('DOMContentLoaded', function () {
    // Create the chat icon button
    const chatIcon = document.createElement('div');
    chatIcon.id = 'chat-icon';
    chatIcon.innerHTML = `<img src="./assets/verde.png" alt="Chat Icon">`;
    document.body.appendChild(chatIcon);

    // Create the chat window container
    const chatContainer = document.createElement('div');
    chatContainer.id = 'chat-container';
    chatContainer.innerHTML = `
        <div id="chat-header">
            <span>GPT-101 Chatbot</span>
            <div class="header-buttons">
                <button id="expand-button" class="header-button">⛶</button>  <!-- Expand icon -->
                <button id="popout-button" class="header-button">⧉</button>   <!-- Popout icon -->
                <button id="chat-close" class="header-button">×</button>
            </div>
        </div>
        <div id="chat-body">
            <iframe 
                src="https://chat-qa.cyverse.org/intro-gpt/" 
                id="chat-frame" 
                width="100%" 
                height="100%"
                sandbox="allow-same-origin allow-scripts allow-popups allow-forms allow-top-navigation"
            ></iframe>
        </div>
    `;
    document.body.appendChild(chatContainer);

    // Event listener for iframe messages (if the iframe sends any)
    window.addEventListener('message', function(event) {
        if (event.origin === 'https://chat-qa.cyverse.org/intro-gpt/') {
            if (event.data.type === 'link') {
                window.open(event.data.url, '_blank', 'noopener,noreferrer');
            }
        }
    });

    // Toggle the chat window when the chat icon is clicked
    chatIcon.addEventListener('click', () => {
        chatContainer.style.display = chatContainer.style.display === 'block' ? 'none' : 'block';
    });

    // Close the chat window
    document.getElementById('chat-close').addEventListener('click', () => {
        chatContainer.style.display = 'none';
    });

    // Expand the chat window
    const expandButton = document.getElementById('expand-button');
    expandButton.addEventListener('click', function() {
        chatContainer.classList.toggle('expanded');
    });
      
    // Popout the chat window
    const popoutButton = document.getElementById('popout-button');
    popoutButton.addEventListener('click', function() {
        // Option A: Open only the React app in a new tab:
        //window.open('https://chat-qa.cyverse.org/intro-gpt/', '_blank', 'noopener,noreferrer');

        // Option B: Pop out the entire widget:
        const chatContent = chatContainer.outerHTML;
        const newWindow = window.open('https://chat-qa.cyverse.org/intro-gpt/', '_blank', 'width=800,height=600');
        newWindow.document.write(`
            <html>
                <base href="https://chat-qa.cyverse.org/intro-gpt/">
            <head>
            <title>CyVerse Chatbot Popout</title>
            <link rel="stylesheet" type="text/css" href="chatbot_widget.css">
            <style>
                /* Override the chat container styles for full-window display */
                #chat-container {
                    position: relative !important;
                    bottom: auto !important;
                    right: auto !important;
                    width: 100% !important;
                    height: 100% !important;
                    max-width: none !important;
                    max-height: none !important;
                    border-radius: 0 !important;
                    box-shadow: none !important;
                    display: block !important;
                }
                body { 
                    margin: 0; 
                    overflow: hidden;
                }
            </style>
        </head>
        <body>
            ${chatContent}
        </body>
            </html>
        `);
        newWindow.document.close();
        // Optionally, hide the original chat window:
        // chatContainer.style.display = 'none';
    });

    // Attempt to add event listeners to links inside the iframe (subject to cross-origin restrictions)
    const chatFrame = document.getElementById('chat-frame');
    chatFrame.onload = function() {
        try {
            const iframeLinks = chatFrame.contentDocument.getElementsByTagName('a');
            Array.from(iframeLinks).forEach(link => {
                link.setAttribute('target', '_blank');
                link.setAttribute('rel', 'noopener noreferrer');
                link.addEventListener('click', (e) => {
                    e.preventDefault();
                    window.open(link.href, '_blank', 'noopener,noreferrer');
                });
            });
        } catch (e) {
            console.log('Note: Cross-origin restrictions prevent direct iframe manipulation');
        }
    };
});
