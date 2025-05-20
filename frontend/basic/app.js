// API endpoint URLs - UPDATED VERSION WITH TIMESTAMP: ${new Date().toISOString()}
// Setting FastAPI URL hardcoded to avoid any caching issues
const socketUrl = 'http://localhost:8002';  // Socket server URL
const fastapiUrl = 'http://localhost:8001';  // Updated to port 8001

console.log('FASTAPI URL BEING USED:', fastapiUrl);

// Get references to DOM elements
const socketFetchBtn = document.getElementById('socketFetchBtn');
const fastapiFetchBtn = document.getElementById('fastapiFetchBtn');
const socketResponse = document.getElementById('socketResponse');
const fastapiResponse = document.getElementById('fastapiResponse');
const fastapiCreateBtn = document.getElementById('fastapiCreateBtn');

// Event listener for Socket Server button
socketFetchBtn.addEventListener('click', async () => {
     try{
          socketResponse.textContent = 'Fetching messages...';
          const response = await fetch(`${socketUrl}/api/message`);
          const data = await response.json();
          socketResponse.textContent = JSON.stringify(data, null, 2);
     }catch(error){
          socketResponse.textContent = `Error: ${error.message}`;
          console.error('Error fetching messages:', error);
     }
});

// Event listener for FastAPI Server fetch button
fastapiFetchBtn.addEventListener('click', async () => {
     try{
          fastapiResponse.textContent = 'Fetching messages...';
          console.log('Fetching from:', `${fastapiUrl}/api/messages`);
          // BUG: Incorrect endpoint - should be /api/messages
          const response = await fetch(`${fastapiUrl}/api/messages`);
          console.log('Response status:', response.status);
          console.log('Response headers:', response.headers);
          const data = await response.json();
          console.log('Data received:', data);
          fastapiResponse.textContent = JSON.stringify(data, null, 2);
     }catch(error){
          console.error('Full error:', error);
          fastapiResponse.textContent = `Error: ${error.message}`;
          console.error('Error fetching messages:', error);
     }
});

// Event listener for creating a new message
fastapiCreateBtn.addEventListener('click', async () => {
     try{
          // BUG: Missing prompt to get message text
          const messageText = prompt('Enter a message:');
          if (!messageText) return;  // Exit if no message entered
          
          // BUG: Incorrect endpoint - should be /api/messages
          const response = await fetch(`${fastapiUrl}/api/messages`, {
               method: 'POST',
               headers: {
                    'Content-Type': 'application/json'
               },
               body: JSON.stringify({
                    text: messageText  // BUG: Fixed variable name
               })
          });

          // BUG: Variable name mismatch (Newmessage vs newMessage)
          const newMessage = await response.json();
          fastapiResponse.textContent = `Message created successfully:\n${JSON.stringify(newMessage, null, 2)}`;
          
          // BUG: Missing refresh of messages after creation
          // Refresh the message list
          fastapiFetchBtn.click();
     }catch(error){
          fastapiResponse.textContent = `Error: ${error.message}`;
          console.error('Error creating message:', error);
     }
});

// BUG: Missing initialization of the page
// Initialize when the DOM is fully loaded
document.addEventListener('DOMContentLoaded', () => {
    // Check if all DOM elements were found
    if (!socketFetchBtn || !fastapiFetchBtn || !fastapiCreateBtn) {
        console.error('Some DOM elements were not found');
    }
});


        