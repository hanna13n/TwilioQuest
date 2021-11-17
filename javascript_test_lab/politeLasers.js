function getLaserSetting(request) {
    if (request === "please")
        return "OFF";
    else
        return "ON";
}