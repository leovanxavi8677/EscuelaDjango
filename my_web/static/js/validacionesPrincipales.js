function ValidateAlpha(evt)
    {
        var keyCode = (evt.which) ? evt.which : evt.keyCode
        if ((keyCode < 65 || keyCode > 90) && (keyCode < 97 || keyCode > 123) && keyCode != 32)

        return false;
            return true;
    }

function isNumberKey(evt){  <!--Function to accept only numeric values-->
    //var e = evt || window.event;
	var charCode = (evt.which) ? evt.which : evt.keyCode
    if (charCode != 46 && charCode > 31 && (charCode < 48 || charCode > 57))
        return false;
        return true;
	}

function lettersAndNumbers(evt){
    var regex = new RegExp("^[a-zA-Z0-9 ]+$");   
    var charCode = String.fromCharCode(!evt.charCode ? evt.which : evt.charCode)
    if (regex.test(charCode)){
        return true
    }
    else{
        return false
    }
    

       


}