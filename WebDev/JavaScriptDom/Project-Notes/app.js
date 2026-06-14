

// VARIABLES

const textArea = document.getElementById('note-content');
const searchBtn = document.getElementById('search-note');
const addBtn = document.getElementById('add-note');
const deleteBtn = document.querySelector('.delete-note');
const saveBtn = document.getElementById('save-note');
const windowSearch = document.getElementById('window-box-search');
const windowTitle = document.getElementById('window-title-box');
const windowDelete = document.getElementById('window-delete-confirm');
let savedList = document.getElementById('saved-note-list');

const searchInput = document.getElementById('search-note-title');
const searchTitleBtn = document.getElementById('search');

const titleInput = document.getElementById('add-notes-title');
const confirmBtn = document.getElementById('confirm-button');

let headingTitle = document.getElementById('heading-title');
let deleteNoteBtn = document.querySelectorAll('.delete-btn');
let activeNote = null;


// LOCAL STORAGE FILE

function saveNotesStorage() {
    let allNotes = document.querySelectorAll('.list');
    let notesArray = []

    allNotes.forEach(function(note){
        notesArray.push({
            id: note.id,
            content: note.dataset.content
        });
    });
    localStorage.setItem('note', JSON.stringify(notesArray));
}


// DISPLAY LIST

let notes = JSON.parse(localStorage.getItem('note')) || [];

notes.forEach(function(note) {

    let li = document.createElement('li');
    li.classList.add('list');
    li.id = note.id;
    li.innerText = note.id;
    li.dataset.content = note.content;
    savedList.appendChild(li);

});



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


let highlightedNote = null;


searchTitleBtn.addEventListener('click', function(){


    if (highlightedNote) {
        highlightedNote.style.border = 'none';
    }

    if (searchInput.value === '') {
        alert('You must enter title to search');
    } else {
        const allNotes = document.querySelectorAll('.list');
        allNotes.forEach(function(note){
            if (searchInput.value.toLowerCase() === note.innerText.toLowerCase()) {
                note.style.borderColor = 'blue';
                note.style.borderStyle = 'solid';
                searchInput.value = '';
                windowSearch.style.display = 'none';
                activeNote = note;

                headingTitle.innerText = note.innerText;
                textArea.value = note.dataset.content;
                highlightedNote = note;
            }
        });
    }


});



// ADD NOTES COMPONENTS



confirmBtn.addEventListener('click', function(){

    let allNotes = document.querySelectorAll('.list');
    if (titleInput.value === '') {
        alert('You must Enter a title word');
    } else {
        var isExist = false;
        allNotes.forEach(function(note) {
            if (note.innerText.toLowerCase() === titleInput.value.toLowerCase()) {
                isExist = true;
            }
        });
        if (!isExist) {
            let li = document.createElement('li');
            li.innerText = titleInput.value;
            li.classList.add('list');
            li.id = titleInput.value;
            li.dataset.content = '';
            savedList.appendChild(li);
            titleInput.value = '';
            windowTitle.style.display = 'none';
            saveNotesStorage(); 
        } else {
            alert(`${titleInput.value} is Already Exist`);
        }
    }

});

window.addEventListener('click', function(e) {

    if (e.target === windowSearch) {
        windowSearch.style.display = 'none';
    } else if (e.target === windowTitle) {
        windowTitle.style.display = 'none';
    }

});


// ACTIVE NOTES



window.addEventListener('click', function(e) {

    const allNotes = document.querySelectorAll('.list');
    allNotes.forEach(function(note) {
        if (e.target === note) {
            headingTitle.innerText = note.innerText;
            textArea.value = note.dataset.content;
            activeNote = note;
        }
    })
});


saveBtn.addEventListener('click', function(){
    if (activeNote) {
        activeNote.dataset.content = textArea.value;
        saveNotesStorage();
    }
});


// DELETE NOTES

let hasDeleteBtn = true;


deleteBtn.addEventListener('click', function(){

    const allNotes = document.querySelectorAll('.list');
    if (hasDeleteBtn)  {
        allNotes.forEach(function(note){
            let image = document.createElement('img');
            image.src = 'Image/trash-circle.svg';
            image.style.width = '30px';

            const button = document.createElement('button');
            button.classList.add('delete-note', 'delete-btn');
            button.appendChild(image);
            note.appendChild(button);
        })
        hasDeleteBtn = false;
    } else {
        const allBtn = document.querySelectorAll('.delete-btn');
        allBtn.forEach(function(note) {
            note.remove();
        })
        hasDeleteBtn = true;
    }
});


// function isDeleteBtn(button) {
//     deleteNoteBtn.forEach(function(noteBtn) {
//         if (button === noteBtn.parentElement.id) {
//             return true;
//         }
//     })
// }

let activeId = null;
const noBtn = document.getElementById('no');
const confirmButton = document.getElementById('confirm');


window.addEventListener('click', function(e) {

    let trashBtn = e.target.closest('.delete-btn');

    if(trashBtn) {
        activeId = trashBtn.parentElement;
        console.log(activeId);
        windowDelete.style.display = 'block';
    }
});

noBtn.addEventListener('click', function(){
    windowDelete.style.display = 'none';
});


confirmButton.addEventListener('click', function(){

    const allNotes = document.querySelectorAll('.list');
    allNotes.forEach(function(note){
        if (note.id === activeId.id) {
            note.remove();
            windowDelete.style.display = 'none';
        }
    });
    saveNotesStorage();

});







