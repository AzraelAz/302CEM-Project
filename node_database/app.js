var http = require("http");
var stack = require("stack");
var express = require("express");
var router = express.Router();
var mysql = require("mysql");
var bodyParser = require("body-parser");
var urlencodedParser = bodyParser.urlencoded({ extended: false });

var app = express(); // Generate Application
app.engine("html", require("ejs").renderFile);

app.use(bodyParser.json());

var mysql = require("mysql");
var connection = mysql.createConnection({
    host: "localhost",
    user: "root",
    password: "",
    database: "logistic_db",
});

app.get("/", function(req, res) {
    //when user connect to ("/"), as a response
    res.render("index.html");
});

app.get("/index", function(req, res) {
    //when user connect to ("/"), as a response
    res.render("index.html");
});

app.get("/order", function(req, res) {
    res.render("order.ejs");
});
app.post("/order", urlencodedParser, function(req, res) {
    console.log(req.body);

    var sql =
        "INSERT INTO orderlist (S_FirstName, S_LastName, S_Address, S_City, S_Country, R_FirstName, R_LastName,R_Address,R_City, R_Country, ProductName, OrderQun) VALUES ('" +
        req.body.S_FirstName +
        "','" +
        req.body.S_LastName +
        "','" +
        req.body.S_Address +
        "','" +
        req.body.S_City +
        "','" +
        req.body.S_Country +
        "','" +
        req.body.R_FirstName +
        "','" +
        req.body.R_LastName +
        "','" +
        req.body.R_Address +
        "','" +
        req.body.R_City +
        "','" +
        req.body.R_Country +
        "','" +
        req.body.ProductName +
        "','" +
        req.body.OrderQun +
        "')";
    console.log(req.body);
    console.log(typeof req.body);
    connection.query(sql, function(err, result) {
        if (err) throw err;
        console.log("Insert Error:", err);
    });
    res.render("order.ejs");
});

app.listen(8080, function() {
    console.log("Server now run at http://localhost:8080/");
});