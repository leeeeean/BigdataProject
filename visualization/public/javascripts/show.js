$(function() {
  function slide() {
    var first = $('#slide-container img:last-of-type')
    $('#slide-container').prepend(first)
  }
  var intervalF = setInterval(slide, 100)

  $(".stop").click(function() {
    clearInterval(intervalF)
  });
  $(".run").click(function() {
    intervalF = setInterval(slide, 100)
  });
})