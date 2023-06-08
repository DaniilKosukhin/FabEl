function buttonPressed() {
    let textField = document.querySelector("#name");
    let modelField = document.querySelector("#models");
    let controllerField = document.querySelector("#controllers");
    let sliderEl = document.querySelector("#number");


    let item = {
        name: textField.value,
        model: modelField.value,
        controller: controllerField.value,
        number: sliderEl.value,

    }

    fetch(`http://127.0.0.1:8000/save`, {
       method: 'POST',
       headers: {'Content-Type': 'application/json'},
       body: JSON.stringify(item)
   })
  .then(response => response.json())
  .then(data => console.log(data));
}

function allitems() {
    let container = document.querySelector()
}