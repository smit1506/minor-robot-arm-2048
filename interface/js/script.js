let drawRectangle = false;
const templateFieldOptions = {};

function calibrate(origin){
    remove(origin);
    document.getElementById('calibration-menu').classList.remove('hidden');
}
function finishCalibration() {
    document.getElementById('calibration-menu').classList.add('hidden');
    document.getElementById('start-button').classList.remove('hidden');
}
function activate(origin) {
    remove(document.getElementById('init'));
    const canvas = document.getElementById('canvas');
    canvas.classList.remove('hidden');
    fetch('http://localhost:8080/init').then(function(response) {
      return response.text();
    }).then(function(data) {
        console.log(data);
        const image = new Image();
        // if (data == "1") {

                // document.getElementById('happy-button-group').classList.remove('hidden');
                // document.getElementById('sad-button-group').classList.add('hidden');
        //     image.src = 'template_field.png';
        // }
        //else if (data == "0") {
            drawRectangle = true;
            document.getElementById('message').classList.remove('hidden');
            document.getElementById('sad-button-group').classList.remove('hidden');
            document.getElementById('happy-button-group').classList.add('hidden');
            canvas.classList.add('drawable');
            image.src = 'cam.png';
        //}
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
    document.getElementById('confirm-button').classList.add('hidden');
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

function remove(element) {
    element.parentNode.removeChild(element);
}
