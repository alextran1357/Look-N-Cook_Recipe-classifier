// function findRecipesOnPage() {
//     // Logic to find recipes
//     // This might involve parsing the DOM, looking for certain keywords, etc.
//     // Return an array or other structure containing the recipe information
//     return []; // Replace with actual recipe finding logic
// }
// function processText(text) {  
//     console.log("test")
//     return("THIS IS A TEST SENTENCE")
// }

document.addEventListener('DOMContentLoaded', function() {
    let allText = document.body.innerText;

    chrome.runtime.sendMessage({ action: "sendData", data: allText });
});

// let text="test"
// console.log("content.js2")
// chrome.runtime.sendMessage({ action: "foundRecipes", data: text });