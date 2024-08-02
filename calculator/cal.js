let p;
function addToInput(value){
    p= document.getElementById('input').value += value;
 };

 function remove(){
    p=document.getElementById('input').value = "";
    
};
function calculate(){
    const display =document.getElementById('input');
    try {
        display.value =eval(display.value);
    }catch(e){
        display.value="Error";
    }
}
 