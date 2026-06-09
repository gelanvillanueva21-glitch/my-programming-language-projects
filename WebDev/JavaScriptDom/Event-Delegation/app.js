
document.querySelector('.box-list').addEventListener('click', function(e) {
    console.log(e.target.getAttribute('id') + " is clicked");
    const target = e.target
    if (target.matches('li')) {
        target.style.color = 'white'
        target.style.backgroundColor = 'black'
    }
})

const sport = document.querySelector('.box-list')
const newSport = document.createElement('li')

newSport.innerText = 'Boxing'
newSport.setAttribute('class', 'list')
newSport.setAttribute('id', 'boxing')

sport.append(newSport)