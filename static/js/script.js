// ===============================
// CHARACTER COUNTER
// ===============================

const messageBox = document.getElementById("message");
const counter = document.getElementById("count");


if(messageBox && counter){

    messageBox.addEventListener("input", function(){

        counter.innerText = messageBox.value.length;

    });

}




// ===============================
// EXAMPLE MESSAGE AUTO FILL
// ===============================


const examples = document.querySelectorAll(".example");


examples.forEach(function(example){


    example.addEventListener("click", function(){


        if(messageBox){

            messageBox.value = example.innerText;

            counter.innerText = messageBox.value.length;


            messageBox.focus();

        }


    });


});






// ===============================
// LOADING BEFORE PREDICTION
// ===============================


const form = document.getElementById("spamForm");


if(form){


    form.addEventListener("submit", function(){


        const button = form.querySelector("button");


        if(button){


            button.innerHTML =
            "🔍 Analyzing...";


            button.disabled = true;


        }


    });


}






// ===============================
// SCROLL ANIMATION
// ===============================


const cards = document.querySelectorAll(

".feature-card, .stat-card, .step, .ai-card"

);



const observer = new IntersectionObserver(

(entries)=>{


entries.forEach(entry=>{


    if(entry.isIntersecting){


        entry.target.classList.add("show");


    }


});


},

{

threshold:0.2

}

);




cards.forEach(card=>{


    card.classList.add("hidden-card");

    observer.observe(card);


});
