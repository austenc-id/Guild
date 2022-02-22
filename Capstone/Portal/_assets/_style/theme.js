defaultTheme()

const useColor = document.getElementById("use-color").innerText;
if (useColor === "True") {
  const color = document.getElementById("fav-color").innerText;
  const links = document.getElementsByTagName("a");
  setColors(links, color);
}

function defaultTheme(){
  document.body.classList.add('bg-void')
  document.body.classList.add('font-acme')
  document.getElementById('block-index').classList.add('bg-ocean')
  document.getElementById('block-index').classList.add('text-stone')
  document.getElementById('main').classList.add('bg-wave')
  document.getElementById('header').classList.add('border-b2-void')
  document.getElementById('footer').classList.add('border-t2-void')
  const LINKS = document.getElementsByTagName('a')
  const FORMS = document.getElementsByTagName('form')
  const TITLE = document.getElementById('site-title')
  setColorClasses(LINKS, "text-sand")
  setColorClasses(FORMS, "border-2-void")
  TITLE.classList.add('text-stone')
}

function setColors(elements, color) {
    console.log(elements)
    for (let i = 0; i < elements.length; i++) {
      let elemID = elements.item(i).id
      if (elemID != 'site-title'){
      elements.item(i).style.color = color;
      }
    }
  }
function setColorClasses(elements, className) {
    // console.log(elements)
    for (let i = 0; i < elements.length; i++) {
      let elemID = elements.item(i).id
      if (elemID != 'site-title'){
        elements.item(i).classList.add(className)
    }
    }
  }