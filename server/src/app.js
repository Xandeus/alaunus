const express = require('express')
const bodyParser = require('body-parser')
const cors = require('cors')
const morgan = require('morgan')
const { exec } = require("child_process");

const app = express()
let ledState = false
app.use(morgan('combined'))
app.use(bodyParser.json())
app.use(cors())
console.log('Starting up')

app.post('/posts', (req, res) => {
    let result = 'No response';
    console.log('Request: ', req.body);
    const command = req.body.command;
    const stripAnimations = [
	    { title: "POWER", description: "Turn the LEDS on and off", isActive: ledState }, 
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
    let command = 'echo no actions taken';
    console.log(toggleObj);
    if (toggleObj.name === 'POWER' && toggleObj.state) {
        command = './../send_command.sh';
        ledState = true;
    	console.log('Turning LEDS on');
    } else if (toggleObj.name === 'POWER') {
        ledState = false;
        command = './../send_stop.sh';
        console.log('Turning LEDS off');
    }
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
	res.send('exectued command');
    });
})

app.post('/rfTransmits', (req, res) => {
    const rfTransmissionObj = req.body;
    console.log('Request: ', req.body);
    let command = 'echo no actions taken';
    console.log(rfTransmissionObj);
    console.log('Transmitting bitstring', rfTransmissionObj.name);
    command = './../transmitRF.py %s' % rfTransmissionObj.name
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
	res.send('exectued command');
    });
})


app.listen(process.env.PORT || 8081)
