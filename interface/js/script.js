function activate(origin) {
    const parent = origin.parentNode;
    parent.removeChild(origin);
    document.getElementById('canvas').classList.remove('hidden');
}
