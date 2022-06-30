var d13 = document.getElementById('costn13')

    d13.addEventListener('change', function(evt) {
        console.log("listned");
        var selectedValue = costn13.value;
        console.log(selectedValue);
        var e = document.getElementById('costc13')
        
        c = selectedValue
        readTextFile(url, function(text) {
            
            var data = JSON.parse(text);
            c = data[c - 1][1]
            console.log(data);
            console.log(data[1]);
            e.value = c
        });
    });
    setTimeout(() => {
        var event = new Event('change');
        d13.dispatchEvent(event);

    }, 1000)