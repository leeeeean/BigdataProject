const express = require('express');
const router = express.Router();
const fs = require('fs');

/* GET home page. */
router.get('/', async function(req, res, next) {
  const cloud = 'public/images/cloud/';
  
  fs.readdir(cloud, (err, files) => {
    // console.log(files)
    files.reverse()
    res.render('index', { files: files });
  })
  res.render('index', { title: 'Express', img: files });
  
});

module.exports = router;
