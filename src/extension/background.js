let storedData;
chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
        if (request.action == "foundRecipes") {
            document.getElementById("recipeContainer").innerHTML = request.data;
        } else if (request.action === "sendData") {
            storedData = request.data;

        } else if (request.action === "requestData") {
            sendResponse(storedData)
        }
    }
)