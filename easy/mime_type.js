/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

const N = parseInt(readline()); // Number of elements which make up the association table.
const Q = parseInt(readline()); // Number Q of file names to be analyzed.
let mime = {};
for (let i = 0; i < N; i++) {
    var inputs = readline().split(' ');
    const EXT = inputs[0]; // file extension
    const MT = inputs[1]; // MIME type.
    mime[EXT.toLowerCase()] = MT;
}

let names = [];
for (let i = 0; i < Q; i++) {
    const FNAME = readline(); // One file name per line.
    names.push(FNAME);
}

function files(names){
   for(let name of names){
       let parts = name.split('.');
       let m = "UNKNOWN";
       if(parts.length > 1 ){
            m = mime[parts[parts.length - 1].toLowerCase()] ||"UNKNOWN";
       }
       console.log(m);
   }
}

files(names);