function calibrate(origin){
    hide(origin);
    document.getElementById('calibration-menu').classList.remove('hidden');
}
function finishCalibration() {
    document.getElementById('calibration-menu').classList.add('hidden');
    document.getElementById('start-button').classList.remove('hidden');
}
function activate(origin) {
    hide(document.getElementById('init'));
    const canvas = document.getElementById('canvas');
    canvas.classList.remove('hidden');
    fetch('http://localhost:8080/run').then(function(response) {
      return response.text();
    }).then(function(data) {
        if (data == "1") {
            image = new Image();
            image.src = 'cam.png';
            image.onload = function(){
                context = canvas.getContext('2d');
                context.imageSmoothingEnabled = false;
                //context.drawImage(image, 0, 0, 960, 540);
                context.drawImage(image, 0, 0);
            }
        }
    }).catch(function(error) {
      console.log(error)
    });
}

function hide(element) {
    element.parentNode.removeChild(element);
}
