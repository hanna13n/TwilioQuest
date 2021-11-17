let status = process.argv[2];
status = Number(status);
let dryness = process.argv[3];
dryness = Number(dryness);

if (status === 0 && dryness > 10) {
    console.log("WATER");
}