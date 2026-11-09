\# Universal Integration Guide for Local AI Assistant



This guide explains how any developer can download this repository, start the AI backend, and connect it to their external application (Website, PHP app, React app, etc.).



\## Step 1: Running the Backend

1\. Download or clone this repository.

2\. Double-click \*\*`run.bat`\*\* on Windows to automatically configure the environment and start the server at `http://127.0.0.1:5000`.



\## Step 2: Connecting Your App (Code Snippets)



\### JavaScript (Fetch API)

```javascript

async function askAI(userMessage) {

&#x20;   const response = await fetch('\[http://127.0.0.1:5000/api/chat](http://127.0.0.1:5000/api/chat)', {

&#x20;       method: 'POST',

&#x20;       headers: { 'Content-Type': 'application/json' },

&#x20;       body: JSON.stringify({ message: userMessage })

&#x20;   });

&#x20;   const data = await response.json();

&#x20;   console.log(data.response);

}





\###PHP (SERVER SIDE)



<?php

$url = '\[http://127.0.0.1:5000/api/chat](http://127.0.0.1:5000/api/chat)';

$data = json\_encode(\['message' => 'Hello AI']);

$ch = curl\_init($url);

curl\_setopt($ch, CURLOPT\_RETURNTRANSFER, true);

curl\_setopt($ch, CURLOPT\_CUSTOMREQUEST, "POST");

curl\_setopt($ch, CURLOPT\_POSTFIELDS,$data);

curl\_setopt($ch, CURLOPT\_HTTPHEADER, \['Content-Type: application/json']);

$response = curl\_exec($ch);

curl\_close($ch);

$result = json\_decode($response, true);

echo $result\['response'];

?>

