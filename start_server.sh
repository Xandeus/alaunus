#!/bin/bash
cd dist
http-server --port=5000 &
cd ../server/
pm2 start src/app.js &
