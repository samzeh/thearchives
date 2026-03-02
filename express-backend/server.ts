const express = require('express')
const app = express()
const { Pool } = require("pg")
const PORT = 3000

app.use(express.urlencoded({ extended: true}))


const pool = new Pool({
});

app.listen(3000)