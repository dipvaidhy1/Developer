$(document).ready(function() {

    $("#btnsave").click(function () {
        let output = "";
        let sid = $("#stuid").val();
        let nm = $("#nameid").val();
        let em = $("#emailid").val();
        let pw = $("#passwordid").val();
        let csrf = $("input[name=csrfmiddlewaretoken]").val();

        if(nm == "") {
            $("#msg").text("Please enter your name");
            $("#msg").show();
        } else if(em == "") {
            $("#msg").text("Please enter your email");
            $("#msg").show();
        } else if(pw == "") {
            $("#msg").text("Please enter your password");
            $("#msg").show();
        } else {
            let mydata = {stuid: sid, name: nm, email: em, password: pw, csrfmiddlewaretoken: csrf};
            sendDataToServer(mydata);
        }
    });

    $("tbody").on("click", ".btn-del", function () {
        let id = $(this).attr("data-sid");
        let csrf = $("input[name=csrfmiddlewaretoken]").val();
        let mydata = {sid: id, csrfmiddlewaretoken: csrf};
        sendDeleteRequest(mydata, this);
    });

    $("tbody").on("click", ".btn-edit", function () {
        let id = $(this).attr("data-sid");
        let csrf = $("input[name=csrfmiddlewaretoken]").val();
        let mydata = {sid: id, csrfmiddlewaretoken: csrf};
        sendEditRequest(mydata);
    });

    // function sendDataToServer(mydata) {
    //     $.ajax({
    //         url: ("/save/"),
    //         method: "POST",
    //         data: mydata,
    //         success: function(data) {
    //             handleSaveResponse(data);
    //         }
    //     });
    // }

    // function sendDeleteRequest(mydata, element) {
    //     $.ajax({
    //         url: ("/delete/"),
    //         method: "POST",
    //         data: mydata,
    //         success: function(data) {
    //             handleDeleteResponse(data, element);
    //         }
    //     });
    // }

    // function sendEditRequest(mydata) {
    //     $.ajax({
    //         url: ("/edit/"),
    //         method: "POST",
    //         data: mydata,
    //         success: function(data) {
    //             handleEditResponse(data);
    //         }
    //     });
    
    // }

    // function sendRequest(endpoint, method, data, successCallback, element = null) {
    //     $.ajax({
    //         url: endpoint,
    //         method: method,
    //         data: data,
    //         success: function(responseData) {
    //             if (element !== null) {
    //                 successCallback(responseData, element);
    //             } else {
    //                 successCallback(responseData);
    //             }
    //         }
    //     });
    // }
    
    // function sendDataToServer(data) {
    //     sendRequest("save", "POST", data, handleSaveResponse);
    // }
    
    // function sendDeleteRequest(data, element) {
    //     sendRequest("delete", "POST", data, handleDeleteResponse, element);
    // }
    
    // function sendEditRequest(data) {
    //     sendRequest("edit", "POST", data, handleEditResponse);
    // }
    
    function handleSaveResponse(data) {
        let output = "";
        let msg = $("#msg");

        if(data.status == "Save") {
            msg.text("Form Submitted successfully!!");
            msg.show();

            data.student_data.forEach(function (item) {
                output += "<tr><td>" + item.id + "</td><td>" + item.name +
                    "</td><td>" + item.email + "</td><td>" + item.password +
                    "</td><td> <input type='button' class='btn btn-success btn-sm btn-edit' value='Edit' data-sid='" + item.id + "' />" +
                    "<input type='button' class='btn btn-danger btn-sm btn-del' value='Delete' data-sid='" + item.id + "' />" +
                    "</td></tr>";
            });

            $("#tbody").html(output);
            $("#stuid").val("");
            $("form")[0].reset();
        }

        if(data.status == 0){
            msg.text("Unable to save data");
            msg.show();

            $("#stuid").val("");
            $("form")[0].reset();
        }
    }

    function handleDeleteResponse(data, element) {
        let msg = $("#msg");

        if(data.status == 1) {
            msg.text("Data Deleted Successfully");
            msg.show();
            
            $(element).closest("tr").fadeOut();
        }
        
        if(data.status == 0) {
            msg.text("Unable to Delete Data");
            msg.show();
        }
    }

    function handleEditResponse(data) {
        $("#stuid").val(data.id);
        $("#nameid").val(data.name);
        $("#emailid").val(data.email);
        $("#passwordid").val(data.password);
    }
});
