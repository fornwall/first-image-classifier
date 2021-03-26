// https://www.smashingmagazine.com/2018/01/drag-drop-file-uploader-vanilla-js/
let dropArea = document.documentElement;
let form = document.querySelector('form');

['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
  dropArea.addEventListener(eventName, (e) => {
    e.preventDefault()
    e.stopPropagation()

    const method = ['dragenter', 'dragover'].includes(eventName) ? 'add' : 'remove';
    form.classList[method]('highlight');

    if (eventName == 'drop') {
      const files = e.dataTransfer.files;
      handleFiles(files);
    }
  }, false);
});

function handleFiles(files) {
  previewFile(files[0]);
  uploadFile(files[0]);
}

document.querySelector('#file').addEventListener('change', (e) => {
  handleFiles(e.target.files);
});

function uploadFile(file) {
  const output = document.querySelector('#output');
  output.innerHTML = '<p>Awaiting classification...</p>';

  let url = '';
  let formData = new FormData();
  formData.append('file', file)
  fetch(url, { method: 'POST', body: formData })
    .then((response) => response.json())
    .then((data) => {
      const smiling = data['smiling'];
      const certainty = data['certainty'];

      output.innerHTML = '';
      const outputText = document.createElement('h2');
      outputText.textContent = 'Smiling: ' + (smiling ? 'YES' : 'NO') + ' (' + certainty.toFixed(3) + ' certain)';
      output.appendChild(outputText);
    });
}


function previewFile(file) {
  const gallery = document.getElementById('gallery');
  gallery.innerHTML = '';
  const reader = new FileReader()
  reader.readAsDataURL(file)
  reader.onloadend = () => {
    let img = document.createElement('img');
    img.src = reader.result;
    gallery.appendChild(img);
  };
}
