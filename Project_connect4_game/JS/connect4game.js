var player1 = prompt('Player 1: Enter your name:')
// var player2Name = prompt('Player 2: Enter your name:')

var player1color = 'rgb(12, 24, 247)'
var player2color = 'rgb(247, 29, 12)'

// define horizontal win
// define vertical win
// define diagonal win
// define drop take the player1Name and player1color
//
// define last empty
//

// Start with Player One
$('h4').text(player1+": it is your turn, please pick a column to drop your blue chip.");


$('.board button').on('click',function(){
  // This is the Column Number (starts at zero):
  console.log('This is the Column:');
  console.log($(this).closest("td").index());
  // This is the Row Number:
  console.log("This is the Row:");
  console.log($(this).closest("tr").index());
  console.log('\n');
  // This is a way to grab a particular cell (replace):
  // $('table').eq(rowIndex).find('td').eq(colIndex)
});

// Change color on click
$('.board button').on('click',function() {
  if($(this).css('background-color') === 'rgb(51, 51, 51)'){
    $(this).css('background-color','rgb(86, 151, 255)');
  }else if ($(this).css('background-color') === 'rgb(86, 151, 255)'){
    $(this).css('background-color','rgb(237, 45, 73)');
  }else{
    $(this).css('background-color','rgb(51, 51, 51)');
  }
});
