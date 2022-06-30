import data from './data.json' assert {type: "json"};

window.addEventListener("load",(event)=>{
    document.getElementById('costn').onchange = function de(){
        console.log(data);
    }

})


// console.log(data);