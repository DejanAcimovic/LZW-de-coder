
// Function to download data to a file
function download(data, filename, type) {
    dat = data.replace("None ", "")
    var file = new Blob([dat], {type: type,endings:'native'});
    if (window.navigator.msSaveOrOpenBlob) // IE10+
        window.navigator.msSaveOrOpenBlob(file, filename);
    else { // Others
        var a = document.createElement("a"),
                url = URL.createObjectURL(file);
        a.href = url;
        a.download = filename;
        document.body.appendChild(a);
        a.click();
        setTimeout(function() {
            document.body.removeChild(a);
            window.URL.revokeObjectURL(url);  
        }, 0); 
    }
}


function compress(){

    text = document.getElementById("textarea1").value;
    console.log("text je :"+text);
    
    $.ajax({
        type: "POST",
        url: "/compress",
        data: JSON.stringify({"text":text}),
        success: (response)=>{document.getElementById("textarea2").value = response;},
        error: (error) => {document.getElementById("textarea2").value="UPS SOMETHING BAD HAPPENED!"},
        contentType: "application/json; charset=utf-8",
      });

    if(document.getElementById("file").value !== null){
        var reader = new FileReader(); 
      
        reader.onload = function(e) {
            var fileText = reader.result;
            
            $.ajax({
                type: "POST",
                url: "/compress",
                data: JSON.stringify({"text":fileText}),
                success: (response)=>{download(response, "compressed.txt", "text")},
                contentType: "application/json; charset=utf-8",
              });
        }
  
        reader.readAsText(document.getElementById("file").files[0]);
    }  
}

function decompress(){
    text = document.getElementById("textarea1").value;
    console.log("text je :"+text);

    $.ajax({
        type: "POST",
        url: "/decompress",
        data: JSON.stringify({"text":text}),
        success: (response)=>{document.getElementById("textarea2").value = response;},
        error: (error) => {document.getElementById("textarea2").value="UPS SOMETHING BAD HAPPENED!"},
        contentType: "application/json; charset=utf-8",
      });

      if(document.getElementById("file").value !== null){
        var reader = new FileReader(); 

      
        reader.onload = function(e) {
            var fileText = reader.result;
            
            console.log(fileText)
            $.ajax({
                type: "POST",
                url: "/decompress",
                data: JSON.stringify({"text":fileText}),
                success: (response)=>{download(response, "compressed.txt", "text/plain;charset=utf-8")},
                contentType: "application/json; charset=utf-8",
              });
        }
  
        reader.readAsText(document.getElementById("file").files[0]);
    } 
}