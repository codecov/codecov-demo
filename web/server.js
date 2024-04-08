const axios = require('axios')
const express = require("express");
const path = require("path");

const app = express();

const backendHost = 'http://localhost';
const backendPort = '8080';

app.use(express.json());
app.use("/static", express.static(path.resolve(__dirname, "static")));

app.post("/api/:operation", (req, res) => {
  axios.post(
    backendHost + ':' +  backendPort + '/api/' + req.params['operation'],
    req.body
  ).then(response => {
    res.json(response.data);
  }).catch(error => {
    console.log("Error: " + error);
  });
});

app.get("/", (req, res) => {
  res.sendFile(path.resolve("index.html"));
});
app.listen(process.env.PORT || 3000, () => console.log("Server running..."));