function updateYachts(yachts) {
    $.each($(".dynamic-runs .field-yacht select"), function(index, select) {
        $(select).children("option:gt(0)").remove();
        $.each(yachts, function(index, option) {
            $(select).append($("<option></option>").attr("value", option[0]).text(option[1]));
        });
    });
}

function getYachts(event_id) {
    $.ajax({
        url: '/ajax/yachts/',
        data: {event_id: event_id},
        success: function(response) {
            updateYachts(response.yachts);
        },
        error: function(response) {
            console.error('Failed to fetch yachts for event:', response);
        }
    })
}

window.onload = function() {
    $("#id_event").change(function(event) {
        getYachts($(event.target).val());
    });
    $(".add-row a").click(function(event) {
        getYachts($("#id_event").val());
    })
}

