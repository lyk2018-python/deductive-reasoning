  window.onload = showErrorDiv;
  function showErrorDiv(){
    var error = document.getElementById('errorForPythonCheck').innerHTML;
    if(error==''){
      document.getElementById('errorForPythonCheck').style.display = 'none';
    }
    else{
      document.getElementById('errorForPythonCheck').style.display = '';
    }
  }
  function onInputTextValueChange(){
    //Boolean Python
    var is_universal_major = document.getElementById('id_is_universal_major').value;
    var is_affirmative_major = document.getElementById('id_is_affirmative_major').value;
    var is_universal_minor = document.getElementById('id_is_universal_minor').value;
    var is_affirmative_minor = document.getElementById('id_is_affirmative_minor').value;
    var is_universal_conclusion = document.getElementById('id_is_universal_conclusion').value;
    var is_affirmative_conclusion = document.getElementById('id_is_affirmative_conclusion').value;

    //Boolean Js
    var is_universal_majorJS = convertToJSBoolean(is_universal_major);
    var is_affirmative_majorJS = convertToJSBoolean(is_affirmative_major);
    var is_universal_minorJS = convertToJSBoolean(is_universal_minor);
    var is_affirmative_minorJS = convertToJSBoolean(is_affirmative_minor);
    var is_universal_conclusionJS = convertToJSBoolean(is_universal_conclusion);
    var is_affirmative_conclusionJS = convertToJSBoolean(is_affirmative_conclusion);

    //Conclusions
    var majorConclusionType = getConclusionType(is_universal_majorJS, is_affirmative_majorJS);
    var minorConclusionType = getConclusionType(is_universal_minorJS, is_affirmative_minorJS);
    var conclusionConclusionType = getConclusionType(is_universal_conclusionJS, is_affirmative_conclusionJS);
    var isValid = isConclusionValid(majorConclusionType, minorConclusionType, conclusionConclusionType);

    //Textfields
    var major_subject = document.getElementById('id_subject_major').value;
    var major_predicate = document.getElementById('id_predicate_major').value;
    var minor_subject = document.getElementById('id_subject_minor').value;
    var minor_predicate = document.getElementById('id_predicate_minor').value;

    //Decide whether button should be disabled or not according to the inputs
    if (major_subject == "" || major_predicate == "" || minor_subject == "" || minor_predicate == "") {
      document.getElementById("buttonSubmit").disabled = true;
      if (!isValid) {
        document.getElementById("invalidArg").style.display = '';
        document.getElementById("buttonSubmit").disabled = true;
      }
      else{
        document.getElementById("invalidArg").style.display = 'none';
      }
    }
    else{
      document.getElementById("buttonSubmit").disabled = false;
      if (isValid) {
        document.getElementById("invalidArg").style.display = 'none';
      }
      else{
        document.getElementById("invalidArg").style.display = '';
        document.getElementById("buttonSubmit").disabled = true;
      }
    }
  }

  //Convert method
  function convertToJSBoolean(boolToConvert){
    if (boolToConvert == 'True'){
      return true;
    }
    else{
      return false;
    }
  }

  //Decision table
  function isConclusionValid(major, minor, conclusion){
    var isValid;
    if (major == "A" && minor == "A" && conclusion == "A") {
      document.getElementById("conclusionName").innerHTML = "Conclusion Form: \"Barbara\"";
      isValid = true;
    }
    else if (major == "E" && minor == "A" && conclusion == "E"){
      document.getElementById("conclusionName").innerHTML = "Conclusion Form: \"Cesare\"";
      isValid = true;
    }
    else if (major == "A" && minor == "I" && conclusion == "I"){
      document.getElementById("conclusionName").innerHTML = "Conclusion Form: \"Datisi\"";
      isValid = true;
    }
    else if (major == "E" && minor == "I" && conclusion == "O"){
      document.getElementById("conclusionName").innerHTML = "Conclusion Form: \"Ferison\"";
      isValid = true;
    }
    else if (major == "A" && minor == "E" && conclusion == "O"){
      document.getElementById("conclusionName").innerHTML = "Conclusion Form: \"Camestros\"";
      isValid = true;
    }
    else if (major == "A" && minor == "O" && conclusion == "O"){
      document.getElementById("conclusionName").innerHTML = "Conclusion Form: \"Baroco\"";
      isValid = true;
    }
    else if (major == "O" && minor == "A" && conclusion == "O"){
      document.getElementById("conclusionName").innerHTML = "Conclusion Form: \"Bocardo\"";
      isValid = true;
    }
    else if (major == "E" && minor == "A" && conclusion == "O"){
      document.getElementById("conclusionName").innerHTML = "Conclusion Form: \"Celaront\"";
      isValid = true;
    }
    else if (major == "A" && minor == "E" && conclusion == "E"){
      document.getElementById("conclusionName").innerHTML = "Conclusion Form: \"Calemes\"";
      isValid = true;
    }
    else if (major == "I" && minor == "A" && conclusion == "I"){
      document.getElementById("conclusionName").innerHTML = "Conclusion Form: \"Disamis\"";
      isValid = true;
    }
    else{
      document.getElementById("conclusionName").innerHTML = "Conclusion Form: None";
      isValid = false;
    }
    if (document.getElementById("conclusionName").innerHTML.includes("None")) {
      document.getElementById("conclusionName").style.color="rgb(255, 106, 96)";
    }
    else{
      document.getElementById("conclusionName").style.color="green";
    }
    return isValid;
  }
  function getConclusionType(universal, affirmative){
    if(universal == true && affirmative == true){
      return "A";
    }
    else if (universal == true && affirmative == false){
      return "I";
    }
    else if (universal == false && affirmative == true){
      return "E";
    }
    else{
      return "O";
    }
  }

  //Put elements in SelectOneMenus
  function getElements(){
    var subject_conclusion_select_items = document.getElementById('id_subject_conclusion');
    var predicate_conclusion_select_items = document.getElementById('id_predicate_conclusion');
    subject_conclusion_select_items.innerHTML = '';
    predicate_conclusion_select_items.innerHTML = '';
    var major_subject = document.getElementById('id_subject_major').value;
    var major_predicate = document.getElementById('id_predicate_major').value;
    var minor_subject = document.getElementById('id_subject_minor').value;
    var minor_predicate = document.getElementById('id_predicate_minor').value;
    var subject_conclusion_select_items = document.getElementById('id_subject_conclusion');
    if(major_subject != null && major_subject != '' && subject_conclusion_select_items.innerHTML.indexOf('>'+major_subject+'<') == -1){
      subject_conclusion_select_items.innerHTML += '<option>' + major_subject + '</option>';
      predicate_conclusion_select_items.innerHTML += '<option>' + major_subject + '</option>';
    }
    if(major_predicate != null && major_predicate != '' && subject_conclusion_select_items.innerHTML.indexOf('>'+major_predicate+'<') == -1){
      subject_conclusion_select_items.innerHTML += '<option>' + major_predicate + '</option>';
      predicate_conclusion_select_items.innerHTML += '<option>' + major_predicate + '</option>';
    }
    if(minor_subject != null && minor_subject != '' && subject_conclusion_select_items.innerHTML.indexOf('>'+minor_subject+'<') == -1){
      subject_conclusion_select_items.innerHTML += '<option>' + minor_subject + '</option>';
      predicate_conclusion_select_items.innerHTML += '<option>' + minor_subject + '</option>';
    }
    if(minor_predicate != null && minor_predicate != '' && subject_conclusion_select_items.innerHTML.indexOf('>'+minor_predicate+'<') == -1){
      subject_conclusion_select_items.innerHTML += '<option>' + minor_predicate + '</option>';
      predicate_conclusion_select_items.innerHTML += '<option>' + minor_predicate + '</option>';
    }
    onInputTextValueChange();
  }