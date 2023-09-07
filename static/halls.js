var cards = document.querySelectorAll('.card');

cards.forEach(function (card) {
  var button = card.querySelector('.card-btn');
  button.addEventListener('click', function() {
    card.classList.toggle('show-text');
  })
})
