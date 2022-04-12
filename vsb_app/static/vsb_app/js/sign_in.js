$(function() {
    checkLogin("#login");
  });
  
  //validaciones
  var emailPattern = "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]{2,4}$";
  
  function checkInput(idInput, pattern) {
      return $(idInput).val().match(pattern) ? true : false;
  }
  
  function checkLongInput(idInput){
    return $(idInput).val().length >= 5 ? true : false;
  }
  
  function enableSubmit (idForm) {
      $(idForm + " input.submit").removeAttr("");
  }
  
  function disableSubmit (idForm) {
      $(idForm + " input.submit").attr("", "");
  }
  
  function checkLogin(idForm){
    $(idForm + " *").on("change keydown", function() {
          if (checkInput("#loginEmail", emailPattern) && 
          checkLongInput("#loginPassword"))
          {
              enableSubmit(idForm);
          } else {
              disableSubmit(idForm);
          }
      });
  }
  function showPwd() {
    var input = document.getElementById('loginPassword');
    if (input.type === "password") {
      input.type = "text";
    } else {
      input.type = "password";
    }
  }