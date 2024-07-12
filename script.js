function domReady(fn) {
	if (
		document.readyState === "complete" ||
		document.readyState === "interactive"
	) {
		setTimeout(fn, 1000);
	} else {
		document.addEventListener("DOMContentLoaded", fn);
	}
}

domReady(function () {

	// If found you qr code
	// function onScanSuccess(decodeText, decodeResult) {
	// 	alert("You Qr is : " + decodeText, decodeResult);
	// }

	function onScanSuccess(decodeText, decodeResult) {
		const linkContainer = document.createElement("div");
		const link = document.createElement("a");
		link.href = decodeText;
		link.textContent = "Click here to visit: " + decodeText;
		link.target = "_blank";
		linkContainer.appendChild(link);
	
		const qrReaderElement = document.getElementById("my-qr-reader");
		qrReaderElement.appendChild(linkContainer);
	}
	

	let htmlscanner = new Html5QrcodeScanner(
		"my-qr-reader",
		{ fps: 10, qrbos: 250 }
	);
	htmlscanner.render(onScanSuccess);
});
