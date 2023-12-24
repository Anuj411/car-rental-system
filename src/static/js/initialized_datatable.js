
function initialize_datatable(){
    var table = $(`#${table_id}`).DataTable({
        scrollX: false,
        processing: true,
        serverSide: true,
        ajax: {
            url: url,
            type: 'get',
        },
        columns: columns,
    });
    return table;
}