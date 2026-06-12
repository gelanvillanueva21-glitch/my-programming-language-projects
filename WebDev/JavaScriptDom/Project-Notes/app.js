
// VARIABLES

const searchBtn = document.getElementById('search-note');
const addBtn = document.getElementById('add-note');
const deleteBtn = document.getElementById('delete-note');
const saveBtn = document.getElementById('save-note');
const windowSearch = document.getElementById('window-box-search');
const windowTitle = document.getElementById('window-title-box');
let savedList = document.getElementById('saved-note-list');

const searchInput = document.getElementById('search-note-title');
const searchTitleBtn = document.getElementById('search');

const titleInput = document.getElementById('add-notes-title');
const confirmBtn = document.getElementById('confirm-button');


// WINDOW POP UP COMPONENTS

searchBtn.addEventListener('click', function(e){
    e.stopPropagation();
    windowSearch.style.display = 'block';

});

addBtn.addEventListener('click', function(e) {
    e.stopPropagation();
    windowTitle.style.display = 'block';

})


// SEARCH NOTES

searchTitleBtn.addEventListener('click', function(){


    if (searchInput.value === '') {
        alert('You must enter title to search');
    } else {
        let allNotes = document.querySelectorAll('#saved-note-list .list');
        allNotes.forEach(function(note){
            if (searchInput.value === note.innerText) {
                note.style.borderColor = 'blue';
                note.style.borderStyle = 'solid';
                searchInput.value = '';
                windowSearch.style.display = 'none';
            }
        });
    }


});



// ADD NOTES COMPONENTS

confirmBtn.addEventListener('click', function(){


    if (titleInput.value === '') {
        alert('You must Enter a title word');
    } else {
        let li = document.createElement('li');
        li.innerText = titleInput.value;
        li.classList.add('list');
        savedList.appendChild(li);
        titleInput.value = '';
        windowTitle.style.display = 'none';
    }
    

});

window.addEventListener('click', function(e) {

    if (e.target === windowSearch) {
        windowSearch.style.display = 'none';
    } else if (e.target === windowTitle) {
        windowTitle.style.display = 'none';
    }

});




