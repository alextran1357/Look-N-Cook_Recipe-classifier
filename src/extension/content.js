// window.addEventListener('message', (event) => {
//     console.log('Message from:', event.origin);
//     if (event.origin !== null) {
//         console.log("testing")
//         return; // Ignore messages from unexpected sources
//     }
//     console.log('Received message:', event.data);
//   });

window.addEventListener('message', (event) => {
    console.log('Message from:', event.origin);

    // Allow messages from a null origin
    if (event.origin !== "null") {
        console.log("Origin is not null, ignoring the message.");
        return; // Ignore messages from non-null origins
    }

    // Log the received message
    console.log('Received message:', event.data);
});