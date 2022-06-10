const express = require('express')
const { use } = require('express/lib/application')
const app = express()
const port = 3000
const path = require('path')


app.set('view engine', 'ejs')
app.use(express.json());
app.use('/public', express.static(path.join(__dirname + '/public')));

app.get('/', (req, res) => {
    res.render('index')
})

app.get('/cadastro', (req, res) => {
    res.render('cadastro')
})

app.get('/ajuda', (req, res) => {
    res.render('ajuda')
})

app.get('/sobre', (req, res) => {
    res.render('sobre')
})

app.get('/volkswagen', (req, res) => {
    res.render('volkswagen')
})

app.get('/audi', (req, res) => {
    res.render('audi')
})

app.get('/chevrolet', (req, res) => {
    res.render('chevrolet')
})

app.listen(port, () => {
  console.log("Conectado com sucesso! Acesse o site: http://localhost:3000")
})

/*
app.listen(port, () => console.log("Conectado com sucesso! Acesse o site: http://localhost:3000"));
*/