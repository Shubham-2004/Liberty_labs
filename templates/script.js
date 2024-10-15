let cross = document.getElementById("cross");
let side = document.getElementById("side");
let three = document.getElementById("three");

three.addEventListener("click", function(){
    side.className = "sideBar";
});


cross.addEventListener("click", function(){
    side.classList.toggle("sideBar2");
});
