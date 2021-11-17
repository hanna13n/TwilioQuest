let s1 = process.argv[2];
let s2 = process.argv[3];
s1 = (String(s1)).toLowerCase();
s2 = (String(s2)).toLowerCase();
if (s1 < s2) {
    console.log(-1);
}
else if (s1 == s2) {
    console.log(0);
}
else {
    console.log(1);
}
