let drawRectangle = false;
const templateFieldOptions = {};

let stopped = false;

function calibrate(origin){
    remove(document.getElementById('firstButtons'));
    document.getElementById('calibration-menu').classList.remove('hidden');
}
function skipCalibration(origin) {
    remove(document.getElementById('firstButtons'));
    document.getElementById('start-button').classList.remove('hidden');
}
function setPosition(positionName){
    fetch('http://localhost:8080/calibrate', {
        method: 'POST',
        body: positionName
    }).then(function(response) {
        return response.text();
    }).then(function(data) {

        console.log(data);
        // temp
        if (data == "1") {
            console.log("Success!");
        }
        else {
            console.log("Position not set");
        }
    }).catch(function(error) {
        console.log(error)
    });
}

function moveToStart() {
    fetch('http://localhost:8080/move', {
        method: 'POST',
        body: 'start'
    }).then(function(response) {
      return response.text();
    }).then(function(data) {

        console.log(data);
        // temp
        if (data == "1") {
            console.log("Success!");
        }
        else {
            console.log("Didn't move");
        }
    }).catch(function(error) {
      console.log(error)
    });
}

function finishCalibration() {
    document.getElementById('calibration-menu').classList.add('hidden');
    document.getElementById('start-button').classList.remove('hidden');
}
function activate(origin) {
    remove(document.getElementById('init'));
    const canvas = document.getElementById('canvas');
    canvas.classList.remove('hidden');
    const message = document.getElementById('message');
    message.classList.remove('hidden');
    message.innerHTML="Fetching image...";
    fetch('http://localhost:8080/init').then(function(response) {
      return response.text();
    }).then(function(data) {
        console.log(data);
        const image = new Image();
        if (data == "1") {
            message.innerHTML="Continue if there is a black grid over the play area."
            document.getElementById('happy-button-group').classList.remove('hidden');
            document.getElementById('sad-button-group').classList.add('hidden');
            image.src = 'template_field.png';
        }
        else if (data == "0") {
            drawRectangle = true;
            message.innerHTML="Draw a rectangle over the 2048 field."
            message.classList.remove('hidden');
            document.getElementById('sad-button-group').classList.remove('hidden');
            document.getElementById('happy-button-group').classList.add('hidden');
            canvas.classList.add('drawable');
            const date = new Date()
            image.src = 'cam.png?temp=' + date.getTime();
        }
        image.onload = function(){
            const context = canvas.getContext('2d');
            context.imageSmoothingEnabled = false;
            context.drawImage(image, 0, 0);
            document.getElementById('fetch-image-button').classList.remove('hidden');
        }
    }).catch(function(error) {
        console.log(error)
    });
}

function fetchImage(){
    fetch('http://localhost:8080/image').then(function(response) {
        return response.text();
    }).then(function(data) {

        console.log(data);
        // temp
        if (data == "1") {

            const canvas = document.getElementById('canvas');
            const image = new Image();
            const date = new Date()
            image.src = 'cam.png?temp=' + date.getTime();
            image.onload = function(){
                const context = canvas.getContext('2d');
                context.clearRect(0, 0, canvas.width, canvas.height);
                context.imageSmoothingEnabled = false;
                context.drawImage(image, 0, 0);
            }
            console.log("Success!");
        }
        else {
            console.log("Reselect rectangle");
        }
    }).catch(function(error) {
        console.log(error)
    });
}

function redrawFieldTemplate() {
    document.getElementById('message').innerHTML="Draw a rectangle over the 2048 field."
    const canvas = document.getElementById('canvas');
    const image = new Image();
    drawRectangle = true;
    document.getElementById('message').classList.remove('hidden');
    document.getElementById('sad-button-group').classList.remove('hidden');
    document.getElementById('happy-button-group').classList.add('hidden');
    canvas.classList.add('drawable');
    const date = new Date()
    image.src = 'cam.png?temp=' + date.getTime();
    image.onload = function(){
        const context = canvas.getContext('2d');
        context.imageSmoothingEnabled = false;
        context.drawImage(image, 0, 0);
    }
}

function setFieldTemplate() {
    let fieldTemplate = document.getElementById('field-template');
    let rct = fieldTemplate.dataset.rct
    fetch('http://localhost:8080/field', {
        method: 'POST',
        body: rct
    }).then(function(response) {
      return response.text();
    }).then(function(data) {

        console.log(data);
        // temp
        if (data == "1") {
            console.log("Success!");
            remove(fieldTemplate);
            start();
        }
        else {
            console.log("Reselect rectangle");
        }



        // const context = canvas.getContext('2d');
        // context.clearRect(0, 0, canvas.width, canvas.height);
        // const image = new Image();
        // if (data == "1") {
        //     image.src = 'cam.png';
        // }
        // image.onload = function(){
        //     context.imageSmoothingEnabled = false;
        //     context.drawImage(image, 0, 0);
        // }
    }).catch(function(error) {
      console.log(error)
    });
}

function start() {
    stopped = false;
    document.getElementById("happy-button-group").classList.add('hidden');
    document.getElementById("sad-button-group").classList.add('hidden');
    document.getElementById("running-button-group").classList.remove('hidden');
    document.getElementById("fetch-image-button").classList.add('hidden');
    document.getElementById('message').innerHTML = "Doing first move!";

    const canvas = document.getElementById('canvas');
    const context = canvas.getContext('2d');
    context.clearRect(0, 0, canvas.width, canvas.height);
    run();
}

function run() {
    fetch('http://localhost:8080/run').then(function(response) {
      return response.json();
    }).then(function(data) {
        console.log(data);
        const image = new Image();
        const canvas = document.getElementById('canvas');
        const context = canvas.getContext('2d');

        const direction = parseInt(data[0]);

        let message = "Robot is moving ";
        const date = new Date()
        image.src = 'cam.png?temp=' + date.getTime();
        switch (direction) {
            case -2:
                message = "Please redraw the field template.";
                redrawFieldTemplate();
                break;
            case -1:
                message = "Finished!";
                break;
            case 0:
                message = message.concat("left");
                break;
            case 1:
                message = message.concat("up");
                break;
            case 2:
                message = message.concat("right");
                break;
            case 3:
                message = message.concat("down");
                break;
            default:
        }
        message = message.concat("!");
        document.getElementById('message').innerHTML = message;
        const fieldPlaceholder = document.getElementById('field-placeholder');
        console.log(fieldPlaceholder);
        fieldPlaceholder.innerHTML = data[1];
        fieldPlaceholder.classList.remove('hidden');
        image.onload = function(){
            context.imageSmoothingEnabled = false;
            context.drawImage(image, 0, 0);
            if (direction >= 0 && !stopped) {
                run();
            }
            else if (drawRectangle) {
                redrawFieldTemplate();
            }
        }
    }).catch(function(error) {
      console.log(error)
    });
}

function stop(){
    stopped = true;
    document.getElementById("running-button-group").classList.add('hidden');
}

function stopAndRedrawFieldTemplate(){
    stop();
    document.getElementById('message').innerHTML = "Stopping...";
    drawRectangle = true;
}

function remove(element) {
    element.parentNode.removeChild(element);
}
