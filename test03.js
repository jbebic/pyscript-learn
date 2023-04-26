var jzb;
function ProcessFile(){
    let file = document.getElementById("file_input").files[0];
    if (file) {
        var reader = new FileReader();
        reader.readAsText(file, "UTF-8");
        reader.onload = function (evt) {
            // document.getElementById("fileContents").innerHTML = evt.target.result;
            plot_w_python = pyscript.interpreter.globals.get('plot_w_python');
            let temp = plot_w_python(evt.target.result);
            // jzb = temp;
            jzb = temp.toJs();
            // jzb =  temp.getBuffer();
        }
        reader.onerror = function (evt) {
            document.getElementById("fileContents").innerHTML = "error reading file";
        }
    }
}
