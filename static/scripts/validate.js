(() => {
  'use strict'

  const forms = document.querySelectorAll('.needs-validation')

  Array.from(forms).forEach(form => {
    form.addEventListener('submit', event => {
      if (!form.checkValidity()) {
        event.preventDefault()
        event.stopPropagation()
      }

      form.classList.add('was-validated')
    }, false)
  })
})()


// Extra validation
// document.getElementById("form").addEventListener("submit", (event) => {
//     const name = document.getElementById("InputName");
//     const genre = document.getElementById("InputGenre");
//     const platform = document.getElementById("InputPlatform");
//     const file = document.getElementById("InputFile");
//
//
//     if (name.value == "" || genre.value == "" || platform.value == "" || file.value == "") {
//         event.preventDefault()
//         event.stopPropagation()
//         alert("Please Fill Out All Fields")
//         name.required = true;
//         genre.required = true;
//         platform.required = true;
//         file.required = true;
//     }
// })
