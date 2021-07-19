function resizeImage(imageData, maxWidth, maxHeight, callback) {
  const img = new Image();
  img.onload = () => {
    const zoomRate = Math.max(
      (1.0 * img.width) / maxWidth,
      (1.0 * img.height) / maxHeight
    );
    const newWidth =
      zoomRate > 1 ? Math.floor(img.width / zoomRate) : img.width;
    const newHeight =
      zoomRate > 1 ? Math.floor(img.height / zoomRate) : img.height;
    mainCanvas = document.createElement("canvas");
    mainCanvas.width = newWidth;
    mainCanvas.height = newHeight;
    const ctx = mainCanvas.getContext("2d");
    ctx.drawImage(img, 0, 0, newWidth, newHeight);
    var newImageData = mainCanvas.toDataURL("image/jpeg");

    newImageData = ExifRestorer.restore(imageData, newImageData);
    callback(newImageData);
  };
  img.src = imageData;
}

var Utils = {
  isEmptyString(s) {
    return s === undefined || s === null || s.length === 0;
  },
  isValidString(s) {
    return !Utils.isEmptyString(s);
  },
  isValid(o) {
    return o !== undefined && o !== null;
  }
};
