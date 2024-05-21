// Get the current hostname and create the REST API URL
const currentHostname = window.location.hostname;
const port = window.location.port ? `:${window.location.port}` : "";


function restAPICore(cmd) {
    // Core micrOS rest API handler
    cmd = cmd.trim().replace(/\s+/g, '/');
    let query = `http://${currentHostname}${port}/rest/${cmd}`;
    const startTime = performance.now();
    let endTime;
    // Call rest api with command parameter and return the promise
    return fetch(query).then(response => {
        if (!response.ok) {
            throw new Error('restAPICore code NOK: ' + response.status);
        }
        endTime = performance.now();
        return response.json();
    }).then(response => {
        // return cmd result
        const delta = (endTime - startTime).toFixed(0);
        return { response, delta, query };                  // RETURN DATA
    }).catch(error => {
        console.error('Error in restAPICore:', error);
        throw error;
    });
}

function restAPI(cmd='', console=true) {
    // micrOS rest API handler with built-in restCmdInput
    // UPDATES: restConsole(...)
    if (cmd == '') {
        cmd = document.getElementById('restCmdInput').value;
    }
    return restAPICore(cmd)
            .then(({ response, delta, query }) => {
                if (console) {
                    restConsole(query, response, delta);
                }
            return response
        }).catch(error => {
            console.error('Error in restAPI:', error);
        });
}

function restConsole(apiUrl, data, delta) {
    // UPDATES: restConsoleUrl, restConsoleResponse, restConsoleTime
    document.getElementById('restConsoleUrl').innerHTML = `<strong>Generated URL:</strong><br> <a href="${apiUrl}" target="_blank" style="color: white;">${apiUrl}</a>`;
    document.getElementById('restConsoleResponse').innerHTML = JSON.stringify(data, null, 4).replace(/\\n/g, "<br/>" + "&nbsp;".repeat(15));
    document.getElementById('restConsoleTime').innerHTML = `⏱ Response time: ${delta} ms`;
}

// Init basic info from board
// restAPI();