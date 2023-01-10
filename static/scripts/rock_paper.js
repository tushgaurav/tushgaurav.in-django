// Stone Paper Scissors
// User can play this game through the developer console
// User can call rock(), paper() and scissors() by function calls

function computerPlay() {
  let choices = ["rock", "papers", "scissors"];
  let randomIndex = Math.floor(Math.random() * choices.length);
  return choices[randomIndex];
}

function playRound(
  player_one,
  player_two,
  player_one_name = "Computer",
  player_two_name = "User"
) {
  if (player_one == player_two) {
    return "It is a tie!";
  } else if (
    (player_one == "rock" && player_two == "paper") ||
    (player_one == "paper" && player_two == "scissors") ||
    (player_one == "scissors" && player_two == "rock")
  ) {
    return `${player_two_name} wins! ${player_two} beats ${player_one}`;
  } else {
    return `${player_one_name} wins! ${player_one} beats ${player_two}`;
  }
}

function game(playerSelection) {
  let computerSelection = computerPlay();
  console.log(playRound(computerSelection, playerSelection));
}

// using functions as user commands
function rock() {
  console.log(game("rock"));
}

function paper() {
  console.log(game("paper"));
}

function scissors() {
  console.log(game("scissors"));
}

function help() {
  console.log(`
    You can play by calling functions.
    Like if you want to show rock, type rock()
  `);
}

// The console output is formatted using CSS
console.log(
  "%cYou found an easter egg!",
  "background: linear-gradient(90deg, rgba(3,4,94,1) 0%, rgba(9,9,121,1) 35%, rgba(0,212,255,1) 100%); color: white; font-weight: bold; font-size: 1.2em; padding: 1em; border-radius: 500px;"
);

console.log("%cNow you can play Rock, Papers & Scissors", "color: #00FF1F;");
setTimeout(help, 6000);
