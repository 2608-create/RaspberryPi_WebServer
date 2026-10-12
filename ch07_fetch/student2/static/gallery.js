const fakePhotos = [
    { title: "사진 1", img: "https://picsum.photos/seed/1/600" },
    { title: "사진 2", img: "https://picsum.photos/seed/2/600" },
    { title: "사진 3", img: "https://picsum.photos/seed/3/600" }
];

const gallery = document.getElementById("gallery");
const moreBtn = document.getElementById("more");

// 사진 목록을 받아 화면에 붙임
function showPhotos(photos) {
    let html = "";
    photos.forEach(photo => {
        html += `
            <div class="col-4 mb-3">
                <img src="${photo.img}" class="img-fluid">
                <p>${photo.title}</p>
            </div>
        `;
    });
    gallery.insertAdjacentHTML("beforeend", html);
}

// 더 보기 버튼 (예시로 완성해둠)
let page = 0;

function loadPhotos(){
	page = page + 1
	fetch("/api/photos?page="+ page)
	.then(function (response){
		if (!response.ok){
			throw new Error("HTTP 오류" + response.status);
		}
		return response.json();
	})
	.then(function (photos){
		showPhotos(photos);
	})
	.catch((error) => {
		alert("사진을 불러오지 못함");
	});
}

moreBtn.addEventListener("click", loadPhotos);   // 더 보기를 누르면 실행
loadPhotos();
	
