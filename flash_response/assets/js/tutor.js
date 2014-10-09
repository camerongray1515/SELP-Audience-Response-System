// Submit the course selection form when the course in the drop down is changed
$(document).ready(function() {
    $('#course-selection').change(function() {
        $('#course-selection-form').trigger('submit');
    });

    // Do not submit form if the item selected is not a course (i.e. the "Select a Course" option)
    $('#course-selection-form').submit(function() {
        if (isNaN(parseInt($('#course-selection').val()))) {
            return false;
        }
    });
});