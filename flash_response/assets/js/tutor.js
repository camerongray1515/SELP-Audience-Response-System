$(document).ready(function() {
    // Submit the course selection form when the course in the drop down is changed
    $('#course-selection').change(function() {
        $('#course-selection-form').trigger('submit');
    });

    // Do not submit form if the item selected is not a course (i.e. the "Select a Course" option)
    $('#course-selection-form').submit(function() {
        if (isNaN(parseInt($('#course-selection').val()))) {
            return false;
        }
    });


    // Add a question option to the table
    $('#add-question-option').click(function() {
        html = $('#option-row-template').html();

        // Append row before the second last row
        $('#option-table tr:last').before(html);

        return false; // Block default form sumbit
    });
    
    $(document).on('click', '.remove-option', function() {
        $(this).closest('tr').remove();
        return false;
    });
});
