/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

 function binary(s){
    let b = "";
    for(let c of s){
        b += c.charCodeAt(0).toString(2).padStart(7, '0');
    }
    return b;
}

function unary(msg){
    let b = binary(msg);
    let u = "";
    let i = 0;
    //console.log(b);
    while(i < b.length){
        let series = "";
        if(b[i] === '1'){
            series += '0 ';
            while(b[i] === '1'){
                series += '0';
                i++;
            }
        }else{
            series += '00 ';
            while(b[i] === '0'){
                series += '0';
                i++;
            }
        }
        u += series + " ";
    }
    return u.trimEnd();
}


console.log(unary(msg));
