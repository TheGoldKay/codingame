/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

const LON = rad(parseFloat(readline().replace(',', '.')));
const LAT = rad(parseFloat(readline().replace(',', '.')));
const N = parseInt(readline());
let df = [];
for (let i = 0; i < N; i++) {
    const DEFIB = readline();
    let d = DEFIB.split(';');
    df.push({
        name: d[1],
        lon: rad(parseFloat(d[4].replace(',', '.'))),
        lat: rad(parseFloat(d[5].replace(',', '.'))),
    })
}

function rad(deg){
   return deg * (Math.PI / 180);
}

function distance(lon1, lon2, lat1, lat2){
    let x = Math.abs(lon1 - lon2) * Math.cos((lat1 + lat2) / 2);
    let y = Math.abs(lat1 - lat2);
    return Math.sqrt(x**2 + y**2) * 6371 * 1000;
}

function closest(df){
    let close = {name: "", dist: Infinity};
    for(let d of df){
        let dist = distance(LON, d.lon, LAT, d.lat);
        if(dist < close.dist){
            close.name = d.name;
            close.dist = dist;
        }
    }
    return close.name;
}

console.log(closest(df));
