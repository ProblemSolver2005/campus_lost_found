
// IMAGE PREVIEW

const imageInput = document.getElementById('imageInput');
const imagePreview = document.getElementById('imagePreview');

if (imageInput) {

    imageInput.addEventListener('change', function () {

        const file = this.files[0];

        if (file) {

            imagePreview.src = URL.createObjectURL(file);
            imagePreview.style.display = 'block';

        }

    });

}


// DELETE CONFIRMATION

const deleteForms = document.querySelectorAll('.delete-form');

deleteForms.forEach(function (form) {

    form.addEventListener('submit', function (event) {

        const confirmed = confirm(
            'Are you sure you want to delete this item?'
        );

        if (!confirmed) {
            event.preventDefault();
        }

    });

});
