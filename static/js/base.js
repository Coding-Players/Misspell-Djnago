// =================[This section is for effectiveness of MenuBar]==================
let menu = document.getElementById("NavMenu");
let nave = document.getElementById("nav");
let exit = document.getElementById("Exit-from-Navbar");

if(menu != null){
    menu.addEventListener('click', function (e) {
        nave.classList.toggle('hideMobile');
        exit.classList.toggle('hideMobile');
        e.preventDefault();
    });
    exit.addEventListener('click', function (e) {
        nave.classList.add('hideMobile');
        exit.classList.add('hideMobile');
        e.preventDefault();
    });
}


// ===============[That section control Hide and show of Scroll Menu]==================
var prevScrollpos = window.pageYOffset;
window.onscroll = function () {
    var currentScrollpos = window.pageYOffset;
    if (prevScrollpos > currentScrollpos) {
        document.getElementById("Scroll-MenuBar").style.top = "50px";
    }
    else {
        document.getElementById("Scroll-MenuBar").style.top = "-50px";
    }
    prevScrollpos = currentScrollpos;
}


