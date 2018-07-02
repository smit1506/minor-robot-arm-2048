function calibrate(origin){
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
    fetch('http://localhost:8080/run').then(function(response) {
      return response.text();
    }).then(function(data) {
      console.log(data);
    }).catch(function(error) {
      console.log(error)
    });
}

function hide(element) {
    element.parentNode.removeChild(element);
}
