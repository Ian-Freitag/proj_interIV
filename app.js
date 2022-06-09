// Imports
const express = require('express');
const app = express();
const port = 3000
const ejs = require('ejs');
const res = require('express/lib/response');

// Static Files
app.use(express.json);
/*
app.use('/', express.static(__dirname + ''))
*/

app.set('view engine', 'ejs');

// Set Views

app.get('/index', (req, res) => { 
    res.render('./views/index')
})


// Listen on port 3000
app.listen(port , () => console.log('Conectado com sucesso! Acesse o site: http://localhost:3000'))