// password validation
document.querySelector("#pass1").addEventListener("keypress" , function(e){
  if (document.getElementById("pass1").value.length<8) {
      document.querySelector("#mainpasswordvalid").setAttribute("style" , "color:#ff0000");
      document.querySelector("#mainpasswordvalid").innerHTML = "* Short password *";
      // document.querySelector("#submit").setAttribute("disabled" , true);
      validate_data.password = false;
  }
  else {
      document.querySelector("#mainpasswordvalid").setAttribute("style" , "display:none;");
      // document.querySelector("#submit").setAttribute("disabled" , true);
      validate_data.password = true;
  }
});
document.querySelector("#pass2").addEventListener("change" , function(e){
  if (document.getElementById("pass2").value != document.getElementById("pass1").value) {
      document.querySelector("#passwordvalid").setAttribute("style" , "color:#ff0000");
      document.querySelector("#passwordvalid").innerHTML = "* Password do not match *";
      // document.querySelector("#submit").setAttribute("disabled" , true);
      validate_data.password = false;
  }
  else {
      document.querySelector("#passwordvalid").setAttribute("style" , "display:none;");
      // document.querySelector("#submit").setAttribute("disabled" , true);
      validate_data.password = true;
  }
});
