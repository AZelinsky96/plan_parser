id_var = setInterval(testInput, 500);

function testInput() {
  var file_input = document.getElementById('file_upload');
  var upload_button = document.getElementById("file_submit");
  console.log("Inside Loop");
  if (file_input.files.length != 0) {
    upload_button.disabled = false;
    clearInterval(id_var);
  }else {
    upload_button.disabled = true;
  };
};

console.log("Outside loop");

