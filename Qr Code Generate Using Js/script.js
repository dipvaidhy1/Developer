document.addEventListener("DOMContentLoaded", function () {
    function onScanSuccess(decodeText, decodeResult) {
        const qrResultLink = document.getElementById("qr-result-link");
        qrResultLink.href = decodeText;
        qrResultLink.textContent = decodeText;
        qrResultLink.style.display = "block";
        qrResultLink.target = "_blank"; // Opens the link in a new tab
    }

    let html5QrCode = new Html5Qrcode("my-qr-reader");
    const qrCodeScannerConfig = { fps: 10, qrbox: { width: 250, height: 250 } };
    html5QrCode.start(
        { facingMode: "environment" }, // Use the rear camera
        qrCodeScannerConfig,
        onScanSuccess
    ).catch(err => {
        console.error("Unable to start scanning:", err);
    });
});
