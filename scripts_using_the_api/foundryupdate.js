const foundrybutton = document.getElementById("foundrybutton");
if (foundrybutton) {
    const wikiApiUrl = 'https://wiki.samoore.page/graphql';
    const foundryApiUrl = "http://dm.samoore.page/foundry";
    const page_url = window.location.href;
    let button = document.createElement("button");
    button.style.backgroundImage = "url('https://repository-images.githubusercontent.com/501376342/429c4d03-3c60-4e9c-903d-ea3001da9e05')";
    button.style.backgroundSize = "cover";
    button.style.backgroundPosition = "center";
    button.style.backgroundRepeat = "no-repeat";
    button.style.width = "5rem";
    button.style.height = "2rem";
    button.style.borderRadius = "5px";
    botton.eventListener("click", sendUpdatetoFoundry);
    dbbutton.appendChild(button);
}

// Function to send player ID to the update API
async function sendUpdatetoFoundry() {
    try {
        const response = await fetch(updateApiUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ id: page_url }),
        });

        if (!response.ok) {
            throw new Error('Failed to send update to Foundry');
        } else {
            const responseData = await response.json();
            console.log(responseData);
        }
    } catch (error) {
        console.error(error);
        return null;
    }
}