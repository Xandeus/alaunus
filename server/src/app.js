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
            [result]
        )
    });
})

app.listen(process.env.PORT || 8081)