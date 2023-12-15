chrome.runtime.onMessage.addListener(
    function(request, sender, sendResponse) {
        if (request.action == "foundRecipe") {
            document.geteElementById("recipeContainer").innerText = request.data;
        }
    }
)