function checkPassword() {

    let password = document.getElementById("password").value;
    let score = 0;

    if(password.length >= 8)
        score++;

    if(/[A-Z]/.test(password))
        score++;

    if(/[a-z]/.test(password))
        score++;

    if(/[0-9]/.test(password))
        score++;

    if(/[!@#$%^&*(),.?":{}|<>]/.test(password))
        score++;

    let result = document.getElementById("result");

    if(score <= 2){
        result.innerHTML = "Weak Password ❌";
        result.style.color = "red";
    }
    else if(score <= 4){
        result.innerHTML = "Medium Password ⚠️";
        result.style.color = "orange";
    }
    else{
        result.innerHTML = "Strong Password ✅";
        result.style.color = "green";
    }
}
