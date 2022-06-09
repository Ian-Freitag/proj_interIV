const express = require('express')
const { use } = require('express/lib/application')
const app = express()
const port = 3000
const path = require('path')

app.set('view engine', 'ejs')
app.use(express.json());
app.use('/',express.static(path.join(__dirname + '/css')));

app.get('/', (req, res) => {
<<<<<<< HEAD
    res.render('index')
=======
    res.render('pages/index')
})
app.get('/', (req, res) => {
    res.render('pages/cadastro')
})
app.listen(port, () => {
  console.log(`App listening at port ${port}`)
>>>>>>> 20b68ad27d73e1467885b7adfb948c1d0a58817f
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