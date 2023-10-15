
let submit = document.querySelector("#submit")
let guess = document.querySelector("#guess")
let timer = document.querySelector('#timer')
good_guesses = new Set() //incomplete


let score = 0
function add_score(word) {
    score += word.length + 1
    scoreEl = document.querySelector('#score').innerHTML = `Current Score: ${score}`
}

let sec = 60;
time = setInterval(() => {
    timer.innerHTML = `Time left: ${sec} secs`;
    sec--

    if (sec < 0) {
        clearInterval(time)
        submit.remove()
        guess.placeholder = 'no guess allowed'
    }


}, 1000)

async function submit_form(event){
    event.preventDefault()
    let guess_val = guess.value
    let response = await axios.get("http://127.0.0.1:5000/guesses", {params: {guess:guess_val}})
    let res = response.data.res
    let p = document.querySelector('#pEl').innerHTML = `your guess is ${res}`

  
    if (res == 'ok') {
        add_score(res)
        good_guesses.add(res)
    } 
}

submit.addEventListener("click", submit_form)



