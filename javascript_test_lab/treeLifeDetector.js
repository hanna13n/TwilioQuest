let status = process.argv[2];
status = Number(status);
if (status == 0) {
    console.log("alive");
}
else {
    console.log("other");
}