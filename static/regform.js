function validateform() {
    var name = document.myform.name.value;
    var password = document.myform.password.value;
    var password1 = document.myform.password1.value;
    var phno = document.myform.phno.value;
    var email = document.myform.email.value;
    var city = document.myform.city.value;
    var state = document.myform.state.value;

    if (name == null || name == "") {
        alert("Name can't be blank");
        return false;
    }

    if (name.length != "") {
        var regex = /^(?=.[A-z])/;
        if (regex.test(name) === false) {
            alert("Please enter a valid Name");
            return false;
        }
    }
    if (password == "") {
        alert("Please enter your password");
        password.focus();
        return false;
    }
    if (password != password1) {
        alert("Password mismatch");
        return false;
    }
    if (password.length != "") {
        var regex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])(?=.{8,})/;
        if (regex.test(password) === false) {
            alert("Please enter a valid pwd");
            return false;
        }
    }
    if (city.length != "") {
        var regex = /^(?=.[A-z])/;
        if (regex.test(city) === false) {
            alert("Please enter a valid City Name");
            return false;
        }
    }

    if (state.length != "") {
        var regex = /^(?=.[A-z])/;
        if (regex.test(state) === false) {
            alert("Please enter a valid State Name");
            return false;
        }
    }

    if (phno.length != 10) {
        alert("Please enter a valid phone number");
        return false;
    }

    if (/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(email)) {
        return (true);
    }
    else {
        alert("You have entered an invalid email address!");
        return (false);
    }

}


function passwordEyeCheck() {

    const container = document.querySelector(".container"),
        pwShowHide = document.querySelectorAll(".showHidePw"),
        pwFields = document.querySelectorAll(".password");

    pwShowHide.forEach(eyeIcon => {
        eyeIcon.addEventListener("click", () => {
            pwFields.forEach(pwField => {
                if (pwField.type === "password") {
                    pwField.type = "text";

                    pwShowHide.forEach(icon => {
                        icon.classList.replace("uil-eye-slash", "uil-eye");
                    })
                } else {
                    pwField.type = "password";

                    pwShowHide.forEach(icon => {
                        icon.classList.replace("uil-eye", "uil-eye-slash");
                    })
                }
            })
        })
    })

}
