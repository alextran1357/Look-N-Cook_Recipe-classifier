// chrome.runtime.onMessage.addListener(
//     function(request, sender, sendResponse) {
//         if (request.action == "foundRecipes") {
//             // document.getElementById("recipeContainer").innerHTML = request.data;
//             console.log("popup.js")
//         }
//     }
// )
chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
    if (request.action == "foundRecipes") {
        console.log("Message received:", request.data);
        // Additional logic here...
    }
});
