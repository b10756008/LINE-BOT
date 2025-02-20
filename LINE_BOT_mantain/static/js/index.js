$(".page_btn").click(function(){
    const page = $(this).data("page");
    window.location.href = `/${page}`;
})

$("#uploadForm").submit(function (event) {
    let path_name = location.pathname.substring(1);
    console.log(path_name)
    event.preventDefault();  // 防止表單提交後跳轉

    let formData = new FormData();
    let fileInput = $("#excelFile")[0].files[0];
    console.log(fileInput)
    if (!fileInput) {
        Swal.fire("錯誤", "請選擇一個檔案", "error");
        return;
    }
    else if(fileInput.name !== path_name+".xlsx"){
        Swal.fire({
            title: "檔案名稱錯誤",
            text: `檔案名稱須為 ${path_name}`,
            icon: "error",
            showCancelButton: true
        })
    }
    else{
        formData.append("file", fileInput);

    $.ajax({
        url: "/upload",
        type: "POST",
        data: formData,
        processData: false,
        contentType: false,
        success: function (response) {
            Swal.fire({
                title: "轉換成功！",
                text: "已轉換成JSON檔案",
                icon: "success",
                showCancelButton: true
            })
        },
        error: function () {
            Swal.fire({
                title: "檔案上傳失敗",
                text: "請確認檔案名稱及內容",
                icon: "error",
                showCancelButton: true
            })
        }
    });
    }
});