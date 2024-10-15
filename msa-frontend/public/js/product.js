// 상품등록 버튼 이벤트 처리
const regbtn = document.querySelector('#regbtn');
const productfrm = document.productfrm

regbtn.addEventListener('click', async ()=> {
    const formData = new FormData(productfrm);

    let jsondata = {};
    formData.forEach((val, key)=> {
        jsondata[key] = val;
    });
    console.log(jsondata);

    const res = await fetch('http://127.0.0.1:8050/product',
        {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type':'application/json'
            },
            body: JSON.stringify(jsondata)
        })

        .then(res => {   // 서버로의 응답 처리
            alert('상품 등록 성공!!');
        }).catch((error) => {
            alert('상품 등록 실패!!');
            console.log(data.detail);
        });

});