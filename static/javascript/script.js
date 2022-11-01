function validation(){
    var name=document.signupForm.username.value; 
    if (name==null || name==""){  
        alert("Name can't be blank");  
        return false;  
    }
    // var flag=true
    // username = document.getElementById("username");
    // inputs = document.getElementsByTagName("input");
    // console.log(inputs[0].value.length());
    // if(inputs[0].value.length()<3){
    //     inputs[0].style.bordercolor="red";
    //     flag=false;
    //     username.innerHTML="username must contain more than 3 words";
    // }
    console.log("Hello world");
}