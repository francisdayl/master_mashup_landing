

// static/js/script.js

document.addEventListener('DOMContentLoaded', function() {
    const generateMashButton = document.getElementById('generate-mashup');
    const audioGenerated = document.getElementById('generated-mashup')
    generateMashButton.addEventListener('click', function() {
        if(audioGenerated.classList.contains('hidden')){
            audioGenerated.classList.toggle('hidden')

        }
    });
});


