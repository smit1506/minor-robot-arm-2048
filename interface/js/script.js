function calibrate(origin){
    console.log("click");
    hide(origin);
    document.getElementById('calibration-menu').classList.remove('hidden');
}
function finishCalibration() {
    document.getElementById('calibration-menu').classList.add('hidden');
    document.getElementById('start-button').classList.remove('hidden');
}
function activate(origin) {
    hide(origin);
    document.getElementById('canvas').classList.remove('hidden');
}

function hide(element) {
    element.parentNode.removeChild(element);
}
