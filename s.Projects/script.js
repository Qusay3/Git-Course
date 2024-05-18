let score = 0;
let currentQuestion = 0;
let questions = [];

function startTest() {
  const username = document.getElementById('username').value;
  if (username === '') {
    alert('Please enter your name.');
    return;
  }
  document.getElementById('question').innerHTML = 'Loading...';
  document.getElementById('answer').value = '';
  score = 0;
  currentQuestion = 0;
  document.getElementById('score').innerHTML = '';
  document.getElementById('result').innerHTML = '';
  fetchQuestions();
}

function fetchQuestions() {
  // Fetch questions from an API or define them locally
  // For simplicity, let's define questions locally
  questions = [
    { num1: randomNumber(), num2: randomNumber(), operator: '+' },
    { num1: randomNumber(), num2: randomNumber(), operator: '-' },
    { num1: randomNumber(), num2: randomNumber(), operator: '*' },
    { num1: randomNumber(), num2: randomNumber(), operator: '/' }
  ];
  displayQuestion();
}

function displayQuestion() {
  const question = questions[currentQuestion];
  document.getElementById('question').innerHTML = `What is ${question.num1} ${question.operator} ${question.num2}?`;
}

function checkAnswer() {
  const userAnswer = parseFloat(document.getElementById('answer').value);
  const question = questions[currentQuestion];
  let correctAnswer;
  switch (question.operator) {
    case '+':
      correctAnswer = question.num1 + question.num2;
      break;
    case '-':
      correctAnswer = question.num1 - question.num2;
      break;
    case '*':
      correctAnswer = question.num1 * question.num2;
      break;
    case '/':
      correctAnswer = question.num1 / question.num2;
      break;
  }
  if (userAnswer === correctAnswer) {
    document.getElementById('result').innerHTML = 'Correct!';
    score++;
  } else {
    document.getElementById('result').innerHTML = 'Incorrect!';
  }
  currentQuestion++;
  if (currentQuestion < questions.length) {
    displayQuestion();
  } else {
    showScore();
  }
}

function showScore() {
  document.getElementById('score').innerHTML = `Your final score is: ${score}`;
}

function randomNumber() {
  return Math.floor(Math.random() * 10) + 1;
}
