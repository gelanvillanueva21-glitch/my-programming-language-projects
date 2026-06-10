window.addEventListener("click", function() {
    console.log("Window");
}, false);

document.addEventListener("click", function() {
    console.log("Document");
}, false)

document.querySelector(".container-box").addEventListener("click", function(e) {
    // e.stopPropagation()
    console.log("Container Box");
}, {once: true})

document.querySelector(".box").addEventListener("click", function() {
    console.log("Box");
}, false)

document.querySelector(".button").addEventListener("click", function(e) {
    e.preventDefault()
    console.log(e.target.innerText = "clicked!");
}, false)