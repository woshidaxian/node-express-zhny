var express = require('express');
var router = express.Router();

/* GET users listing. */
router.get('/', function(req, res, next) {
  res.send('respond with a resource');
});

// 管理员登录操作
router.post('/login', function(req,res,next){
  let acc = req.body.account;
  let pass = req.body.password;
})

module.exports = router;
