
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

    let url = '/static/assets/js/data.json'
    let gradeurl = '/static/assets/js/data_grade.json'
    let yardurl = '/static/assets/js/yard.json'
    let metalurl = '/static/assets/js/data_metal.json'
    let costurl = '/static/assets/js/data_cost.json'
    var room = 1;
    cmetal = 1;
    m = 101;




    function call(element, values){
        readTextFile(metalurl, function(text) {
            var data = JSON.parse(text);
            var options = ''
            var c = values
            if(values=="SELECT"){
                values = 0
            }
            if(values!=0){
                for (let i = 0; i < data.length; i++) {
                    var value = data[i][0]
                    options += `<option value=${value}>` + data[i][1] + "</option>";
                }
                document.getElementById(element).innerHTML = options;
                document.getElementById(element).value =values;
            }else{
                options += "<option>SELECT</option>";
                for (let i = 0; i < data.length; i++) {
                    var value = data[i][0]
                    if(value==values){
                        
                    }else{
                        options += `<option value=${value}>` + data[i][1] + "</option>";
                    }
                    document.getElementById(element).innerHTML = options;
                }
            }
        })
    }    
        array = ['c',1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        htmx.onLoad(function(content){
        var supplier = document.getElementById('id_supplier')
        if(supplier){
            
                var supplier = document.getElementById('id_supplier')
                // console.log(document.getElementById("id_yard").value);
                if(document.getElementById("id_yard").value!=""){

                }else{
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
                                    // console.log(`<option value=${value}>`);
                                }
                                document.getElementById("id_yard").innerHTML = options;
                            }
                        })
                    });

                }
                
                // }, false)
                setTimeout(() => {
                var event = new Event('change');
                supplier.dispatchEvent(event);
    
                }, 1000)
        
        }


        var gr = document.getElementById('id_grade')
        if(gr){
            console.log(gr.value);
            if(gr.value!=""){
                // gr.addEventListener("click", function() {
                //     gr.addEventListener('change', function(evt) {
                        // 
                        console.log(gr.value);
                        var selectedValue = gr.value;
                        // console.log(selectedValue);
                        c = selectedValue
                        var i= 0
                        
                        var cdata,mdata;
        
                        readTextFile(costurl, function(text) {
                            var data = JSON.parse(text);
                            // console.log(data);
                            cdata = data;
                        })
                        readTextFile(metalurl, function(text) {
                            var data = JSON.parse(text);
                            // console.log(data);
                            mdata = data;
                        })
        
        
        
                        readTextFile(gradeurl, function(text) {
                            var data = JSON.parse(text);
                            // var cdata = JSON.parse(costurl);
                            // console.log(cdata);
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
                                            // console.log(field[i]);
                                            var ele = document.getElementById('c' + idf)
                                            // console.log('c' + idf);
                                            // var def = 'costc'+idf
                                            ele.removeAttribute('hidden')
                                        }else{
                                            name.style.display = 'inline-block'
                                        }
                                        // console.log();
                                        if(i.startsWith('costn')){
                                            var m = 0
                                            var cost_value = field[i]
                                            // console.log(cost_value);
                                            while(cost_value!=cdata[m][0]){
                                                m++;
                                            }
                                            name.innerHTML = cdata[m][1]
                                            // console.log(cdata[0].fields);
                                        }else if(i.startsWith('metaln')){
                                            var m = 0
                                            var metal_value = field[i]
                                            // console.log(metal_value);
                                            while(metal_value!=mdata[m][0]){
                                                m++;
                                            }
                                            name.innerHTML = mdata[m][1]
                                        }else{
                                            name.innerHTML =  field[i]
                                        }
        
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
                    
            

            }else{
                gr.addEventListener("click", function() {
                    gr.addEventListener('change', function(evt) {
                        // 
                        var selectedValue = gr.value;
                        // console.log(selectedValue);
                        c = selectedValue
                        var i= 0
                        
                        var cdata,mdata;
        
                        readTextFile(costurl, function(text) {
                            var data = JSON.parse(text);
                            // console.log(data);
                            cdata = data;
                        })
                        readTextFile(metalurl, function(text) {
                            var data = JSON.parse(text);
                            // console.log(data);
                            mdata = data;
                        })
        
        
        
                        readTextFile(gradeurl, function(text) {
                            var data = JSON.parse(text);
                            // var cdata = JSON.parse(costurl);
                            // console.log(cdata);
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
                                            // console.log(field[i]);
                                            var ele = document.getElementById('c' + idf)
                                            // console.log('c' + idf);
                                            // var def = 'costc'+idf
                                            ele.removeAttribute('hidden')
                                        }else{
                                            name.style.display = 'inline-block'
                                        }
                                        // console.log();
                                        if(i.startsWith('costn')){
                                            var m = 0
                                            var cost_value = field[i]
                                            // console.log(cost_value);
                                            while(cost_value!=cdata[m][0]){
                                                m++;
                                            }
                                            name.innerHTML = cdata[m][1]
                                            // console.log(cdata[0].fields);
                                        }else if(i.startsWith('metaln')){
                                            var m = 0
                                            var metal_value = field[i]
                                            // console.log(metal_value);
                                            while(metal_value!=mdata[m][0]){
                                                m++;
                                            }
                                            name.innerHTML = mdata[m][1]
                                        }else{
                                            name.innerHTML =  field[i]
                                        }
        
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
            }

        
    setTimeout(() => {
        var event = new Event('change');
        gr.dispatchEvent(event);

    }, 1000)
    }
})

    
    // var gr = document.getElementById('id_grade')
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
        let windowurl = window.location.href

            if(windowurl.includes('update')){
                var ele = document.getElementById('metaln')
                readTextFile(gradeurl, function(text) {
                    var c = windowurl.charAt(windowurl.length-2)
                    var data = JSON.parse(text);
                    var a=0
                    while(c!=data[a].pk){
                        a++;
                    }

                    var field = data[a].fields

                    var element = "metaln"; call(element,field.metaln)
                    var element = "metalnn"; call(element,field.metalnn)
                    var metal_data = {
                        'metaln1': field.metaln1
                    }
                    for(const i in field){
                        if(i.startsWith('metaln')){
                            metal_data[i] = field[i]
                        }
                    }
                    for (let i = 1; i < 21; i++) {
                        var element = ("metaln" +""+ i)
                        var a = document.getElementById(element);
                        call(element,metal_data[element])            
                    }

                })
                
            }else{
                var element = document.getElementById('metaln'); call('metaln',0)
                element = document.getElementById('metalnn'); call('metalnn',0)

                for (let i = 1; i < 21; i++) {
                    var ele = ("metaln" + "" + i)
                    element = document.getElementById(ele)
                    call(ele,0)
                    
                }

            }

    }



    var d = document.getElementById('costn')
    if(d){
        let windowurl = window.location.href

        function callc(element, values){
            readTextFile(costurl, function(text) {
                var data = JSON.parse(text);
                var options = ''
                var c = values
                if(values=="SELECT"){
                    values = 0
                }
                // console.log(values);
                if(values!=0){
                    for (let i = 0; i < data.length; i++) {
                        var value = data[i][0]
                        options += `<option value=${value}>` + data[i][1] + "</option>";
                    }
                    document.getElementById(element).innerHTML = options;
                    document.getElementById(element).value = values;
                }else{
                    options += "<option>SELECT</option>";
                    for (let i = 0; i < data.length; i++) {
                        var value = data[i][0]
                        if(value==values){
                            
                        }else{
                            options += `<option value=${value}>` + data[i][1] + "</option>";
                        }
                        document.getElementById(element).innerHTML = options;
                        
                    }
                }
            })

                
        }
        if(windowurl.includes('update')){
            // var ele = document.getElementById('metaln')
            readTextFile(gradeurl, function(text) {
                var c = windowurl.charAt(windowurl.length-2)
                var data = JSON.parse(text);
                var a=0
                while(c!=data[a].pk){
                    a++;
                }

                var field = data[a].fields

                var element = "costn"; callc(element,field.costn)
                var element = "costnn"; callc(element,field.costnn)
                var cost_data = {
                    'costn1': field.costn1
                }
                for(const i in field){
                    if(i.startsWith('costn')){
                        cost_data[i] = field[i]
                    }
                }
                // console.log(cost_data['costn']);
                for (let i = 1; i < 21; i++) {
                    var element = ("costn" +""+ i)
                    var a = document.getElementById(element);
                    // console.log(cost_data[element]+ " " + element);
                    callc(element,cost_data[element])            
                }

            })
            
        }else{
            var element = document.getElementById('costn'); callc('costn',0)
            element = document.getElementById('costnn'); callc('costnn',0)

            for (let i = 1; i < 21; i++) {
                var ele = ("costn" + "" + i)
                element = document.getElementById(ele)
                callc(ele,0)
                
            }

        }
        // var element = "costn"; callc(element)
        // element = "costnn"; callc(element)

        // for (let i = 1; i < 21; i++) {
        //     if(i==20){
        //         // console.log(a);
        //     }
        //     var element = ("costn" +""+ i)
        //     var a = document.getElementById(element);
        //     callc(element)

            
        // }



    d.addEventListener("click", function() {

        d.addEventListener('change', function(evt) {
            // 
            var selectedValue = costn.value;
            var e = document.getElementById('costc') 

            c = selectedValue
            if(c=='SELECT'){
                e.value=0
            }else{
                readTextFile(costurl, function(text) {
                    
                    var data = JSON.parse(text);
                    // console.log(data);
                    for (let i = 0; i < data.length; i++) {
                        
                        if(data[i][0]==c){
                            c = data[i][2]
                            // 
                        }   
                    }
                    e.value = c
                    if(e.value==null){
                        e.value = 0
                    }
                    // console.log("jns")
                    // e.value = data[c][1]
                });
            }
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

        var selectedValue = costnn.value;
        
        var e = document.getElementById('costcn')
        e.value = 0
        // console.log(e.value);
        
        c = selectedValue
        if(c=='SELECT'){
            e.value=0
        }else{
            // console.log(e.value);
            readTextFile(costurl, function(text) {
                
                var data = JSON.parse(text);
                // console.log(data);
                for (let i = 0; i < data.length; i++) {
                    
                    if(data[i][0]==c){
                        c = data[i][2]
                        // 
                    }   
                }
                e.value = c
                // console.log("jns")
                // e.value = data[c][1]
            });
        }
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
        
        var selectedValue = costn1.value;
        
        var e = document.getElementById('costc1')
        
        c = selectedValue
        readTextFile(costurl, function(text) {
            
            var data = JSON.parse(text);
            for (let i = 0; i < data.length; i++) {
                    
                if(data[i][0]==c){
                    c = data[i][2]
                    // 
                }   
            }
            e.value = c
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
        
        var selectedValue = costn2.value;
        
        var e = document.getElementById('costc2')
        
        c = selectedValue
        readTextFile(costurl, function(text) {
            
            var data = JSON.parse(text);
            for (let i = 0; i < data.length; i++) {
                    
                if(data[i][0]==c){
                    c = data[i][2]
                    
                }   
            }
            e.value = c
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
        
        var selectedValue = costn3.value;
        
        var e = document.getElementById('costc3')
        
        c = selectedValue
        readTextFile(costurl, function(text) {
            
            var data = JSON.parse(text);
            for (let i = 0; i < data.length; i++) {
                    
                if(data[i][0]==c){
                    c = data[i][2]
                    
                }   
            }
            e.value = c
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
        
        var selectedValue = costn4.value;
        
        var e = document.getElementById('costc4')
        
        c = selectedValue
        readTextFile(costurl, function(text) {
            
            var data = JSON.parse(text);
            for (let i = 0; i < data.length; i++) {
                    
                if(data[i][0]==c){
                    c = data[i][2]
                    
                }   
            }
            e.value = c
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
        
        var selectedValue = costn5.value;
        
        var e = document.getElementById('costc5')
        
        c = selectedValue
        readTextFile(costurl, function(text) {
            
            var data = JSON.parse(text);
            for (let i = 0; i < data.length; i++) {
                    
                if(data[i][0]==c){
                    c = data[i][2]
                    
                }   
            }
            e.value = c
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
        
        var selectedValue = costn6.value;
        
        var e = document.getElementById('costc6')
        
        c = selectedValue
        readTextFile(costurl, function(text) {
            
            var data = JSON.parse(text);
            for (let i = 0; i < data.length; i++) {
                    
                if(data[i][0]==c){
                    c = data[i][2]
                    
                }   
            }
            e.value = c
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
        
        var selectedValue = costn7.value;
        
        var e = document.getElementById('costc7')
        
        c = selectedValue
        readTextFile(costurl, function(text) {
            
            var data = JSON.parse(text);
            for (let i = 0; i < data.length; i++) {
                    
                if(data[i][0]==c){
                    c = data[i][2]
                    
                }   
            }
            e.value = c
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
        
        var selectedValue = costn8.value;
        
        var e = document.getElementById('costc8')
        
        c = selectedValue
        readTextFile(costurl, function(text) {
            
            var data = JSON.parse(text);
            for (let i = 0; i < data.length; i++) {
                    
                if(data[i][0]==c){
                    c = data[i][2]
                    
                }   
            }
            e.value = c
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
        
        var selectedValue = costn9.value;
        
        var e = document.getElementById('costc9')
        
        c = selectedValue
        readTextFile(costurl, function(text) {
            
            var data = JSON.parse(text);
            for (let i = 0; i < data.length; i++) {
                    
                if(data[i][0]==c){
                    c = data[i][2]
                    
                }   
            }
            e.value = c
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
        
        var selectedValue = costn10.value;
        
        var e = document.getElementById('costc10')
        
        c = selectedValue
        readTextFile(costurl, function(text) {
            
            var data = JSON.parse(text);
            for (let i = 0; i < data.length; i++) {
                    
                if(data[i][0]==c){
                    c = data[i][2]
                    
                }   
            }
            e.value = c
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
        
        var selectedValue = costn11.value;
        
        var e = document.getElementById('costc11')
        
        c = selectedValue
        readTextFile(costurl, function(text) {
            
            var data = JSON.parse(text);
            for (let i = 0; i < data.length; i++) {
                    
                if(data[i][0]==c){
                    c = data[i][2]
                    
                }   
            }
            e.value = c
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
        
        var selectedValue = costn12.value;
        
        var e = document.getElementById('costc12')
        
        c = selectedValue
        readTextFile(costurl, function(text) {
            
            var data = JSON.parse(text);
            for (let i = 0; i < data.length; i++) {
                    
                if(data[i][0]==c){
                    c = data[i][2]
                    
                }   
            }
            e.value = c
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
        
        var selectedValue = costn13.value;
        
        var e = document.getElementById('costc13')
        
        c = selectedValue
        readTextFile(costurl, function(text) {
            
            var data = JSON.parse(text);
            for (let i = 0; i < data.length; i++) {
                    
                if(data[i][0]==c){
                    c = data[i][2]
                    
                }   
            }
            e.value = c
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


    