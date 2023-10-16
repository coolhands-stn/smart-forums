const form = document.getElementById("form")
const radioButtons = document.querySelectorAll(".radio-container")
const placeholderDescription = document.getElementById("placeholder-description")
const selectedFilterValueInput = document.getElementById("selected_filter_Value")

let placeholderText = ""

const placeholderTextCollection = {
    "description": "Input the textual description of the question",
    "topic": "Search by topic of the questions",
    "time": "X 20XX PX",
    "username": "Search by student or instructor username"
}

radioButtons.forEach((button)=> {
    radioButtons.forEach((btn)=> {
        btn.removeAttribute("id")
    })
    button.addEventListener("Click", ()=> {
        const value = button.getAttribute("value")
        placeholderText = placeholderTextCollection[`${value}`]
        placeholderDescription.textContent =  placeholderText

        button.setAttribute("id", "selected-radio")
    })
})

form.addEventListener("submit", (e)=> {
    e.preventDefault()
    const formData = new FormData(form);  // grab the data inside the form fields
    fetch('/', {   // assuming the backend is hosted on the same server
        method: 'POST',
        body: formData,
    }).then((res)=> {
        console.log(res)
    });
})