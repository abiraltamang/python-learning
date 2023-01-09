function onSubmit() {
  un = document.forms["login-form"]["username"].value;
  pd = document.forms["login-form"]["password"].value;
  alert(un + pd);
}

function addNumber() {
  num1 = Number(document.forms["add-numbers"]["num1"].value);
  num2 = Number(document.forms["add-numbers"]["num2"].value);
  op = document.forms["add-numbers"]["op"].value;
  var result;

  // if(op=="+"){
  //     alert(num1 + num2)
  // }
  // else if(op == '-'){
  //     alert(num1-num2)
  // }
  // else if( op == '*'){
  //     alert(num1*num2)
  // }
  // else if( op== "/"){
  //     alert(num1/num2)
  // }
  // else{
  //     alert(error)
  // }

  switch (op) {
    case "+":
      result = num1 + num2;
      break;

    case "-":
      result = num1 - num2;
      break;

    case "*":
      result = num1 * num2;
      break;
    case "/":
      result = num1 / num2;
      break;
    default:
      alert("Error caught");
  }

  document.getElementById("result").innerHTML = result;
}


function multiplicationTableGenerator(){
    let n1 = Number(document.forms['add-numbers']['num1'].value);
    output  = '<table border="1">';

    for (i=1; i<=10 ; i++)
    {
        output += '<tr><td>' + n1 + 'x' + i+ ' = '+(n1*i) + '</td></tr>'; 
    }
    output += '</table>'
    document.getElementById('output').innerHTML = output;
}
