// vars
let result = document.querySelector(".result"),
    img_result = document.querySelector(".img-result"),
    save = document.querySelector(".save"),
    cropped = document.querySelector(".cropped"),
    dwn = document.querySelector(".download"),
    upload = document.querySelector("#file-input"),
    cropper = "";

const cropBtnsContainer = document.querySelector(".crop-btns-container");


// handle clicking on a page
const pagesContainer = document.querySelector("#pages-container");
const pagesImgs = pagesContainer.querySelectorAll("button");

Array.from(pagesImgs).forEach((btn) => {
    btn.addEventListener('click', function(e) {
        let src = btn.querySelector("img").src;

        console.log(src)
        let img = document.createElement("img");
        img.id = "image";
        img.src = src;
        result.classList.remove('hidden');
        cropBtnsContainer.classList.remove('hidden');
        result.innerHTML = "";
        // append new image
        result.appendChild(img);
        // show save btn and options
        // init cropper
        cropper = new Cropper(img);
    })
});



// on change show
// save on click
save.addEventListener("click", (e) => {
    e.preventDefault();
    // get result to data uri
    let imgSrc = cropper
        .getCroppedCanvas({
            width: 300, // input value
        })
        .toDataURL();
    // remove hide class of img
    // cropped.classList.remove("hide");
    // img_result.classList.remove("hide");
    // show image cropped

    cropped.src = imgSrc;
    dwn.classList.remove("hide");
    dwn.download = "imagename.png";
    dwn.setAttribute("href", imgSrc);



    cropBtnsContainer.classList.add('hidden');
    result.classList.add('hidden');
});