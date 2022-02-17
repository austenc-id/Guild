const useColor = document.getElementById("use-color").innerText;
if (useColor === "True") {
  cascadeColors();
}

function cascadeColors(){
    const color = document.getElementById("fav-color").innerText;
    const links = document.getElementsByTagName("a");
    setColors(links, color);
    const color_ocean = getComputedStyle(
      document.documentElement
    ).getPropertyValue("--ocean");
    const color_void = getComputedStyle(
      document.documentElement
    ).getPropertyValue("--void");
    document.documentElement.style.setProperty("--wave", color_ocean);
    document.documentElement.style.setProperty("--ocean", color_void);
    document.documentElement.style.setProperty("--void", color);
  }
  function setColors(elements, color) {
    for (let i = 0; i < elements.length; i++) {
      elements.item(i).style.color = color;
    }
  }