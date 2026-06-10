// // DOM MANIPULATION

// const title = document.getElementById('main-heading');


// title.style.color = 'White'
// title.style.background = 'Black'
// title.style.padding = '5px'


// // const listItem = document.querySelectorAll('.list-items')

// // for ( i = 0; i < listItem.length; i++) {
// //     listItem[i].style.fontSize = '3rem'
// // }

// // console.log(listItem);


// const ul = document.querySelector('ul')
// const li = document.createElement('li')

// ul.append(li)

// const firstListItem = document.querySelector('.list-items')


// // li.setAttribute('class', 'list-items')
// li.innerText = 'Spider-Man 6'

// // const listItem = document.getElementsByClassName('list-items')

// li.classList.add('list-items')
// // li.remove()


let ul = document.querySelector('ul')

console.log(ul.childNodes);

ul.children[3].style.backgroundColor = 'Blue'

const div = document.querySelector('div')

console.log(div.childNodes);
console.log(div.childNodes[1]);

