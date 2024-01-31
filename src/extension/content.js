// When page finishes loading, the extension needs to check if this is a recipe page or not
// we can either restrict the pages, or we can leave it open and run some sort of script to 
// check if there is a clump of recipes on a page
document.addEventListener('DOMContentLoaded', function() {
    var pageText = extractTextUsingTreeWalker(document.body)
    chrome.runtime.sendMessage({type: "pageText", text: pageText}, function(response) {
        console.log(response.farewell);
    });
});

function extractTextUsingTreeWalker(rootNode) {
    let text = '';
    const walker = document.createTreeWalker(
        rootNode,
        NodeFilter.SHOW_TEXT, 
        {
            acceptNode: function(node) {
                // Filter to only include text nodes that are not children of script, style, iframe, or noscript elements
                return (node.parentNode.nodeName !== 'SCRIPT' &&
                        node.parentNode.nodeName !== 'STYLE' &&
                        node.parentNode.nodeName !== 'IFRAME' &&
                        node.parentNode.nodeName !== 'NOSCRIPT') ?
                        NodeFilter.FILTER_ACCEPT : 
                        NodeFilter.FILTER_REJECT;
            }
        },
        false
    );

    let node;
    while (node = walker.nextNode()) {
        text += node.textContent + ' ';
    }

    return text;
}