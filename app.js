const express = require('express')
const app = express()
const port = 3000

app.set('view engine', 'ejs')

app.get('/', (req, res) => {
    res.render('index')
})

/*
app.get('/pesquisar', (req, res) => {
    res.render('views/pesquisar')
})
*/

app.listen(port, () => {
  console.log("Conectado com sucesso! Acesse o site: http://localhost:3000")
})

/*
app.listen(port, () => console.log("Conectado com sucesso! Acesse o site: http://localhost:3000"));
*/