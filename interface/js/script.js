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
    fetch('http://localhost:8080/init').then(function(response) {
      return response.text();
    }).then(function(data) {
        console.log(data);
        const image = new Image();
        if (data == "1") {
            image.src = 'template_field.png';
        }
        else if (data == "0") {
            document.getElementById('message').classList.remove('hidden');
            image.src = 'cam.png';
        }
        image.onload = function(){
            const context = canvas.getContext('2d');
            context.imageSmoothingEnabled = false;
            context.drawImage(image, 0, 0);
        }
    }).catch(function(error) {
      console.log(error)
    });
}

function run() {
    hide(document.getElementById('done-button'));
    const canvas = document.getElementById('canvas');
    fetch('http://localhost:8080/run').then(function(response) {
      return response.text();
    }).then(function(data) {
        console.log(data);

        const context = canvas.getContext('2d');
        context.clearRect(0, 0, canvas.width, canvas.height);
        const image = new Image();
        if (data == "1") {
            image.src = 'cam.png';
        }
        image.onload = function(){
            context.imageSmoothingEnabled = false;
            context.drawImage(image, 0, 0);
        }
    }).catch(function(error) {
      console.log(error)
    });
}

function hide(element) {
    element.parentNode.removeChild(element);
}
