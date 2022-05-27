const addProblemForm = $('#add-problem-form');
addProblemForm.submit(function (e) {
    console.log(addProblemForm.serialize())
    e.preventDefault();
    $.ajax({
        type: addProblemForm.attr('method'),
        url: addProblemForm.attr('action'),
        data: addProblemForm.serialize(),
        success: function (response) {
            $("#form-response").html('<strong><p class="text-info">' + response + '</p></strong>');
        },
        error: function () {
            $("#form-response").html('<strong><p class="text-danger">Error!</p></strong>');
        }
    });
    return false;
});