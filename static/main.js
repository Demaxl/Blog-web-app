window.onload = () => {
    for (const btn of document.querySelectorAll(".show-btn")) {
        btn.addEventListener("click", function () {
            let input = document.getElementById(this.dataset.input)       
           
            if (input.type === "password") {
                input.type = "text";
                this.innerHTML = "Hide"
            } else {
                input.type = "password"
                this.innerHTML = "Show"
            }
        })
    }

    // document.getElementById("edit-profile-btn").addEventListener("click", editProfile)
}


function registerForm(form) {
    if (form['password'].value !== form['confirm_password'].value) {
        let error = '<div class="invalid-feedback">Passwords must match</div>'
        form.classList.add("was-validated")

        document.getElementById("error-lbl").innerHTML = "Passwords must match"
        return false
    }
}

function editProfile() {
    
}