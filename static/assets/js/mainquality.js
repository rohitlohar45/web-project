
    function readTextFile(file, callback) {
        var rawFile = new XMLHttpRequest();
        rawFile.overrideMimeType("application/json");
        rawFile.open("GET", file, true);
        rawFile.onreadystatechange = function() {
            if (rawFile.readyState === 4 && rawFile.status == "200") {
                callback(rawFile.responseText);
            }
        }
        rawFile.send(rawFile.responseText);
    }

//     fields = [
//             'name','details','gradegrp','misc','metalc','costc','metaln','typeo','recovery','metalcn','metalnn',
//             'metaln1','metalc1','metaln2','metalc2','metaln3','metalc3','metaln4','metalc4','metaln5','metalc5',
//             'metaln6','metalc6','metaln7','metalc7','metaln8','metalc8','metaln9','metalc9','metaln10','metalc10',
//             'metaln11','metalc11','metaln12','metalc12','metaln13','metalc13','metaln14','metalc14','metaln15','metalc15',
//             'metaln16','metalc16','metaln17','metalc17','metaln18','metalc18','metaln19','metalc19','metaln20','metalc20',
// ]

    let url = '/static/assets/js/data.json'
    let gradeurl = '/static/assets/js/data_grade.json'
    let yardurl = '/static/assets/js/yard.json'
    let metalurl = '/static/assets/js/data_metal.json'
    var room = 1;
    cmetal = 1;
    m = 101;


    var econtact = document.getElementsByTagName('label');
    console.log(econtact);



    

    
        array = ['c',1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        htmx.onLoad(function(content){
        var supplier = document.getElementById('id_supplier')
        if(supplier){
            
                var supplier = document.getElementById('id_supplier')
                
                    supplier.addEventListener('change', function(evt) {
                        var supplierValue = supplier.value
                        readTextFile(yardurl, function(text) {
                            var data = JSON.parse(text);
                            var options = "<option>SELECT</option>";
                            // console.log(data);
                            if (supplierValue.length == 0) document.getElementById("id_yard").innerHTML = options;
                            for (let i = 0; i < data.length; i++) {
                                if(data[i][0]==supplier.value){
                                    var option = document.createElement("option");
                                    var value = data[i][2]
                                    // console.log("This is $(2)" );
                                    options += `<option value=${value}>` + data[i][1] + "</option>";
                                    console.log(`<option value=${value}>`);
                                }
                                document.getElementById("id_yard").innerHTML = options;
                            }
                            
                                // var yard = document.getElementById('id_yard')
                                // var option = document.createElement("option");
                                // option.setAttribute('id','option')
                                // for (var i = 0; i < data.length; i++) {
                                //     if(data[i][0]==supplier.value){
                                //         option.value = data[i][2];
                                //         console.log(option.value);
                                //         option.innerHTML = data[i][1];
                                //         yard.appendChild(option);
                                //     }
                                // }
                                // var ele = document.getElementById('option')
                                // ele.remove()
                            // if (supplierValue.length == 0) document.getElementById("id_yard").innerHTML = "<option></option>";
                            // else {
                            //     var catOptions = "";
                            //     for (categoryId in data[supplierValue][1]) {
                            //         catOptions += "<option>" + data[supplierValue][1] + "</option>";
                            //     }
                            //     document.getElementById("id_yard").innerHTML = catOptions;
                            // }
                        })
                    });
                // }, false)
                setTimeout(() => {
                var event = new Event('change');
                supplier.dispatchEvent(event);
    
                }, 1000)
        
        }


        var gr = document.getElementById('id_grade')
        if(gr){
        gr.addEventListener("click", function() {
            gr.addEventListener('change', function(evt) {
                // console.log("listned");
                var selectedValue = gr.value;
                // console.log(selectedValue);
                c = selectedValue
                var i= 0
                

                readTextFile(gradeurl, function(text) {
                    var data = JSON.parse(text);
                    while(c!=data[i].pk && i<data.length){
                        c = selectedValue
                        i++;
                    }
                    if(data[i].pk==c){
                        field = data[i].fields
                        for(const i in field){
                            var name = document.getElementById(i)
                            // console.log(field[i]);
                            if(field[i]=="SELECT" || field[i]==0){
                                continue
                            }else{
                                var idf = i.charAt(i.length-1)
                                var ele = document.getElementById(idf)
                                // console.log( i + " " + idf);
                                
                                if(i=='metalc' && field[i]!=0){
                                    ele.removeAttribute('hidden')
                                }else if(i.startsWith('metalc') && field[i]!=0){
                                    var def = 'metalc'+idf
                                    ele.removeAttribute('hidden')

                                }else if(i=='costc' && field[i]!=0){
                                    var ele = document.getElementById('cost')
                                    ele.removeAttribute('hidden')
                                }
                                else if(i.startsWith('costc') && field[i]!=0){
                                    console.log(field[i]);
                                    var ele = document.getElementById('c' + idf)
                                    console.log('c' + idf);
                                    // var def = 'costc'+idf
                                    ele.removeAttribute('hidden')
                                }else{
                                    
                                    // console.log("idhar" + " " + i);
                                    name.style.display = 'inline-block'
                                }
                                name.innerHTML =  field[i]
                                if(i=='typeo'){
                                        if(field[i]==1){
                                            name.innerHTML = 'Ingot'
                                        }else if(field[i]==2){
                                            name.innerHTML = 'Scrap'
                                        }
                                    }
                            }
                        }
                    }
                    
                });
            });
    }, false);
    setTimeout(() => {
        var event = new Event('change');
        gr.dispatchEvent(event);

    }, 1000)
    }
})

    
    var gr = document.getElementById('id_grade')
    
    var btn = document.getElementById('add-metal')
    
    if(btn){
        btn.addEventListener("click", function() {
        var obj = document.getElementById(cmetal)
        //console.log(obj)
        obj.style.display = 'flex';
        obj.setAttribute('class','form-group row')
        cmetal++;
    }, false);
    }


    var metal = document.getElementById('metaln')

    if(metal){

        function call(element){
            readTextFile(metalurl, function(text) {
                var data = JSON.parse(text);
                var options = "<option>SELECT</option>";
                for (let i = 0; i < data.length; i++) {
                    // if(data[i][0]==supplier.value){
                        var option = document.createElement("option");
                        var value = data[i][0]
                        // console.log(value);
                        options += `<option value=${value}>` + data[i][1] + "</option>";
                        // console.log(`<option value=${value}>`);
                        // console.log(options);
                        // console.log(document.getElementById(element));
                    document.getElementById(element).innerHTML = options;
                }
            })
        }
        var element = "metaln"; call(element)
        element = "metalnn"; call(element)

        for (let i = 1; i < 20; i++) {
            var element = ("metaln" +""+ i)
            var a = document.getElementById(element);
            console.log(a);
            call(element)

            
        }
    }



    var d = document.getElementById('costn')
    if(d){
        
        function call(element){
            readTextFile(url, function(text) {
                var data = JSON.parse(text);
                var options = "<option>SELECT</option>";
                for (let i = 0; i < data.length; i++) {
                    // if(data[i][0]==supplier.value){
                        var option = document.createElement("option");
                        var value = i
                        // console.log(value);
                        options += `<option value=${value}>` + data[i][0] + "</option>";
                        // console.log(`<option value=${value}>`);
                        // console.log(options);
                        // console.log(document.getElementById(element));
                    document.getElementById(element).innerHTML = options;
                }
            })
        }
        var element = "costn"; call(element)
        element = "costnn"; call(element)

        for (let i = 1; i < 20; i++) {
            var element = ("costn" +""+ i)
            var a = document.getElementById(element);
            console.log(a);
            call(element)

            
        }



    d.addEventListener("click", function() {

        d.addEventListener('change', function(evt) {
            console.log("listned");
            var selectedValue = costn.value;
            var e = document.getElementById('costc') 

            c = selectedValue
            console.log(c);
            readTextFile(url, function(text) {
                
                var data = JSON.parse(text);
                
                for (let i = 0; i < data.length; i++) {
                    
                    if(data[i][0]==c){
                        c = data[i][1]
                    }   
                }
                e.value = c
                // console.log("jns")
                e.value = data[c][1]
            });
        });
    }, false);
    setTimeout(() => {
        var event = new Event('change');
        d.dispatchEvent(event);

    }, 1000)
}




    var dn = document.getElementById('costnn')
    if(dn){
    dn.addEventListener("click", function() {
    dn.addEventListener('change', function(evt) {
        console.log("listned");
        var selectedValue = costnn.value;
        
        var e = document.getElementById('costcn')
        
        c = selectedValue
        readTextFile(url, function(text) {
            
            var data = JSON.parse(text);
            e.value = data[c][1]
        });
    });
}, false);
    setTimeout(() => {
        var event = new Event('change');
        dn.dispatchEvent(event);

    }, 1000)
    }

    // setTimeout(() => {
    //     var event = new Event('change');
    //     d.dispatchEvent(event);

    // }, 1000)



    var d1 = document.getElementById('costn1')
    if(d1){
    d1.addEventListener("click", function() {
    d1.addEventListener('change', function(evt) {
        console.log("listned");
        var selectedValue = costn1.value;
        
        var e = document.getElementById('costc1')
        
        c = selectedValue
        readTextFile(url, function(text) {
            
            var data = JSON.parse(text);
            e.value = data[c][1]
        });
    });
}, false);
    setTimeout(() => {
        var event = new Event('change');
        d1.dispatchEvent(event);

    }, 1000)
    }

    var d2 = document.getElementById('costn2')
    if(d2){
    d2.addEventListener("click", function() {
    d2.addEventListener('change', function(evt) {
        console.log("listned");
        var selectedValue = costn2.value;
        
        var e = document.getElementById('costc2')
        
        c = selectedValue
        readTextFile(url, function(text) {
            
            var data = JSON.parse(text);
            e.value = data[c][1]
        });
    });
}, false);
    setTimeout(() => {
        var event = new Event('change');
        d2.dispatchEvent(event);

    }, 1000)

    }

    var d3 = document.getElementById('costn3')
    if(d3){
    d3.addEventListener("click", function() {
    d3.addEventListener('change', function(evt) {
        console.log("listned");
        var selectedValue = costn3.value;
        
        var e = document.getElementById('costc3')
        
        c = selectedValue
        readTextFile(url, function(text) {
            
            var data = JSON.parse(text);
            e.value = data[c][1]
        });
    });
}, false);
    setTimeout(() => {
        var event = new Event('change');
        d3.dispatchEvent(event);

    }, 1000)
    }


    var d4 = document.getElementById('costn4')
    if(d4){
    d4.addEventListener("click", function() {
    d4.addEventListener('change', function(evt) {
        console.log("listned");
        var selectedValue = costn4.value;
        
        var e = document.getElementById('costc4')
        
        c = selectedValue
        readTextFile(url, function(text) {
            
            var data = JSON.parse(text);
            e.value = data[c][1]
        });
    });
}, false);
    setTimeout(() => {
        var event = new Event('change');
        d4.dispatchEvent(event);

    }, 1000)
}




    var d5 = document.getElementById('costn5')
    if(d5){
    d5.addEventListener("click", function() {
    d5.addEventListener('change', function(evt) {
        console.log("listned");
        var selectedValue = costn5.value;
        
        var e = document.getElementById('costc5')
        
        c = selectedValue
        readTextFile(url, function(text) {
            
            var data = JSON.parse(text);
            e.value = data[c][1]
        });
    });
}, false);
    setTimeout(() => {
        var event = new Event('change');
        d5.dispatchEvent(event);

    }, 1000)
}


    var d6 = document.getElementById('costn6')
    if(d6){
    d6.addEventListener("click", function() {
    d6.addEventListener('change', function(evt) {
        console.log("listned");
        var selectedValue = costn6.value;
        
        var e = document.getElementById('costc6')
        
        c = selectedValue
        readTextFile(url, function(text) {
            
            var data = JSON.parse(text);
            e.value = data[c][1]
        });
    });
}, false);
    setTimeout(() => {
        var event = new Event('change');
        d6.dispatchEvent(event);

    }, 1000)
}

    
    var d7 = document.getElementById('costn7')
    if(d7){
    d7.addEventListener("click", function() {
    d7.addEventListener('change', function(evt) {
        console.log("listned");
        var selectedValue = costn7.value;
        
        var e = document.getElementById('costc7')
        
        c = selectedValue
        readTextFile(url, function(text) {
            
            var data = JSON.parse(text);
            e.value = data[c][1]
        });
    });
}, false);
    setTimeout(() => {
        var event = new Event('change');
        d7.dispatchEvent(event);

    }, 1000)
}



    var d8 = document.getElementById('costn8')
    if(d8){
    d8.addEventListener("click", function() {
    d8.addEventListener('change', function(evt) {
        console.log("listned");
        var selectedValue = costn8.value;
        
        var e = document.getElementById('costc8')
        
        c = selectedValue
        readTextFile(url, function(text) {
            
            var data = JSON.parse(text);
            e.value = data[c][1]
        });
    });
}, false);
    setTimeout(() => {
        var event = new Event('change');
        d8.dispatchEvent(event);

    }, 1000)

}


    var d9 = document.getElementById('costn9')
    if(d9){
    d9.addEventListener("click", function() {
    d9.addEventListener('change', function(evt) {
        console.log("listned");
        var selectedValue = costn9.value;
        
        var e = document.getElementById('costc9')
        
        c = selectedValue
        readTextFile(url, function(text) {
            
            var data = JSON.parse(text);
            e.value = data[c][1]
        });
    });
}, false);
    setTimeout(() => {
        var event = new Event('change');
        d9.dispatchEvent(event);

    }, 1000)}


    var d10 = document.getElementById('costn10')
    if(d10){
    d10.addEventListener("click", function() {
    d10.addEventListener('change', function(evt) {
        console.log("listned");
        var selectedValue = costn10.value;
        
        var e = document.getElementById('costc10')
        
        c = selectedValue
        readTextFile(url, function(text) {
            
            var data = JSON.parse(text);
            e.value = data[c][1]
        });
    });
}, false);
    setTimeout(() => {
        var event = new Event('change');
        d10.dispatchEvent(event);

    }, 1000)}

    var d11 = document.getElementById('costn11')
    if(d11){
    d11.addEventListener("click", function() {
    d11.addEventListener('change', function(evt) {
        console.log("listned");
        var selectedValue = costn11.value;
        
        var e = document.getElementById('costc11')
        
        c = selectedValue
        readTextFile(url, function(text) {
            
            var data = JSON.parse(text);
            e.value = data[c][1]
        });
    });
}, false);
    setTimeout(() => {
        var event = new Event('change');
        d11.dispatchEvent(event);

    }, 1000)}

    var d12 = document.getElementById('costn12')
    if(d12){
    d12.addEventListener("click", function() {
    d12.addEventListener('change', function(evt) {
        console.log("listned");
        var selectedValue = costn12.value;
        
        var e = document.getElementById('costc12')
        
        c = selectedValue
        readTextFile(url, function(text) {
            
            var data = JSON.parse(text);
            e.value = data[c][1]
        });
    });
}, false);
    setTimeout(() => {
        var event = new Event('change');
        d12.dispatchEvent(event);

    }, 1000)
}

    var d13 = document.getElementById('costn13')
    if(d13){
    d13.addEventListener("click", function() {
    d13.addEventListener('change', function(evt) {
        console.log("listned");
        var selectedValue = costn13.value;
        
        var e = document.getElementById('costc13')
        
        c = selectedValue
        readTextFile(url, function(text) {
            
            var data = JSON.parse(text);
            e.value = data[c][1]
        });
    });
}, false);
    setTimeout(() => {
        var event = new Event('change');
        d13.dispatchEvent(event);

    }, 1000)
}



    


    var btn = document.getElementById('add-cost')
    btn.addEventListener("click", function() {
        var obj = document.getElementById(m)
        obj.style.display = 'flex';
        obj.setAttribute('class','form-group row')
        m++;
    }, false);


    