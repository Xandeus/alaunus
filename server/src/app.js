const express = require('express')
const bodyParser = require('body-parser')
const cors = require('cors')
const morgan = require('morgan')
const { exec } = require("child_process");

const app = express()
app.use(morgan('combined'))
app.use(bodyParser.json())
app.use(cors())

function executeCommand () {
}

app.post('/posts', (req, res) => {
    let result = 'No response';
    console.log('Request: ', req.body);
    const command = req.body.command;
    const stripAnimations = [
        { title: "rainbow", description: "Colorful rainbow" },
        { title: "colorful", description: "It's all colorful" }
    ];
    exec(command, (error, stdout, stderr) => {
        if (error) {
            console.log(`error: ${error.message}`);
            return;
        }
        if (stderr) {
            console.log(`stderr: ${stderr}`);
            return;
        }
        console.log(`stdout: ${stdout}`);
        result = { title: "ls -la", description: stdout};
        res.send(
            stripAnimations
        )
    });
})

app.post('/toggles', (req, res) => {
    const toggleObj = req.body;
    console.log('Request: ', req.body);
    if (toggleObj.name === 'powerToggle' && toggleObj.state) {
        console.log('Turning LEDS on');
    } else if (toggleObj.name === 'powerToggle') {
        console.log('Turning LEDS off');
    }
    res.send();
})


app.listen(process.env.PORT || 8081)