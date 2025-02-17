document.getElementById("myButton").addEventListener("click", () => {
    document.getElementById("header").style.color = "green";
    console.log("you hit the button");
}
);


function validateForm() {
    const password = document.forms[0].elements[1].value;
    let hasUpper = false;
    let hasLower = false;
    for (let i = 0; i < password.length; i++) {
        if (password[i] === password[i].toUpperCase()) {
            hasUpper = true;
        }
        if (password[i] === password[i].toLowerCase()) {
            hasLower = true;
        }
    }
    if (hasUpper && hasLower) {
        return true;
    }
    alert("Password must contain an upper and lower case character");
    return false;
}