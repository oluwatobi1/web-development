var player1Name = prompt('Player 1: Enter your name:')
var player2Name = prompt('Player 2: Enter your name:')

var player1color = 'rgb(12, 24, 247)'
var player2color = 'rgb(247, 29, 12)'

// define horizontal win
// define vertical win
// define diagonal win
// define drop take the player1Name and player1color
//
// define last empty
//
var board = $('.board button')
table = $('table tr')
// Start with Player One
$("h4").text("Welcome " + player1Name + ": Click on a cell to drop your chip")

function checkcellcolor(rowIndex, colIndex) {
  return table.eq(rowIndex).find('td').eq(colIndex).css('background-color')
}
function changeCellColor(rowIndex, colIndex, color) {
  table.eq(rowIndex).find('td').eq(colIndex).css('background-color', color)
}

function lastemptycell(colIndex) {
  var last = checkcellcolor(5, colIndex)
  for (var i = 5; i >0; i--) {
    last = checkcellcolor(i, colIndex)
    if (last = 'rgb(3, 252, 115)') {
      return i
    }
    continue;
  }
}
function win(row, col, currentplayer){
  console.log('GAME WON')
  $('h5').text('You won starting from' + row +' row' +" to this"+ col + " column")
}

function checkmatch(one, two, three, four) {
  return (one === two && one === three && one === four && one !== 'rgb(3, 252, 115)' && one !== undefined)
}

function horizontalwin() {
  for (var row = 5; row > 0; row--) {
    for (var col = 0; col < 4; col++) {
      if (checkmatch(checkcellcolor(row, col), checkcellcolor(row, col+1), checkcellcolor(row, col+2), checkcellcolor(row, col+3), checkcellcolor(row, col+4))){
        win(row, col, currentplayer)
        console.log('horizontal');
      }else {
        continue;
      }
    }
  }
}


function verticalwin() {
  for (var row = 0; row < 3; row++) {
    for (var col = 0; col < 5; col++){
      if (checkmatch(checkcellcolor(row, col), checkcellcolor(row+1, col), checkcellcolor(row+2, col), checkcellcolor(row+3, col))){
   win(row, col, currentplayer)
   console.log('vertical');
   return True;
}else {
  continue;
}
};
};
}

function diagonalwin(){
  for (var row = 0; row < 7; row++) {
    for (var col = 0; col < 5; col++){
      if (checkmatch(checkcellcolor(row, col), checkcellcolor(row+1, col+1), checkcellcolor(row+2, col+2), checkcellcolor(row+3, col+3))){
   win(row, col, currentplayer)
   console.log('diagonal win');
   return True;
}else if (checkmatch(checkcellcolor(row, col), checkcellcolor(row-1, col), checkcellcolor(row-2, col), checkcellcolor(row-3, col+3))){
win(row, col, currentplayer)
console.log('diagonal win');
return True;
} else {
  continue;
}
    }
  }

}

// generics
var currentplayer = player1Name
var currentcolor = player1color
var playswitch = 1;

board.on('click', function(){
  var col = $(this).closest('td').index()
  console.log(col);
  avail = lastemptycell(col)
  console.log(avail);
  changeCellColor(col, avail, currentcolor);

  if (horizontalwin){
    $('h4').text(currentplayer + ' has WON!')
    $('h2').text("Reload page to restart")
    $('h4').fadeOut('fast')
    console.log('horizontalwin');
  }else if (verticalwin){
    $('h4').text(currentplayer + ' has WON!')
    $('h2').text("Reload page to restart")
    $('h4').fadeOut('verticalwin')
    console.log('done');
  }else if (horizontalwin){
    $('h4').text(currentplayer + ' has WON!')
    $('h2').text("Reload page to restart")
    $('h4').fadeOut('fast')
    console.log('diagonal');
  }

playswitch = playswitch*-1

  if (playswitch == 1){
    currentplayer = player1Name
    currentcolor = player1color
    $('h4').text(currentplayer + ' its your turn')
  }else {
    currentplayer = player2Name
    currentplayer = player2color
    $('h4').text(currentplayer + ' its your turn')
  }
})

//
//
// $('.board button').on('click',function(){
//   // This is the Column Number (starts at zero):
//   console.log('This is the Column:');
//
//   console.log($(this).closest("td").index());
//   // This is the Row Number:
//   console.log("This is the Row:");
//   console.log($(this).closest("tr").index());
//   console.log('\n');
//   // This is a way to grab a particular cell (replace):
//   // $('table').eq(rowIndex).find('td').eq(colIndex)
// });
//
// // Change color on click
// $('.board button').on('click',function() {
//   if($(this).css('background-color') === 'rgb(51, 51, 51)'){
//     $(this).css('background-color','rgb(86, 151, 255)');
//   }else if ($(this).css('background-color') === 'rgb(86, 151, 255)'){
//     $(this).css('background-color','rgb(237, 45, 73)');
//   }else{
//     $(this).css('background-color','rgb(51, 51, 51)');
//   }
// });
