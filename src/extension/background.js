chrome.runtime.onMessage.addListener(
    function(request, sender, sendResponse) {
        if (request.type === "pageText") {
            if (request.text) {
                var text = request.text
                var cleanedText = processText(text)
                var data = postDataToAPI(cleanedText)
                // prediction logic
                recipeList = processPredictions(data)
            }
            sendResponse({farewell: "Finished"});
        }
        return true;
    }
);

function postDataToAPI(payload) {
    const apiURL = 'https://mmhhfdbck6.execute-api.us-east-2.amazonaws.com/LnC_data_processing';
    fetch(apiURL, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: payload
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json()
    })
    .then(data => {
        console.log('Data received:', data);
        return data
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

function processText(text) {
    const splitSentences = str => str.match(/\S.*?(?<!\w\.\w)(?<![A-Z][a-z]\.)(?<=\.|\?|!)\s/g);
    var splitText = splitSentences(text)
    var filteredStrings = splitText.filter(str => str.length >= 8 && /\s/.test(str));
    var cleanedSentences = filteredStrings.map(cleanSentence);
    const sentencesPayload = JSON.stringify({ sentences: cleanedSentences });
    return sentencesPayload
}

function cleanSentence(sentence) {
    let cleaned = sentence.replace(/"\)/g, '');
    cleaned = cleaned.replace(/\s+/g, ' ');
    cleaned = cleaned.trim();
    return cleaned;
}

function processPredictions(predictions) { 
    return predictions
}