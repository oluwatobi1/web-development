var board = $('.board')
var start = $(".start")

var table = $('table tr')

console.log('laided');

function fadeOutAmimation(row, col){
  return table.eq(row).find('td').eq(col).find('button').fadeToggle(1000)
}

for (var row = 0; row <6 ; row++) {
  for (var col = 0; col < 8; col++) {
    table.eq(row).find('td').eq(col).find('button').hide()

  }
}

start.on('click', function() {
  for (var row = 0; row <6 ; row++) {
    for (var col = 0; col < 8; col++) {
      fadeOutAmimation(row, col)

    }
  }
  console.log('clicked');
}
)
