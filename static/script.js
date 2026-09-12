function yuborish() {
    const inputElement = document.getElementById('ismInput');
    const resultBox = document.getElementById('resultBox');
    const ismValue = inputElement.value;

    // JavaScript orqali Python (Flask) serveriga so'rov yuboramiz
    fetch('/salomlashtirish', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ ism: ismValue })
    })
    .then(response => response.json())
    .then(data => {
        resultBox.classList.remove('hidden', 'success', 'error');

        if (data.muvaffaqiyat) {
            resultBox.classList.add('success');
            resultBox.innerText = data.xabar;
        } else {
            resultBox.classList.add('error');
            resultBox.innerText = data.xabar;
        }
    })
    .catch(error => {
        resultBox.classList.remove('hidden');
        resultBox.classList.add('error');
        resultBox.innerText = "Server bilan bog'lanishda xatolik yuz berdi.";
    });
}