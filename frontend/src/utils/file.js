import { Buffer } from "buffer";


export function displayImage(hexString) {
    const base64Image = Buffer.from(hexString, 'hex').toString('base64');
    const formatedImage = 'data:image/png;base64,' + base64Image;

    return formatedImage;
}

export function downloadImage(byteArray, fileName) {
    var blob = new Blob([byteArray], {type: "image/png"});
    var link = document.createElement('a');
    link.href = window.URL.createObjectURL(blob);
    link.download = fileName;
    link.click();
}

export function fileToHex(file) {
    return new Promise((resolve, reject) => {
        const reader = new FileReader();
        reader.onload = (event) => {
            const arrayBuffer = reader.result;
            const byteArray = new Uint8Array(arrayBuffer);
            const hexArray = Array.from(byteArray, byte => byte.toString(16).padStart(2, '0'));
            const hexString = hexArray.join('');
            resolve(hexString);
        };
        reader.onerror = (error) => reject(error);
        reader.readAsArrayBuffer(file);
    });
}

export function hexToBytes(hexString) {
    var bytes = [];
    for (var i = 0; i < hexString.length; i += 2) {
        bytes.push(parseInt(hexString.substr(i, 2), 16));
    }
    return new Uint8Array(bytes);
}