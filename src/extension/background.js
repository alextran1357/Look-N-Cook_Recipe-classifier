chrome.runtime.onInstalled.addListener(() => {
    chrome.action.onClicked.addListener((tab) => {
      fetch('https://mmhhfdbck6.execute-api.us-east-2.amazonaws.com/LnC_data_processing', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ /* Your request payload */ })
      })
      .then(response => response.json())
      .then(data => {
        console.log(data);
        // Handle the response data
      })
      .catch(error => {
        console.error('Error:', error);
      });
    });
  });
  