
if ('serviceWorker' in navigator) {
    console.log("Register service worker");
    res=navigator.serviceWorker.register('/static/js/serviceworker.js');
    console.log(res);
  }
  
//   document.querySelector('#show').addEventListener('click', () => {
//     const iconUrl = document.querySelector('select').selectedOptions[0].value;
//     let imgElement = document.createElement('img');
//     imgElement.src = iconUrl;
//     document.querySelector('#container').appendChild(imgElement);
//   });
