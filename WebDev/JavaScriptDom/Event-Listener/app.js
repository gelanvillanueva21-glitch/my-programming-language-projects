

// const buttonTwo = document.querySelector('.button2')

// function alertButton() {
//     alert('I also love AI makes my job easier')
// }

// buttonTwo.addEventListener("click", alertButton)

// const newBackgroundColor = document.querySelector('.box3')

// function changeBGColor() {
//     newBackgroundColor.style.backgroundColor = 'blue'
// }

// newBackgroundColor.addEventListener("mouseover", changeBGColor);

const revealBtn = document.querySelector('.button2');
const heading = document.querySelector('.example2')
const hiddenText = document.querySelector('.hidden-box');

function revealContent() {
    hiddenText.classList.toggle('active')
    heading.style.marginBottom = '20px'
}

revealBtn.addEventListener('click', revealContent)