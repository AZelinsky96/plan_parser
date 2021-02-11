var path = window.location.pathname;



id_var = setInterval(function() {
    
  if (path == "/upload") {
      enableDisable('file_upload', "file_submit", path)  
  } else if (path == "/process_files" ){
      enableDisable('file_output_name', 'file_output_button', path)
  }
  
}, 500);


function enableDisable (tag_1, tag_2, path) {
  var input_object = document.getElementById(tag_1)
  var button_object = document.getElementById(tag_2);
  if (path == "/upload") {
    comparison(input_object.files.length, 0, button_object);
  } else if (path == "/process_files") {
    comparison(input_object.value, "", button_object);
  } else {
    console.log("Falling through");
  }
};


function comparison(first_element, second_element, button_object) {
  if (first_element != second_element) {
    button_object.disabled = false;
    clearInterval(id_var);
  }else {
    button_object.disabled = true;
  };
};
