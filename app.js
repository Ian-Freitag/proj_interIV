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