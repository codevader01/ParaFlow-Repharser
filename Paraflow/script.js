document.addEventListener("DOMContentLoaded", () => {
    const inputText = document.getElementById('inputText');
    const outputText = document.getElementById('outputText');
    const letterCount = document.getElementById('letterCount');
    const errorMessage = document.getElementById('errorMessage');
    const rephraseButton = document.getElementById('rephraseBtn');
    const maxLetters = 1000;

    // ✅ Letter count validation
    inputText.addEventListener('input', () => {
        let letters = inputText.value.length;
        letterCount.innerText = letters + ' / ' + maxLetters;

        if (letters > maxLetters) {
            errorMessage.innerText = '⚠️ Character limit exceeded!';
            inputText.style.border = '2px solid red';
        } else {
            errorMessage.innerText = '';
            inputText.style.border = 'none';
        }
    });

    // ✅ Rephrase request to FastAPI backend
    rephraseButton.addEventListener('click', async () => {
        const text = inputText.value;

        if (text.trim() === "") {
            outputText.value = "Please enter some text to rephrase.";
            return;
        }

        try {
            const response = await fetch("http://127.0.0.1:8000/phrase", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ data: text })
            });

            const result = await response.json();
            console.log("Response JSON:", result);  // Debugging

            if (result.name) {
                outputText.value = result.name;
            } else {
                outputText.value = "Error: No rephrased text received.";
            }
        } catch (error) {
            console.error("Fetch Error:", error);
            outputText.value = "❌ Error processing request. Make sure the server is running.";
        }
    });
});
